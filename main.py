from tkinter import *
from tkinter import filedialog
from pdfrw import PdfReader, PdfWriter

#setting the parameters of GUI
root = Tk()
root.title("Изменение заголовка файлов PDF для выгрузки на сайт")
root.iconbitmap("Unibelus_ico.ico")
root.geometry("550x130+600+250")
root.resizable(True, False)

#empty label
Label(root).grid(row = 0, column = 0, columnspan=3)

#Label for messages
message_label = Label(root,padx = 3)
message_label.grid(row = 4, column = 0, columnspan=2, sticky = "n")

#Label and Entry for pdf file path
label_pdf = Label(root, text = "Файл", padx = 3)
label_pdf.grid(row = 1, column = 0)
entry_pdf = Entry(root, width = 50)
entry_pdf.grid(row = 1, column = 1)

#Label and Entry for header
label_header = Label(root, text = "Заголовок", padx = 3)
label_header.grid(row = 2, column = 0)
entry_header = Entry(root, width = 50)
entry_header.grid(row = 2, column = 1)

#changing the header function
def change_header():
    try:
        pdf_file_path = entry_pdf.get()
        trailer = PdfReader(pdf_file_path)
        trailer.Info.Title = str(entry_header.get())
        trailer.Info.Author = ''
        PdfWriter(pdf_file_path, trailer=trailer).write()
        message_label["fg"] = "Green"
        message_label["text"] = "Заголовок изменён"
    except Exception as e:
        message_label["fg"] = "Red"
        message_label["text"] = "Ошибка: "+ str(e)


#browsing pdf file function
def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Выберите файл pdf",
                                          filetypes=(("PDF files",
                                                      "*.pdf*"),
                                                     ("all files",
                                                      "*.*")))
    # Change entry contents
    entry_pdf.delete(0, END)
    entry_pdf.insert(0, filename)


Button(root, text = "Обзор", padx = 4, command = browseFiles).grid(row=1, column=2) #make a pdf button
Button(root, text = "Изменить заголовок файла", padx = 4, command = change_header).grid(row=3, column=2) #make a pdf button


root.mainloop()