import re
import PyPDF2 as pd2
import random

with open("Meditations_ A New Translation ( PDFDrive ).pdf", "rb") as f:
    meditations = pd2.PdfFileReader(f, strict=False)
    page_content = ""
    chapter1 = range(44, 51)
    chapter2 = range(52, 57)
    chapter3 = range(58, 64)
    chapter4 = range(65, 75)
    chapter5 = range(76, 86)
    chapter6 = range(87, 97)
    chapter7 = range(98, 108)
    chapter8 = range(109, 119)
    chapter9 = range(120, 129)
    chapter10 = range(130, 140)
    chapter11 = range(141, 150)
    chapter12 = range(151, 158)
    chapters = [chapter1, chapter2, chapter3, chapter4, chapter5, chapter6,
                chapter7, chapter8, chapter9, chapter10, chapter11, chapter12]
    # pick a random chapter
    chapter = random.choice(chapters)
    # get page content
    for i in chapter:
        page = meditations.getPage(i)
        page_content += page.extract_text()
    # get rid of whitespaces\
    page_content = re.sub(r'\s+', ' ', page_content)
    paragraphs = re.split(r'\d+\.', page_content)
    # print first paragraph
    # return a random paragraph from the list of paragraphs
print(random.choice(paragraphs))
