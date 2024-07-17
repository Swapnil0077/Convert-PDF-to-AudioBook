# importing the modules
import PyPDF2
import pyttsx3
from tkinter.filedialog import *
from PyPDF2 import PdfReader


book = askopenfilename()

reader = PdfReader(book)
number_of_pages = len(reader.pages)
# page = reader.pages[number_of_pages]
# text = page.extract_text()

for num in range(0, number_of_pages):
    page = reader.pages[num]
    text = page.extract_text()
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()
















# path of the PDF file
# book = askopenfilename()


# # creating a PdfFileReader object
# pdfReader = PyPDF2.PdfReader(book)
#
# # the page with which you want to start
# # this will read the page of 25th page.
# from_page = reader.pages[24]
#
# # extracting the text from the PDF
# text = from_page.extractText()
#
# # reading the text
# speak = pyttsx3.init()
# speak.say(text)
# speak.runAndWait()
