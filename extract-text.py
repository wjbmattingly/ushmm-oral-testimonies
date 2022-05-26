import glob
from pdf2image import convert_from_path
import pytesseract
import multiprocessing

def extract(filename):
    print (filename)
    pages = convert_from_path(filename, 500)
    text = ""
    for page in pages:
        res = pytesseract.image_to_string(page, config="--psm 6")
        text = text+res+"\n"
    ocr_filename = filename.replace("pdfs", "new_ocr").replace(".pdf", ".txt")
    with open (ocr_filename, "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    files = glob.glob("pdfs/*trs_en.pdf")
    p = multiprocessing.Pool(processes = multiprocessing.cpu_count()-1)
    p.map(extract, files)
