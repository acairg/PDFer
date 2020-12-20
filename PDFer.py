'''
  Jake Pattinson
  2020-12-19
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

input("Please, press enter to continue.....")
print(" -----------------------------------------------------------")
input('    Please, press enter to continue........... ')
print(" -----------------------------------------------------------")
merger = PdfFileMerger()
for i in os.listdir(ls):
    if i.endswith('.pdf'):
        merger.append(i, 'r+b')
merger.write(ls + 'MergeGuide.pdf')
merger.close()
for f in filelist:
  os.remove(os.path.join(ls, f))

# test url for input prompt
#.     https://support.apple.com/en-gb/guide/iphone/toc
