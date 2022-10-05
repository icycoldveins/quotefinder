import re
import PyPDF2 as pd2
import random

with open("Meditations_ A New Translation ( PDFDrive ).pdf", "rb") as f:
    meditations = pd2.PdfFileReader(f, strict=False)
    page_content = ""
    chapter1 = range(44, 52)
    chapter2 = range(52, 58)
    chapter3 = range(58, 65)
    chapter4 = range(65, 76)
    chapter5 = range(76, 87)
    chapter6 = range(87, 98)
    chapter7 = range(98, 109)
    chapter8 = range(109, 120)
    chapter9 = range(120, 130)
    chapter10 = range(130, 141)
    chapter11 = range(141, 151)
    chapter12 = range(151, 159)
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
