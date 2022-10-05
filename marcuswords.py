import re
import PyPDF2
import random

meditations = PyPDF2.PdfFileReader("Meditations_ A New Translation ( PDFDrive ).pdf",strict=False)
page_content = ""
for page_number in range(52, 159):
    page = meditations.getPage(page_number)
    page_content += page.extract_text()
# get rid of whitespaces\
page_content = re.sub(r'\s+', ' ', page_content)
paragraphs = re.split(r'\d+\.', page_content)
# print first paragraph
# return a random paragraph from the list of paragraphs
print(random.choice(paragraphs))
