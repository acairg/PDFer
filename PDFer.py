'''<- Dev
  Jake Pattinson
  PDfer is a meoified web scraper,
  which renders a website to a PDF doc for offline reference.
'''
from xhtml2pdf import pisa 
import pdfkit
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import os
from PyPDF2 import PdfFileMerger
# imports ^
ls = os.path.dirname(
os.path.realpath(__file__))
#clean slate! delete all PDF before generating 
filelist = [ f for f in os.listdir(ls) if f.endswith(".pdf") ]
for f in filelist:
    os.remove(os.path.join(ls, f))
print(" -----------------------------------------------------------")
print(ls) #prints directory incase you need to cd
print(" -----------------------------------------------------------")

guideURL = input("enter the URL you wish to convert.")
parser = 'html.parser' # or 'lxml' (preferred) or 'html5lib', if installed 
resp = urlopen(guideURL) 
soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))  
for link in soup.find_all('a', href=True): 
  print(link['href']) 
  os.system("xhtml2pdf " + link['href'])
os.system('wkhtmltopdf --load-error-handling ignore http:/#ac-gn-menustat *.pdf')


pdfs = [
f for f in os.listdir(ls)
if f.endswith (".pdf")]
path = ls
pdf_files = pdfs
merger = PdfFileMerger()

for files in pdf_files:
    PdfFileMerger.append(path + files)
if not os.path.exists(path + 'Full Report.pdf'):
    merger.write(path + 'Full Report.pdf')
merger.close()

# test url for input prompt !!!!!!!!!!!!!!
#https://support.apple.com/en-gb/guide/iphone/toc