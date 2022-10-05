import re
import PyPDF2 as pd2
import random
import pandas as pd

with open("Meditations_ A New Translation ( PDFDrive ).pdf","rb") as f:
    meditations = pd2.PdfFileReader(f, strict=False)
    page_content = ""
    # give random page numebr 52-159
    # 
    pagetodecide = random.randint(52,159)
    # get page content
    for i in range(52,159):
        page = meditations.getPage(i)
        page_content += page.extract_text()
    # get rid of whitespaces\
    page_content = re.sub(r'\s+', ' ', page_content)
    paragraphs = re.split(r'\d+\.', page_content)
    # print first paragraph
    # return a random paragraph from the list of paragraphs
print(random.choice(paragraphs))

