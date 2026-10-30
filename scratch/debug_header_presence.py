with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect everything between <header> and </header>
h_start = html.find('<header>')
h_end = html.find('</header>') + 9
print("=== HEADER IN DOWNLOADS HTML ===")
print(html[h_start:h_end][:1000])

# Now let's check: Is there any other header in the file?
print("Occurrences of <header>:", html.count('<header>'))
print("Occurrences of hamburger-btn:", html.count('hamburger-btn'))
