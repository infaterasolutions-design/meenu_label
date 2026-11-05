import os
import sys
import time
from playwright.sync_api import sync_playwright

def verify():
    artifact_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
    html_path = r"C:\Users\sande\Documents\antigravity\splendid-nobel\index.html"
    file_url = f"file:///{html_path.replace(os.sep, '/')}"

    errors = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 900})
        page = context.new_page()

        # Capture console messages and errors
        page.on("console", lambda msg: print(f"[Browser Console] {msg.type}: {msg.text}") if msg.type in ["error", "warning"] else None)
        page.on("pageerror", lambda exc: errors.append(str(exc)))

        print("Navigating to page:", file_url)
        page.goto(file_url, wait_until="networkidle")
        page.wait_for_timeout(1000)

        if errors:
            print("CRITICAL: JS errors on load:", errors)
        else:
            print("Verified: No JS errors on page load!")

        # 1. Check initial badge states
        header_wishlist = page.locator("#headerWishlistCount")
        header_cart = page.locator("#headerCartCount")
        print("Initial wishlist badge display:", header_wishlist.evaluate("el => getComputedStyle(el).display"))
        print("Initial cart badge display:", header_cart.evaluate("el => getComputedStyle(el).display"))

        # 2. Find first plus trigger button on product card
        plus_btn = page.locator(".snitch-plus-trigger").first
        plus_btn.scroll_into_view_if_needed()
        prod_id = plus_btn.get_attribute("data-product-id")
        print(f"Clicking '+' trigger for product {prod_id}...")
        plus_btn.click()
        page.wait_for_timeout(400)

        # 3. Check popup is open
        backdrop = page.locator("#snitchSizeModalBackdrop")
        is_open = backdrop.evaluate("el => el.classList.contains('open')")
        print("Quick Size popup open status:", is_open)
        assert is_open, "Quick Size popup did not open!"

        # 4. Check Wishlist button in popup header
        popup_wish_btn = page.locator("#snitchSizeWishlistBtn")
        is_active_initial = popup_wish_btn.evaluate("el => el.classList.contains('active')")
        print("Initial popup wishlist active:", is_active_initial)
        assert not is_active_initial, "Should not be active initially!"

        # Screenshot 1: Popup open with inactive heart
        shot1 = os.path.join(artifact_dir, "verified_popup_initial_heart.png")
        page.screenshot(path=shot1)
        print("Saved screenshot 1:", shot1)

        # 5. Click the heart icon in popup
        print("Clicking popup wishlist heart...")
        popup_wish_btn.click()
        page.wait_for_timeout(300)

        # Check popup wishlist button active state
        is_active_after_click = popup_wish_btn.evaluate("el => el.classList.contains('active')")
        print("Popup wishlist active after click:", is_active_after_click)
        assert is_active_after_click, "Wishlist button should be active (.active)!"

        # Check header wishlist count
        wish_count_text = header_wishlist.text_content()
        wish_count_display = header_wishlist.evaluate("el => getComputedStyle(el).display")
        print(f"Header Wishlist count: '{wish_count_text}', display: '{wish_count_display}'")
        assert wish_count_text == "1", f"Header wishlist count should be 1, got {wish_count_text}"
        assert wish_count_display == "inline-flex", f"Header wishlist badge should be inline-flex, got {wish_count_display}"

        # Check cart badge is still 0 / hidden
        cart_count_text = header_cart.text_content()
        cart_count_display = header_cart.evaluate("el => getComputedStyle(el).display")
        print(f"Header Cart count: '{cart_count_text}', display: '{cart_count_display}'")
        assert cart_count_display == "none", "Cart count should still be hidden!"

        # Screenshot 2: Popup with active red filled heart & header wishlist count = 1
        shot2 = os.path.join(artifact_dir, "verified_popup_wishlist_active.png")
        page.screenshot(path=shot2)
        print("Saved screenshot 2:", shot2)

        # 6. Click heart icon again to remove
        print("Clicking popup wishlist heart again to toggle off...")
        popup_wish_btn.click()
        page.wait_for_timeout(300)

        is_active_after_second_click = popup_wish_btn.evaluate("el => el.classList.contains('active')")
        print("Popup wishlist active after second click:", is_active_after_second_click)
        assert not is_active_after_second_click, "Wishlist button should be inactive after second click!"

        wish_count_display2 = header_wishlist.evaluate("el => getComputedStyle(el).display")
        print(f"Header Wishlist badge display after toggle off: '{wish_count_display2}'")
        assert wish_count_display2 == "none", "Header wishlist badge should be hidden after removing item!"

        # 7. Wishlist it again so we can test reopening persistence
        print("Re-saving to wishlist...")
        popup_wish_btn.click()
        page.wait_for_timeout(300)
        assert popup_wish_btn.evaluate("el => el.classList.contains('active')")

        # Close popup
        page.locator("#snitchSizeModalBackdrop").click(position={"x": 50, "y": 50})
        page.wait_for_timeout(400)
        assert not backdrop.evaluate("el => el.classList.contains('open')"), "Popup should be closed"

        # 8. Reopen popup with '+' button and verify heart is active upon opening!
        print("Reopening popup for same product...")
        plus_btn.click()
        page.wait_for_timeout(400)
        is_active_on_reopen = popup_wish_btn.evaluate("el => el.classList.contains('active')")
        print("Popup wishlist active on reopen:", is_active_on_reopen)
        assert is_active_on_reopen, "Heart should reflect saved wishlist state upon popup opening!"

        # 9. Now select a size from the popup to ensure Cart works simultaneously and independently
        size_m_btn = page.locator(".snitch-size-row").filter(has_text="M").first
        print("Selecting size M from popup...")
        size_m_btn.click()
        page.wait_for_timeout(500)

        # Verify cart badge is now 1, and wishlist badge is also 1
        cart_count_now = header_cart.text_content()
        cart_display_now = header_cart.evaluate("el => getComputedStyle(el).display")
        wish_count_now = header_wishlist.text_content()
        wish_display_now = header_wishlist.evaluate("el => getComputedStyle(el).display")
        print(f"Final badges -> Cart: '{cart_count_now}' ({cart_display_now}), Wishlist: '{wish_count_now}' ({wish_display_now})")
        assert cart_count_now == "1" and cart_display_now == "inline-flex", "Cart count should be 1"
        assert wish_count_now == "1" and wish_display_now == "inline-flex", "Wishlist count should be 1"

        # Screenshot 3: Final dual badges independent state
        shot3 = os.path.join(artifact_dir, "verified_popup_dual_badges_success.png")
        page.screenshot(path=shot3)
        print("Saved screenshot 3:", shot3)

        browser.close()
        print("ALL VERIFICATION CHECKS PASSED PERFECTLY!")

if __name__ == "__main__":
    verify()
