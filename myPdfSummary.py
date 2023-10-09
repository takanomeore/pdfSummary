from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import sys
import settings
from io import StringIO

#args = sys.argv

filePath = '/var/www/unj-labo/pdfs/'
openaiKey = settings.openaiKey

def main(argv):
    #args = sys.argv
    if(argv[1] == '1'):
        chatGPTAnswer("",argv[2])
    elif(argv[1] == '2'):
        pdfSummary(argv[2])

def pdfSummary(fileName):
    try:
        fp = open(filePath + fileName+'.pdf','rb')
    except Exception as e:
        print(e)
        sys.exit(0)
    outfp = StringIO()

    rmgr = PDFResourceManager()
    lprms = LAParams()
    device = TextConverter(rmgr,outfp,laparams=lprms)
    iprtr = PDFPageInterpreter(rmgr,device)

    for page in PDFPage.get_pages(fp):
        iprtr.process_page(page)

    text = outfp.getvalue()

    outfp.close()
    device.close()
    fp.close()

    chatGPTAnswer(text, "文章を要約してください")


def chatGPTAnswer(assist, question):
    import openai

    openai.api_key = openaiKey

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = [
                {"role":"assistant", "content":assist},
                {"role":"user", "content":question},
            ],
        )

        print(response['choices'][0]["message"]["content"])
    except Exception as e:
        print(e)

if __name__ == '__main__':
    sys.exit(main(sys.argv))