import PyPDF2
import glob
from pdf2image import convert_from_path
import pytesseract

files = glob.glob("pdfs/*trs_en.pdf")
len(files)