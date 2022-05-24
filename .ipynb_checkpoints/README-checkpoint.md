# USHMM Oral Testimonies
This repository houses the ~1,300 pdfs available of oral testimonies in English at the United States Holocaust Memorial Museum. It also houses the extracted OCR output in 2 forms.

1) ocr_no_breaks - used for machine learning
2) json - structured data.

# Notebook
The notebook text2json demonstrates how to convert the ocr_no_break files into structured JSON files with each segment of question and answer separated out using RegEx. Manual validation remains to be done for several areas where the rules were not able to correctly parse the OCR output. In the JSON files, these segments are indicated with the key, "validation_needed" and a value set to True.