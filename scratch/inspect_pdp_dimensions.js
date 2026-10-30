const fs = require('fs');
const path = require('path');

let html = fs.readFileSync('C:\\Users\\sande\\Downloads\\Meenu_Label_Desktop_Storefront.html', 'utf-8');

// Let's inspect what elements have overflow or if body has height
console.log("Checking styles...");
