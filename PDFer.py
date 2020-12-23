'''
  Jake Pattinson
  PDFer
'''
from xhtml2pdf import pisa
import pdfkit
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import os
from PyPDF2 import PdfFileMerger, PdfFileWriter
# imports ^
ls = os.path.dirname(
os.path.realpath(__file__))
#clean slate! delete all PDF before generating
filelist = [ f for f in os.listdir(ls) if f.endswith(".pdf") ]

#
for f in filelist:
    os.remove(os.path.join(ls, f))
print(" -----------------------------------------------------------")
print(ls) #prints directory incase you need it
print(" -----------------------------------------------------------")
guideURL = input("enter the URL you wish to convert: ")
parser = 'html.parser' # or 'lxml' (preferred) or 'html5lib', if installed
resp = urlopen(guideURL)
soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))
x= 0
for link in soup.find_all('a', href=True):
  print(link['href'])
  x=x+1
  print(x)
  os.system("wkhtmltopdf --lowquality --disable-smart-shrinking --load-error-handling ignore " + link['href'] + " out" + str(x) + ".pdf")
