import os

class Library:
	books = []
	file = open("books.txt", "r")
	for line in file:
		books.append(line)	
	no_of_books = len(books)
	def clearBooks(self):
		file = open("books.txt", "r")
		text = file.read()
		if not text:
			print("There are no books to clear.")
			return
		file = open("books.txt", "w")
		print("Books cleared from library.")
	def delBook(self, book):
		with open("books.txt", "r") as file:
			readf = file.readlines()
		file = open("books.txt", "w")
		if book in self.books:
			self.books.remove(book)
			print(f"Deleted '{book}' successfully.")
		elif book+"\n" in self.books:
			self.books.remove(book+"\n")
			print(f"Deleted '{book}' successfully.")
		else:
			print(f"No book named '{book}' found to delete.")
		for book in self.books:
			file.write(book)
		'''for line in readf:
			if book in readf:
				readf.replace(book, '')
		#self.books.remove(book)'''
	def addBook(self, book):
		if not book:
			print("Enter valid name.")
			return
		file = open("books.txt", "a")
		self.books.append(book)
		file.write(book)
		file.write("\n")
		print(f"Added '{book}' successfully.")
	def countBooks(self):
		file = open("books.txt", "r")
		lines = 0
		for line in file:
			lines +=1
		if lines == 0:
			print("There are zero books in library.")
		elif lines == 1:
			print("There is only one book in library.")
		else:
			print(f"There are total of {lines} books in library.")
		file.close()
	def allBooks(self):
		with open("books.txt", "r") as file:
			readf = file.readlines()
		if readf:
			print("Books present in library are:")
			for line in readf:
				print(line, end="")
		else:
			print("No books found to list.")

if os.path.exists("books.txt"):
	pass
else:
	file = open("books.txt", "w")
	file.close()

hkl = Library()

print("Welcome to Harry Ki Library!")
print("Type \n'add' to add, \n'remove' to remove,\n'nob' to list number of books, \n'clear' to clear all books immediately\n'list' to list all the books in library, \n'exit' to exit the program.")
while True:
	choice = input("Enter your choice: ")
	choice = choice.lower()
	match choice:
		case 'add':
			nChoice = input("Enter name of the book to add: ")
			hkl.addBook(nChoice)
		case 'remove':
			nChoice = input("Enter name of the book to remove: ")
			hkl.delBook(nChoice)
		case 'nob':
			hkl.countBooks()
		case 'list':
			hkl.allBooks()
		case 'clear':
			hkl.clearBooks()
		case 'exit':
			print("Program exited.")
			exit()
		case _:
			print("Invalid input, enter again.")