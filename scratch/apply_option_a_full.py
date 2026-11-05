# scratch/apply_option_a_full.py

target_row = """  if (!isAvailable) {
    statusSpan.textContent = 'SOLD OUT • NOTIFY ME';
  }
  row.appendChild(statusSpan);

  if (isAvailable) {
    row.onclick = function() {
      snitchAddSizeToCart(row, variantId, sizeName);
    };
  } else {
    row.onclick = function() {
      closeSnitchSizePopup();
      openNotifyMeModal(
        activeSnitchProduct.id,
        sizeName,
        activeSnitchProduct.title,
        activeSnitchProduct.image,
        activeSnitchProduct.price
      );
    };
  }"""

replacement_row = """  if (!isAvailable) {
    statusSpan.innerHTML = '<span style="color:#25D366; font-size:12px; margin-right:4px;">&#128172;</span> NOTIFY ON WHATSAPP';
  }
  row.appendChild(statusSpan);

  if (isAvailable) {
    row.onclick = function() {
      snitchAddSizeToCart(row, variantId, sizeName);
    };
  } else {
    row.onclick = function() {
      closeSnitchSizePopup();
      var msg = 'Hi Meenu Label! Please notify me when \"' + (activeSnitchProduct ? activeSnitchProduct.title : 'this silhouette') + '\" in Size ' + sizeName + ' is back in stock. Please share restock timeline.';
      var waUrl = 'https://wa.me/919988898845?text=' + encodeURIComponent(msg);
      window.open(waUrl, '_blank');
      if (typeof showMeenuToast === 'function') {
        showMeenuToast('Opening WhatsApp Concierge for Size ' + sizeName + '... 💬');
      }
    };
  }"""

target_submit = """  // Save to localStorage
  try {
    var alerts = JSON.parse(localStorage.getItem('meenu_restock_alerts') || '[]');
    alerts.push({
      productId: activeNotifyProduct.id,
      title: activeNotifyProduct.title,
      size: activeNotifyProduct.size,
      channel: channel,
      contact: contactValue,
      timestamp: new Date().toISOString()
    });
    localStorage.setItem('meenu_restock_alerts', JSON.stringify(alerts));
  } catch(e) {}

  setTimeout(function() {
    var formView = document.getElementById('notifyFormView');
    var successView = document.getElementById('notifySuccessView');
    var sizeDisplay = document.getElementById('notifySuccessSize');

    if (sizeDisplay) sizeDisplay.textContent = activeNotifyProduct.size;
    if (formView) formView.style.display = 'none';
    if (successView) successView.style.display = 'block';

    if (typeof showMeenuToast === 'function') {
      showMeenuToast('Waitlist confirmed for Size ' + activeNotifyProduct.size + ' ✨');
    } else if (typeof showToast === 'function') {
      showToast('Waitlist confirmed for Size ' + activeNotifyProduct.size + ' ✨');
    }
  }, 400);"""

replacement_submit = """  // Save to localStorage
  try {
    var alerts = JSON.parse(localStorage.getItem('meenu_restock_alerts') || '[]');
    alerts.push({
      productId: activeNotifyProduct.id,
      title: activeNotifyProduct.title,
      size: activeNotifyProduct.size,
      channel: channel,
      contact: contactValue,
      timestamp: new Date().toISOString()
    });
    localStorage.setItem('meenu_restock_alerts', JSON.stringify(alerts));
  } catch(e) {}

  // Direct WhatsApp Concierge (Option A): Open WhatsApp chat directly so the merchant receives phone number & request!
  if (channel === 'whatsapp') {
    var waMsg = 'Hi Meenu Label! My contact number is ' + contactValue + '. Please notify me when \"' + (activeNotifyProduct.title || 'this silhouette') + '\" in Size ' + (activeNotifyProduct.size || 'M') + ' is back in stock. Please share restock timeline.';
    var waUrl = 'https://wa.me/919988898845?text=' + encodeURIComponent(waMsg);
    window.open(waUrl, '_blank');
  }

  // Also submit to Shopify native /contact endpoint in the background
  try {
    var formData = new FormData();
    formData.append('form_type', 'contact');
    formData.append('utf8', '✓');
    formData.append('contact[tags]', 'restock-waitlist, ' + (activeNotifyProduct.title || '') + ', Size ' + (activeNotifyProduct.size || ''));
    formData.append('contact[body]', 'Restock Alert Request for ' + (activeNotifyProduct.title || '') + ' (Size ' + (activeNotifyProduct.size || '') + '). Customer Contact: ' + contactValue);
    if (channel === 'email') {
      formData.append('contact[email]', contactValue);
    } else {
      var safeDigits = contactValue.replace(/\\D/g, '');
      formData.append('contact[email]', 'restock-' + safeDigits + '@meenulabel.com');
      formData.append('contact[note][WhatsApp_Phone]', contactValue);
    }
    fetch('/contact', { method: 'POST', body: formData }).catch(function(){});
  } catch(e) {}

  setTimeout(function() {
    var formView = document.getElementById('notifyFormView');
    var successView = document.getElementById('notifySuccessView');
    var sizeDisplay = document.getElementById('notifySuccessSize');

    if (sizeDisplay) sizeDisplay.textContent = activeNotifyProduct.size;
    if (formView) formView.style.display = 'none';
    if (successView) successView.style.display = 'block';

    if (channel === 'whatsapp') {
      var successMsg = document.getElementById('notifySuccessMsg');
      if (successMsg) {
        successMsg.innerHTML = 'Connecting with our Chandigarh stylist via WhatsApp! We have recorded your request for Size <strong>' + activeNotifyProduct.size + '</strong> and will message you the moment it is ready.';
      }
    }

    if (typeof showMeenuToast === 'function') {
      showMeenuToast('Waitlist confirmed for Size ' + activeNotifyProduct.size + ' ✨');
    } else if (typeof showToast === 'function') {
      showToast('Waitlist confirmed for Size ' + activeNotifyProduct.size + ' ✨');
    }
  }, 400);"""

for p in ['assets/meenu-theme.js', 'meenu-label-shopify-theme/assets/meenu-theme.js', 'index.html']:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    
    updated = False
    if target_row in content:
        content = content.replace(target_row, replacement_row, 1)
        updated = True
    else:
        print("target_row missing in:", p)

    if target_submit in content:
        content = content.replace(target_submit, replacement_submit, 1)
        updated = True
    else:
        print("target_submit missing in:", p)

    if updated:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print("SUCCESS: Updated", p)
