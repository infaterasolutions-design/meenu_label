code_to_add = """
/* =========================================================================
   MEENU LABEL - SOLD OUT & LUXURY NOTIFY ME / RESTOCK WAITLIST SYSTEM
   ========================================================================= */

var activeNotifyProduct = {
  id: '',
  size: 'M',
  title: '',
  image: '',
  price: '',
  channel: 'whatsapp'
};

function openNotifyMeModal(productId, size, title, image, price) {
  var backdrop = document.getElementById('meenuNotifyBackdrop');
  if (!backdrop) return;

  activeNotifyProduct.id = productId || '';
  activeNotifyProduct.size = size || 'M';
  activeNotifyProduct.title = title || 'Atelier Silhouette';
  activeNotifyProduct.image = image || '';
  activeNotifyProduct.price = price || '';
  activeNotifyProduct.channel = 'whatsapp';

  // Set modal snapshot info
  var titleEl = document.getElementById('notifyProductTitle');
  if (titleEl) titleEl.textContent = activeNotifyProduct.title;

  var priceEl = document.getElementById('notifyProductPrice');
  if (priceEl) priceEl.textContent = activeNotifyProduct.price;

  var imgEl = document.getElementById('notifyProductImg');
  if (imgEl && activeNotifyProduct.image) {
    imgEl.src = activeNotifyProduct.image;
    imgEl.alt = activeNotifyProduct.title;
  }

  // Update size pills
  var pills = document.querySelectorAll('.notify-size-pill');
  pills.forEach(function(pill) {
    var pillSize = pill.getAttribute('data-size');
    pill.classList.toggle('active', pillSize === activeNotifyProduct.size);
  });

  // Reset channel tabs to WhatsApp
  switchNotifyTab('whatsapp');

  // Clear inputs and errors
  var phoneInput = document.getElementById('notifyPhoneInput');
  if (phoneInput) phoneInput.value = '';
  var emailInput = document.getElementById('notifyEmailInput');
  if (emailInput) emailInput.value = '';

  var phoneErr = document.getElementById('notifyPhoneError');
  if (phoneErr) phoneErr.style.display = 'none';
  var emailErr = document.getElementById('notifyEmailError');
  if (emailErr) emailErr.style.display = 'none';

  // Ensure form is visible, success is hidden
  var formView = document.getElementById('notifyFormView');
  if (formView) formView.style.display = 'block';
  var successView = document.getElementById('notifySuccessView');
  if (successView) successView.style.display = 'none';

  var submitBtn = document.getElementById('notifySubmitBtn');
  if (submitBtn) {
    submitBtn.disabled = false;
    var submitText = document.getElementById('notifySubmitText');
    if (submitText) submitText.innerHTML = 'NOTIFY ME WHEN RESTOCKED &rarr;';
  }

  // Update concierge WhatsApp link
  updateNotifyConciergeLink();

  // Show backdrop with smooth animation
  backdrop.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeNotifyMeModal() {
  var backdrop = document.getElementById('meenuNotifyBackdrop');
  if (backdrop) backdrop.classList.remove('open');
  document.body.style.overflow = '';
}

function closeNotifyMeModalOnBackdrop(event) {
  if (event.target.id === 'meenuNotifyBackdrop') {
    closeNotifyMeModal();
  }
}

function selectNotifySize(size, btn) {
  activeNotifyProduct.size = size;
  var pills = document.querySelectorAll('.notify-size-pill');
  pills.forEach(function(pill) { pill.classList.remove('active'); });
  if (btn) btn.classList.add('active');
  updateNotifyConciergeLink();
}

function switchNotifyTab(channel) {
  activeNotifyProduct.channel = channel;
  var tabWa = document.getElementById('notifyTabWhatsApp');
  var tabEm = document.getElementById('notifyTabEmail');
  var groupWa = document.getElementById('notifyWhatsAppGroup');
  var groupEm = document.getElementById('notifyEmailGroup');

  if (channel === 'whatsapp') {
    if (tabWa) tabWa.classList.add('active');
    if (tabEm) tabEm.classList.remove('active');
    if (groupWa) groupWa.style.display = 'block';
    if (groupEm) groupEm.style.display = 'none';
  } else {
    if (tabWa) tabWa.classList.remove('active');
    if (tabEm) tabEm.classList.add('active');
    if (groupWa) groupWa.style.display = 'none';
    if (groupEm) groupEm.style.display = 'block';
  }
}

function updateNotifyConciergeLink() {
  var conciergeBtn = document.getElementById('notifyConciergeWhatsAppBtn');
  if (conciergeBtn) {
    var msg = 'Hi Meenu Label! I would like to reserve or be notified when "' + (activeNotifyProduct.title || 'this ensemble') + '" in Size ' + (activeNotifyProduct.size || 'M') + ' is crafted again. Please share restock timeline.';
    conciergeBtn.href = 'https://wa.me/919988898845?text=' + encodeURIComponent(msg);
  }
}

function submitNotifyMeRequest() {
  var channel = activeNotifyProduct.channel;
  var contactValue = '';

  if (channel === 'whatsapp') {
    var phoneInput = document.getElementById('notifyPhoneInput');
    var phoneErr = document.getElementById('notifyPhoneError');
    var rawPhone = phoneInput ? phoneInput.value.trim().replace(/\\D/g, '') : '';
    if (!rawPhone || rawPhone.length !== 10) {
      if (phoneErr) phoneErr.style.display = 'block';
      if (phoneInput) phoneInput.focus();
      return;
    }
    if (phoneErr) phoneErr.style.display = 'none';
    contactValue = '+91 ' + rawPhone;
  } else {
    var emailInput = document.getElementById('notifyEmailInput');
    var emailErr = document.getElementById('notifyEmailError');
    var rawEmail = emailInput ? emailInput.value.trim() : '';
    var emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
    if (!rawEmail || !emailRegex.test(rawEmail)) {
      if (emailErr) emailErr.style.display = 'block';
      if (emailInput) emailInput.focus();
      return;
    }
    if (emailErr) emailErr.style.display = 'none';
    contactValue = rawEmail;
  }

  // Visual submit state
  var submitBtn = document.getElementById('notifySubmitBtn');
  var submitText = document.getElementById('notifySubmitText');
  if (submitBtn) submitBtn.disabled = true;
  if (submitText) submitText.innerHTML = 'RESERVING WAITLIST...';

  // Save to localStorage
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
  }, 400);
}
"""

old_create_row = """function createSnitchSizeRow(container, sizeName, variantId, isAvailable) {
  var row = document.createElement('button');
  row.type = 'button';
  row.className = 'snitch-size-row' + (!isAvailable ? ' disabled' : '');
  
  var nameSpan = document.createElement('span');
  nameSpan.className = 'snitch-size-name';
  nameSpan.textContent = sizeName;
  row.appendChild(nameSpan);

  var statusSpan = document.createElement('span');
  statusSpan.className = 'snitch-size-status';
  if (!isAvailable) {
    statusSpan.textContent = 'OUT OF STOCK';
  }
  row.appendChild(statusSpan);

  if (isAvailable) {
    row.onclick = function() {
      snitchAddSizeToCart(row, variantId, sizeName);
    };
  }

  container.appendChild(row);
}"""

new_create_row = """function createSnitchSizeRow(container, sizeName, variantId, isAvailable) {
  var row = document.createElement('button');
  row.type = 'button';
  row.className = 'snitch-size-row' + (!isAvailable ? ' disabled sold-out' : '');
  
  var nameSpan = document.createElement('span');
  nameSpan.className = 'snitch-size-name';
  nameSpan.textContent = sizeName;
  row.appendChild(nameSpan);

  var statusSpan = document.createElement('span');
  statusSpan.className = 'snitch-size-status' + (!isAvailable ? ' sold-out-status' : '');
  if (!isAvailable) {
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
  }

  container.appendChild(row);
}"""

for path in ['assets/meenu-theme.js', 'meenu-label-shopify-theme/assets/meenu-theme.js']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if old_create_row in content:
        content = content.replace(old_create_row, new_create_row, 1)
        print(f'Replaced createSnitchSizeRow in {path}')
    else:
        print(f'Old createSnitchSizeRow not found in {path}')

    if 'activeNotifyProduct' not in content:
        content += '\n' + code_to_add
        print(f'Appended notify me JS to {path}')
    else:
        print(f'activeNotifyProduct already in {path}')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
