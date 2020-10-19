import pyttsx3
import PyPDF2
book = open('pdf_name.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
bot = pyttsx3.init()
for num in range(0, pages):
    page = pdfReader.getPage(0)
    text = page.extractText()
    bot.say(text)
    bot.runAndWait()
