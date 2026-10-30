with open('scratch/build_shopify_theme.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Add sticky-catalog-header into theme.css in build_shopify_theme.py
sticky_css = """.sticky-catalog-header {
  position: sticky;
  top: 98px;
  z-index: 85;
  background: rgba(255, 255, 255, 0.96);
  backdrop-filter: blur(16px);
  padding: 14px 28px;
  border-radius: 12px;
  border: 1px solid var(--border-color);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.05);
  margin-bottom: 28px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
}"""

if ".sticky-catalog-header" not in code:
    code = code.replace(".catalog-section {", sticky_css + "\n.catalog-section {")
    with open('scratch/build_shopify_theme.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Updated build_shopify_theme.py with sticky-catalog-header CSS.")
