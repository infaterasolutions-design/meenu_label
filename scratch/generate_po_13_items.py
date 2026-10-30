import os
import io
import pymupdf
from PIL import Image
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage
)

# 1. Prepare Paths
pdf_in_path = r"C:\Users\sande\Downloads\Selected catalog .pdf"
thumb_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch\po_13_thumbs"
os.makedirs(thumb_dir, exist_ok=True)
pdf_out_path = r"C:\Users\sande\Downloads\Meenu_Label_PO_13_Designs.pdf"

# 13 Selected Designs: (code, page_num, category, fabric, rate, pcs)
items = [
    ("JAB26ST05010", 1, "3-Piece Suit (Kurta+Pant+Dupatta)", "Chanderi (Yellow/Pink)", 925, 3),
    ("SET974", 4, "2-Piece Set (Angrakha+Pant)", "Crepe Silk (Mustard)", 555, 3),
    ("TXC26KB04820", 5, "2-Piece Set (Kurta+Pant)", "Silk Blend (Lime V-Neck)", 685, 3),
    ("JAC25ST03063", 9, "3-Piece Suit (Kurta+Pant+Dupatta)", "Cotton Blend (Baby Pink)", 655, 3),
    ("JAB24ST00932", 10, "3-Piece Fusion (Top+Pant+Shrug)", "Crepe (Black/Floral)", 595, 3),
    ("SET916", 16, "2-Piece Co-ord (Halter+Palazzo)", "Dobby Chiffon (Lime)", 675, 3),
    ("JAC25CD03428", 17, "2-Piece Co-ord (Tunic+Pant)", "Cotton Blend (Ivory)", 555, 3),
    ("JAA26DR04449", 24, "Flared Midi Dress", "Georgette (Navy Floral)", 645, 3),
    ("JNE4046", 25, "Belted Wrap Dress", "Georgette (White Porcelain)", 575, 3),
    ("JAA26DR03942", 28, "Cotton Wrap Dress", "Cotton (Retro Polka Dot)", 595, 3),
    ("TXC26TP04108", 41, "Printed Blouse Top", "Chiffon (Abstract V-Neck)", 395, 3),
    ("TXC26TP04098", 44, "Printed V-Neck Top", "Crepe (White/Black Leaf)", 295, 3),
    ("ZAC26TP04826", 47, "Modern Casual Top", "Crepe (Monochrome Floral)", 345, 3),
]

# 2. Extract and crop clean thumbnails
doc = pymupdf.open(pdf_in_path)

thumb_paths = {}
for code, page_num, cat, fabric, rate, pcs in items:
    page = doc[page_num - 1]
    images = doc.get_page_images(page_num - 1)
    if images:
        xref = images[0][0]
        base_img = doc.extract_image(xref)
        pil_img = Image.open(io.BytesIO(base_img["image"]))
        w, h = pil_img.size
        cropped = pil_img.crop((int(w * 0.05), int(h * 0.12), int(w * 0.95), int(h * 0.88)))
        cropped.thumbnail((140, 210))
        t_path = os.path.join(thumb_dir, f"{code}.jpg")
        cropped.save(t_path, "JPEG", quality=85)
        thumb_paths[code] = t_path

# 3. Build 1-Page PDF with ReportLab
doc_pdf = SimpleDocTemplate(
    pdf_out_path,
    pagesize=A4,
    leftMargin=20,
    rightMargin=20,
    topMargin=14,
    bottomMargin=12
)

styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    "TitleStyle",
    parent=styles["Heading1"],
    fontSize=17,
    leading=20,
    textColor=colors.HexColor("#1A1A1A"),
    spaceAfter=1,
)
subtitle_style = ParagraphStyle(
    "SubTitleStyle",
    parent=styles["Normal"],
    fontSize=8,
    leading=11,
    textColor=colors.HexColor("#555555"),
)
header_label = ParagraphStyle(
    "HeaderLabel",
    parent=styles["Normal"],
    fontSize=8,
    leading=11,
    textColor=colors.HexColor("#222222"),
)
cell_style = ParagraphStyle(
    "CellStyle",
    parent=styles["Normal"],
    fontSize=7.5,
    leading=9.5,
    textColor=colors.HexColor("#222222"),
)
cell_bold = ParagraphStyle(
    "CellBold",
    parent=styles["Normal"],
    fontSize=8,
    leading=10.5,
    fontName="Helvetica-Bold",
    textColor=colors.HexColor("#111111"),
)
cell_center = ParagraphStyle(
    "CellCenter",
    parent=styles["Normal"],
    fontSize=8,
    leading=10.5,
    alignment=1,
    textColor=colors.HexColor("#222222"),
)

elements = []

# Header Box
header_data = [
    [
        Paragraph("<b>MEENU LABEL</b><br/><font size=7.5 color='#666'>Infatera Software Solutions OPC Pvt. Ltd.<br/>Chandigarh, India | meenulabel24@gmail.com</font>", title_style),
        Paragraph("<div align='right'><b>PURCHASE ORDER</b><br/><font size=7.5 color='#555'>PO Date: 17-Oct-2026<br/>Ref: Selected Catalog / Drop 01<br/>Destination: Chandigarh</font></div>", subtitle_style)
    ]
]
header_table = Table(header_data, colWidths=[285, 270])
header_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ("TOPPADDING", (0, 0), (-1, -1), 0),
]))
elements.append(header_table)

# Divider line
divider = Table([[""]], colWidths=[555], rowHeights=[1.5])
divider.setStyle(TableStyle([
    ("LINEABOVE", (0, 0), (-1, -1), 1.2, colors.HexColor("#2B2723")),
]))
elements.append(divider)
elements.append(Spacer(1, 2))

# Note to dealer
note_p = Paragraph(
    "<b>Order Details:</b> Sampling / Debut Collection Order. Please supply <b>3 Pieces per design in Sizes: M, L, XL (1 piece each)</b>. Total 13 designs = 39 pieces. Please share your Proforma Invoice & Bank Details for immediate payment.",
    header_label
)
elements.append(note_p)
elements.append(Spacer(1, 3))

# Table Header
table_data = [
    [
        Paragraph("<b>Photo</b>", cell_center),
        Paragraph("<b>Design Code & Category</b>", cell_bold),
        Paragraph("<b>Fabric</b>", cell_bold),
        Paragraph("<b>Sizes (1 each)</b>", cell_center),
        Paragraph("<b>Rate (Rs.)</b>", cell_center),
        Paragraph("<b>Qty</b>", cell_center),
        Paragraph("<b>Total (Rs.)</b>", cell_center),
    ]
]

subtotal = 0
total_pcs = 0

for idx, (code, page_num, cat, fabric, rate, pcs) in enumerate(items, 1):
    amount = rate * pcs
    subtotal += amount
    total_pcs += pcs
    
    img_widget = Paragraph("Photo", cell_center)
    if code in thumb_paths and os.path.exists(thumb_paths[code]):
        try:
            # 24w x 36h to guarantee single page fit
            img_widget = RLImage(thumb_paths[code], width=24, height=36)
        except:
            pass

    desc_p = Paragraph(f"<b>{code}</b><br/><font size=6.5 color='#666'>Pg #{page_num} | {cat}</font>", cell_style)
    fabric_p = Paragraph(fabric, cell_style)
    sizes_p = Paragraph("<b>M, L, XL</b>", cell_center)
    rate_p = Paragraph(f"Rs. {rate}", cell_center)
    qty_p = Paragraph(f"<b>{pcs}</b>", cell_center)
    amt_p = Paragraph(f"<b>Rs. {amount:,}</b>", cell_center)

    table_data.append([img_widget, desc_p, fabric_p, sizes_p, rate_p, qty_p, amt_p])

gst_5 = round(subtotal * 0.05, 2)
grand_total = subtotal + gst_5

# Summary Rows
table_data.append(["", "", "", "", Paragraph("<b>Subtotal:</b>", cell_bold), Paragraph(f"<b>{total_pcs} pcs</b>", cell_center), Paragraph(f"<b>Rs. {subtotal:,}</b>", cell_center)])
table_data.append(["", "", "", "", Paragraph("<b>GST (5%):</b>", cell_style), "", Paragraph(f"Rs. {gst_5:,}", cell_center)])
table_data.append(["", "", "", "", Paragraph("<b>GRAND TOTAL:</b>", cell_bold), "", Paragraph(f"<font color='#B22222' size=9><b>Rs. {round(grand_total):,}</b></font>", cell_center)])

col_widths = [42, 154, 134, 75, 52, 38, 60]
t = Table(table_data, colWidths=col_widths, repeatRows=1)
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F5F2EB")),
    ("ALIGN", (0, 0), (-1, 0), "CENTER"),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
    ("TOPPADDING", (0, 0), (-1, -1), 1.5),
    ("GRID", (0, 0), (-1, len(items)), 0.5, colors.HexColor("#E0DCD5")),
    ("LINEBELOW", (0, 0), (-1, 0), 1.2, colors.HexColor("#2B2723")),
    ("LINEABOVE", (4, len(items)+1), (-1, len(items)+1), 1, colors.HexColor("#2B2723")),
    ("BACKGROUND", (4, -1), (-1, -1), colors.HexColor("#FDF9F3")),
    ("SPAN", (4, len(items)+1), (4, len(items)+1)),
]))

elements.append(t)
elements.append(Spacer(1, 4))

# Footer instructions
footer_p = Paragraph(
    "<font size=7.5 color='#444'><b>Payment & Dispatch:</b> Payment will be processed immediately upon receipt of Bank Details / Invoice. Please pack with individual poly-bags and dispatch to Chandigarh via express transport.</font>",
    subtitle_style
)
elements.append(footer_p)

doc_pdf.build(elements)
print(f"SUCCESS: 1-Page 13-Item PO generated at {pdf_out_path}")
