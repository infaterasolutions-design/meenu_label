import subprocess, os

# Create test HTML based on index.html with the proposed CSS and JS enhancements
with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\index.html', 'r', encoding='utf-8') as f:
    sf_html = f.read()

# Let's inspect index.html search css
print("Found search-close-action in index.html:", sf_html.count('.search-close-action'))
print("Found toggleSearchBar in index.html:", sf_html.count('toggleSearchBar'))
