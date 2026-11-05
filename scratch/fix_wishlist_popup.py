import os
import sys

def fix_meenu_theme_js(file_path):
    print(f"Fixing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update updateWishlistUI to sync #snitchSizeWishlistBtn
    old_ui_sync = "  // 5. Render Wishlist Drawer items list"
    new_ui_sync = """  // 4b. Update Quick Size drawer Wishlist heart if open
  var snitchWishBtn = document.getElementById('snitchSizeWishlistBtn');
  if (snitchWishBtn) {
    var sId = snitchWishBtn.getAttribute('data-wishlist-id') || (typeof activeSnitchProduct !== 'undefined' && activeSnitchProduct ? activeSnitchProduct.id : null);
    if (sId) {
      var isSActive = list.some(function(it) { return String(it.id) === String(sId); });
      snitchWishBtn.classList.toggle('active', isSActive);
    }
  }

  // 5. Render Wishlist Drawer items list"""

    if old_ui_sync in content and "4b. Update Quick Size drawer Wishlist" not in content:
        content = content.replace(old_ui_sync, new_ui_sync, 1)
        print("  -> updateWishlistUI patched successfully.")

    # 2. Update openQuickSizePopup to initialize wishlist state & attributes
    old_open_wish = """  // Sync Wishlist button in header
  var wishBtn = document.getElementById('snitchSizeWishlistBtn');
  if (wishBtn) {
    if (typeof wishlist !== 'undefined' && wishlist.indexOf(productId) !== -1) {
      wishBtn.classList.add('active');
    } else {
      wishBtn.classList.remove('active');
    }
  }"""

    new_open_wish = """  // Sync Wishlist button in header
  var wishBtn = document.getElementById('snitchSizeWishlistBtn');
  if (wishBtn) {
    var isSaved = false;
    if (typeof isWishlisted === 'function') {
      isSaved = isWishlisted(productId);
    } else if (typeof wishlist !== 'undefined') {
      isSaved = wishlist.indexOf(productId) !== -1;
    }
    wishBtn.classList.toggle('active', isSaved);
    wishBtn.setAttribute('data-wishlist-id', productId);
    wishBtn.setAttribute('data-wishlist-title', title);
    wishBtn.setAttribute('data-wishlist-price', price);
    wishBtn.setAttribute('data-wishlist-image', img);
    wishBtn.setAttribute('data-wishlist-url', url);
  }"""

    if old_open_wish in content:
        content = content.replace(old_open_wish, new_open_wish, 1)
        print("  -> openQuickSizePopup wishlist sync patched successfully.")

    # 3. Update toggleSnitchSizeWishlist
    old_toggle_wish = """function toggleSnitchSizeWishlist(btn) {
  if (!activeSnitchProduct) return;
  btn.classList.toggle('active');
  if (typeof toggleWishlistProduct === 'function') {
    toggleWishlistProduct(activeSnitchProduct.id);
  } else if (typeof toggleWishlist === 'function') {
    // create a pseudo button or call
    var wishId = activeSnitchProduct.id;
    if (typeof wishlist !== 'undefined') {
      var idx = wishlist.indexOf(wishId);
      if (idx === -1) {
        wishlist.push(wishId);
      } else {
        wishlist.splice(idx, 1);
      }
      try { localStorage.setItem('meenu_wishlist', JSON.stringify(wishlist)); } catch(e) {}
    }
  }
}"""

    new_toggle_wish = """function toggleSnitchSizeWishlist(btn) {
  if (!activeSnitchProduct) return;
  var pId = String(activeSnitchProduct.id);

  // 1. Live Shopify theme environment (localStorage 'meenu_saved_wishlist')
  if (typeof getWishlist === 'function' && typeof saveWishlist === 'function') {
    var list = getWishlist();
    var idx = list.findIndex(function(it) { return String(it.id) === pId; });
    var willBeSaved = (idx === -1);

    if (idx >= 0) {
      list.splice(idx, 1);
      saveWishlist(list);
      if (typeof showMeenuToast === 'function') showMeenuToast('Removed from Wishlist');
    } else {
      list.push({
        id: pId,
        title: activeSnitchProduct.title || 'Atelier Silhouette',
        price: activeSnitchProduct.price || '',
        image: activeSnitchProduct.image || '',
        url: activeSnitchProduct.url || '#'
      });
      saveWishlist(list);
      if (typeof showMeenuToast === 'function') showMeenuToast('Saved to Wishlist ❤️');
    }
    btn.classList.toggle('active', willBeSaved);
    var cardBtn = document.querySelector('[data-wishlist-id="' + pId + '"]');
    if (cardBtn) cardBtn.classList.toggle('active', willBeSaved);
    return;
  }

  // 2. Standalone preview environment (index.html, global wishlist array)
  if (typeof wishlist !== 'undefined') {
    var idx = wishlist.indexOf(pId);
    var cardWishBtn = document.getElementById('wishBtn_' + pId) || document.querySelector('[data-wishlist-id="' + pId + '"]');
    if (idx === -1) {
      wishlist.push(pId);
      btn.classList.add('active');
      if (cardWishBtn) cardWishBtn.classList.add('active');
      if (typeof showToast === 'function') showToast('Added to your Wishlist!');
    } else {
      wishlist.splice(idx, 1);
      btn.classList.remove('active');
      if (cardWishBtn) cardWishBtn.classList.remove('active');
      if (typeof showToast === 'function') showToast('Removed from your Wishlist.');
    }
    if (typeof updateWishlistUI === 'function') {
      updateWishlistUI();
    }
    return;
  }

  btn.classList.toggle('active');
}"""

    if old_toggle_wish in content:
        content = content.replace(old_toggle_wish, new_toggle_wish, 1)
        print("  -> toggleSnitchSizeWishlist patched successfully.")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved {file_path}.")


def fix_index_html(file_path):
    print(f"Fixing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Close </script> and open <style> after showToast
    target_split_1 = """    function showToast(msg) {
      var t = document.getElementById('toastNote');
      t.textContent = msg;
      t.style.display = 'block';
      setTimeout(function() { t.style.display = 'none'; }, 3200);
    }
  
/* ========================================================
   EXACT SNITCH-STYLE QUICK SIZE POPUP DRAWER
   ======================================================== */"""

    replacement_split_1 = """    function showToast(msg) {
      var t = document.getElementById('toastNote');
      t.textContent = msg;
      t.style.display = 'block';
      setTimeout(function() { t.style.display = 'none'; }, 3200);
    }
  </script>

  <style>
/* ========================================================
   EXACT SNITCH-STYLE QUICK SIZE POPUP DRAWER
   ======================================================== */"""

    if target_split_1 in content:
        content = content.replace(target_split_1, replacement_split_1, 1)
        print("  -> Closed </script> and opened <style> successfully.")

    # 2. Close </style> before <div class="snitch-size-backdrop">
    target_split_2 = """.snitch-size-row.disabled .snitch-size-status {
  color: #888888 !important;
  font-size: 11px !important;
  text-transform: uppercase !important;
}

<!-- Snitch-Style Quick Size Drawer (Meenu Label) -->"""

    replacement_split_2 = """.snitch-size-row.disabled .snitch-size-status {
  color: #888888 !important;
  font-size: 11px !important;
  text-transform: uppercase !important;
}
  </style>

  <!-- Snitch-Style Quick Size Drawer (Meenu Label) -->"""

    if target_split_2 in content:
        content = content.replace(target_split_2, replacement_split_2, 1)
        print("  -> Closed </style> before Quick Size drawer HTML.")

    # 3. Open <script> before EXACT SNITCH-STYLE QUICK SIZE DRAWER LOGIC
    target_split_3 = """    <!-- Size Rows List (Exact Snitch Stack) -->
    <div class="snitch-size-list" id="snitchSizeList">
      <!-- Dynamically generated rows: XS, S, M, L, XL, XXL -->
    </div>
  </div>
</div>


/* ========================================================
   EXACT SNITCH-STYLE QUICK SIZE DRAWER LOGIC
   ======================================================== */"""

    replacement_split_3 = """    <!-- Size Rows List (Exact Snitch Stack) -->
    <div class="snitch-size-list" id="snitchSizeList">
      <!-- Dynamically generated rows: XS, S, M, L, XL, XXL -->
    </div>
  </div>
</div>

  <script>
/* ========================================================
   EXACT SNITCH-STYLE QUICK SIZE DRAWER LOGIC
   ======================================================== */"""

    if target_split_3 in content:
        content = content.replace(target_split_3, replacement_split_3, 1)
        print("  -> Opened <script> before Quick Size drawer JS logic.")

    # 4. In updateWishlistUI, sync #snitchSizeWishlistBtn and card buttons
    old_update_wish_index = """    function updateWishlistUI() {
      var countEl = document.getElementById('headerWishlistCount');
      if (countEl) { countEl.textContent = wishlist.length; countEl.style.display = wishlist.length > 0 ? 'inline-flex' : 'none'; }
      var drawerCountEl = document.getElementById('wishlistDrawerCount');
      if (drawerCountEl) drawerCountEl.textContent = wishlist.length;
      var container = document.getElementById('wishlistItemsList');"""

    new_update_wish_index = """    function updateWishlistUI() {
      var countEl = document.getElementById('headerWishlistCount');
      if (countEl) { countEl.textContent = wishlist.length; countEl.style.display = wishlist.length > 0 ? 'inline-flex' : 'none'; }
      var drawerCountEl = document.getElementById('wishlistDrawerCount');
      if (drawerCountEl) drawerCountEl.textContent = wishlist.length;

      // Sync Quick Size popup Wishlist heart if open
      var snitchWishBtn = document.getElementById('snitchSizeWishlistBtn');
      if (snitchWishBtn && typeof activeSnitchProduct !== 'undefined' && activeSnitchProduct) {
        snitchWishBtn.classList.toggle('active', wishlist.indexOf(activeSnitchProduct.id) !== -1);
      }

      // Sync all card wishlist buttons
      document.querySelectorAll('.card-wishlist-btn').forEach(function(btn) {
        var pid = btn.getAttribute('data-pid') || (btn.id ? btn.id.replace('wishBtn_', '') : null);
        if (pid) {
          btn.classList.toggle('active', wishlist.indexOf(pid) !== -1);
        }
      });

      var container = document.getElementById('wishlistItemsList');"""

    if old_update_wish_index in content:
        content = content.replace(old_update_wish_index, new_update_wish_index, 1)
        print("  -> updateWishlistUI in index.html updated successfully.")

    # 5. Update openQuickSizePopup in index.html
    old_open_wish_index = """  // Sync Wishlist button in header
  var wishBtn = document.getElementById('snitchSizeWishlistBtn');
  if (wishBtn) {
    if (typeof wishlist !== 'undefined' && wishlist.indexOf(productId) !== -1) {
      wishBtn.classList.add('active');
    } else {
      wishBtn.classList.remove('active');
    }
  }"""

    new_open_wish_index = """  // Sync Wishlist button in header
  var wishBtn = document.getElementById('snitchSizeWishlistBtn');
  if (wishBtn) {
    var isSaved = (typeof wishlist !== 'undefined' && wishlist.indexOf(productId) !== -1);
    wishBtn.classList.toggle('active', isSaved);
    wishBtn.setAttribute('data-wishlist-id', productId);
    wishBtn.setAttribute('data-wishlist-title', title);
    wishBtn.setAttribute('data-wishlist-price', price);
    wishBtn.setAttribute('data-wishlist-image', img);
    wishBtn.setAttribute('data-wishlist-url', url);
  }"""

    if old_open_wish_index in content:
        content = content.replace(old_open_wish_index, new_open_wish_index, 1)
        print("  -> openQuickSizePopup wishlist sync in index.html updated.")

    # 6. Update toggleSnitchSizeWishlist in index.html
    old_toggle_wish_index = """function toggleSnitchSizeWishlist(btn) {
  if (!activeSnitchProduct) return;
  btn.classList.toggle('active');
  if (typeof toggleWishlistProduct === 'function') {
    toggleWishlistProduct(activeSnitchProduct.id);
  } else if (typeof toggleWishlist === 'function') {
    // create a pseudo button or call
    var wishId = activeSnitchProduct.id;
    if (typeof wishlist !== 'undefined') {
      var idx = wishlist.indexOf(wishId);
      if (idx === -1) {
        wishlist.push(wishId);
      } else {
        wishlist.splice(idx, 1);
      }
      try { localStorage.setItem('meenu_wishlist', JSON.stringify(wishlist)); } catch(e) {}
    }
  }
}"""

    new_toggle_wish_index = """function toggleSnitchSizeWishlist(btn) {
  if (!activeSnitchProduct) return;
  var pId = String(activeSnitchProduct.id);

  if (typeof wishlist !== 'undefined') {
    var idx = wishlist.indexOf(pId);
    var cardWishBtn = document.getElementById('wishBtn_' + pId) || document.querySelector('[data-wishlist-id="' + pId + '"]');
    if (idx === -1) {
      wishlist.push(pId);
      btn.classList.add('active');
      if (cardWishBtn) cardWishBtn.classList.add('active');
      if (typeof showToast === 'function') showToast('Added to your Wishlist!');
    } else {
      wishlist.splice(idx, 1);
      btn.classList.remove('active');
      if (cardWishBtn) cardWishBtn.classList.remove('active');
      if (typeof showToast === 'function') showToast('Removed from your Wishlist.');
    }
    if (typeof updateWishlistUI === 'function') {
      updateWishlistUI();
    }
    return;
  }

  btn.classList.toggle('active');
}"""

    if old_toggle_wish_index in content:
        content = content.replace(old_toggle_wish_index, new_toggle_wish_index, 1)
        print("  -> toggleSnitchSizeWishlist in index.html updated.")

    # 7. Close </script></body></html> at end of index.html if missing
    content_stripped = content.rstrip()
    if not content_stripped.endswith("</html>"):
        content = content_stripped + "\n  </script>\n</body>\n</html>\n"
        print("  -> Added </script></body></html> at the end of index.html.")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved {file_path}.")


if __name__ == "__main__":
    fix_meenu_theme_js("assets/meenu-theme.js")
    fix_meenu_theme_js("meenu-label-shopify-theme/assets/meenu-theme.js")
    fix_index_html("index.html")
