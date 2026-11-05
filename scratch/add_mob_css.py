def add_mobile_responsive(file_path):
    print(f"Adding mobile responsive rules to {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    mob_rule = """
@media (max-width: 768px) {
  .snitch-size-drawer {
    width: 100vw !important;
    max-width: 100vw !important;
    border-radius: 14px 14px 0 0 !important;
  }
  .snitch-size-header {
    width: 100% !important;
    padding: 0 16px !important;
  }
  .snitch-size-row {
    width: 100% !important;
    padding: 0 16px !important;
  }
}"""

    if "@media (max-width: 768px)" not in content or "snitch-size-drawer" not in content[content.find("@media (max-width: 768px)"):]:
        if file_path.endswith(".html"):
            target = "</style>\n\n  <!-- Snitch-Style Quick Size Drawer (Meenu Label) -->"
            if target in content:
                content = content.replace(target, mob_rule + "\n  " + target, 1)
                print("  -> Inserted in index.html <style>.")
            else:
                # alternative target
                target2 = "</style>"
                last_style = content.rfind(target2)
                if last_style != -1:
                    content = content[:last_style] + mob_rule + "\n  " + content[last_style:]
                    print("  -> Inserted before last </style>.")
        else:
            content = content.rstrip() + "\n" + mob_rule + "\n"
            print("  -> Appended to CSS file.")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved {file_path}.")

add_mobile_responsive("assets/meenu-luxury.css")
add_mobile_responsive("meenu-label-shopify-theme/assets/meenu-luxury.css")
add_mobile_responsive("index.html")
