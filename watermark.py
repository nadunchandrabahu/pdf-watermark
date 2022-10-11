from PyPDF2 import PdfReader, PdfWriter
import sys
import os

while True:
    try:
        source_file = input(
            "Please input name of the file you want to Watermark (.pdf): \n")
        if os.path.exists(source_file):
            break
        else:
            print("Your file does not exist, please try again. \n")
    except:
        print("Error, please try again.\n")

while True:
    try:
        watermark_file = input(
            "Please input name of the watermark file (.pdf): \n")
        if os.path.exists(watermark_file):
            break
        else:
            print("Watermark file not found, please try again.\n")
    except:
        print("Error, please try again.\n")


reader = PdfReader(source_file)
writer = PdfWriter()

page_count = 0
total_pages = reader.getNumPages()
print("Starting...\n")
for current_page in range(0, total_pages):
    source_page = reader.getPage(current_page)
    page_count += 1
    print(f"{page_count}/{total_pages} pages done.")
    watermark_reader = PdfReader(watermark_file)
    watermark_page = watermark_reader.pages[0]

    watermark_page.mergePage(source_page)
    writer.add_page(watermark_page)

with open("watermarked-pdf.pdf", mode="wb") as out_file:
    writer.write(out_file)

print("\nAll Done!\n")
