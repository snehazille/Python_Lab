#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install PyPDF2')
from PyPDF2 import PdfWriter, PdfReader
num = int(input("Enter page number you want combine from multiple documents "))
pdf1 = open('R Programming LabMannual.pdf', 'rb')
pdf2 = open('Python lab Manual.pdf', 'rb')
pdf_writer = PdfWriter()
pdf1_reader = PdfReader(pdf1) 
page = pdf1_reader.pages[num - 1]
pdf_writer.add_page(page)
pdf2_reader = PdfReader(pdf2) 
page = pdf2_reader.pages[num - 1]
pdf_writer.add_page(page)
with open('output.pdf', 'wb') as output:
    pdf_writer.write(output)


# In[ ]:




