import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class LibraryGUI:
    def __init__(self, master):
        # Kütüphane arayüzü oluşturan sınıfın constructor'ı
        self.master = master
        master.title("Library Management System")

        # Library sınıfından bir nesne oluşturuluyor
        self.lib = Library()

        # Arayüzdeki başlık etiketi
        self.label = tk.Label(master, text="*** MENU ***")
        self.label.pack()

        # Kitapları listeleme butonu
        self.list_button = tk.Button(master, text="1) List Books", command=self.list_books)
        self.list_button.pack()

        # Kitap eklemek için buton
        self.add_button = tk.Button(master, text="2) Add Book", command=self.add_book)
        self.add_button.pack()

        # Kitap silmek için buton
        self.remove_button = tk.Button(master, text="3) Remove Book", command=self.remove_book)
        self.remove_button.pack()

        # Programdan çıkış yapmak için buton
        self.exit_button = tk.Button(master, text="4) Exit", command=self.exit_program)
        self.exit_button.pack()

    def list_books(self):
        # Kitapları listeleyen fonksiyon
        messagebox.showinfo("List Books", self.lib.list_books())

    def add_book(self):
        # Kullanıcıdan kitap bilgilerini alarak kitap ekleyen fonksiyon
        title = simpledialog.askstring("Add Book", "Enter the book title:")
        author = simpledialog.askstring("Add Book", "Enter the book author:")
        release_date = simpledialog.askstring("Add Book", "Enter the release date:")
        num_pages = simpledialog.askstring("Add Book", "Enter the number of pages:")

        self.lib.add_book(title, author, release_date, num_pages)
        messagebox.showinfo("Add Book", "Book added successfully!")

    def remove_book(self):
        # Kullanıcıdan kitap adını alarak kitabı silen fonksiyon
        title_to_remove = simpledialog.askstring("Remove Book", "Enter the title of the book to remove:")
        result = self.lib.remove_book(title_to_remove)

        if result:
            messagebox.showinfo("Remove Book", "Book removed successfully!")
        else:
            messagebox.showinfo("Remove Book", "Book not found!")

    def exit_program(self):
        # Çıkış yapmak istenildiğinde kullanıcıya soran ve programı kapatan fonksiyon
        exit_choice = messagebox.askquestion("Exit", "Do you want to exit?")
        if exit_choice == 'yes':
            self.master.destroy()

class Library:
    def __init__(self):
        # Kütüphane dosyasını açan sınıfın constructor'ı
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")

    def __del__(self):
        # Kütüphane dosyasını kapatan sınıfın destructor'ı
        self.file.close()

    def list_books(self):
        # Kitapları dosyadan okuyarak bilgilerini string olarak döndüren fonksiyon
        self.file.seek(0)
        lines = self.file.read().splitlines()
        book_list = [line.split(',') for line in lines]
        book_info = "\n".join([f"Book: {book[0]}, Author: {book[1]}" for book in book_list])
        return book_info

    def add_book(self, title, author, release_date, num_pages):
        # Kitap ekleyen fonksiyon
        book_info = f"{title},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        self.file.flush()

    def remove_book(self, title_to_remove):
        # Kitap silen fonksiyon
        self.file.seek(0)
        lines = self.file.read().splitlines()
        books = [line.split(',') for line in lines]

        for i, book in enumerate(books):
            if book[0] == title_to_remove:
                del books[i]
                break

        self.file.truncate(0)
        self.file.seek(0)

        for book in books:
            self.file.write(','.join(book) + '\n')

        self.file.flush()
        return len(books) != len(books) 
    
if __name__ == "__main__":
    # Tkinter penceresini başlatan ve GUI'yi çalıştıran kısım
    root = tk.Tk()
    gui = LibraryGUI(root)
    root.mainloop()
