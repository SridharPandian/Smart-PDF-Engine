import PyPDF2 as pdf
import bs4 as bs
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from collections import Counter

filename = "A survey on semantic similarity between words in semantic web.pdf"
file = open(filename, 'rb')
read_pdf = pdf.PdfFileReader(file)

number_of_pages = read_pdf.getNumPages()
print(number_of_pages)
count = 0
text = ""

while count<number_of_pages:
    pageObj = read_pdf.getPage(count)
    count+=1
    text += pageObj.extractText()
print(text)

if text!=[]:
    text = text
else:
    print("Error")

tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
token = tokenizer.tokenize(text)
punctuations = ['(',')','.','.,','-',';',':','[',']',',','\n']
stop_words = stopwords.words('english')

keywords = [word for word in token if not word in stop_words and not word in punctuations]

counter = Counter(keywords)
print(counter)