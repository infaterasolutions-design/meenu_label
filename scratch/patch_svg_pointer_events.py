with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    ".header-icon-action svg {{\n      width: 22px;\n      height: 22px;\n      display: block;\n      stroke-width: 1.6;\n    }}",
    ".header-icon-action svg {{\n      width: 22px;\n      height: 22px;\n      display: block;\n      stroke-width: 1.6;\n      pointer-events: none;\n    }}"
)

text = text.replace(
    ".hamburger-btn svg {{\n      width: 22px;\n      height: 22px;\n      display: block;\n    }}",
    ".hamburger-btn svg {{\n      width: 22px;\n      height: 22px;\n      display: block;\n      pointer-events: none;\n    }}"
)

text = text.replace(
    ".card-wishlist-btn svg {{\n      width: 18px;\n      height: 18px;\n      display: block;\n      transition: fill 0.2s ease, stroke 0.2s ease;\n    }}",
    ".card-wishlist-btn svg {{\n      width: 18px;\n      height: 18px;\n      display: block;\n      transition: fill 0.2s ease, stroke 0.2s ease;\n      pointer-events: none;\n    }}"
)

# Also guard selectModalSize with {{ and }}
text = text.replace(
    "el.classList.add('selected');",
    "if (el) el.classList.add('selected');"
)

with open('scratch/build_snitch_storefront.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated SVG pointer-events and selectModalSize guard.")
