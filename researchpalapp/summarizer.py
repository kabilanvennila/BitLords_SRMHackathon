from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import re 
# import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    # fp = open(path, 'rb')
    fp=path
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    # fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    my_str=str
    my_str=re.sub("\n", "" , my_str)
    my_str=re.sub("REFERENCES|References.*","",my_str)
    my_str=re.sub("\uf020","",my_str)
    my_str=re.sub("\uf0b7","",my_str)
    my_str=re.sub("\x0c","",my_str)
    my_str=re.sub(r"\AFig \d*","",my_str)
    my_str=re.sub("DOI: \s*","",my_str)
    my_str=re.sub(r'^.*?ABSTRACT', 'ABSTRACT', my_str)
    stopwords1 = set(stopwords.words("english"))
    words = word_tokenize(my_str)
    freqTable = dict()
    for word in words:
        word = word.lower ()
        if word in stopwords1:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    sentences = sent_tokenize(my_str)
    sentenceValue = dict()
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq
    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[ sentence]
    # Average value of a sentence from the original text
    average = int (sumValues / len(sentenceValue))
    summary=''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[ sentence] > (1.2 * average)) :
            summary+= " "+sentence
    return summary