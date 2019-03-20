#This is the user class
class User:
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.books = {}
		
	#email associted with the user
	def get_email(self):
		return self.email
		
	#Take new email and changes the email associated with the user
	def change_email(self, address):
		self.email = address
		print("Email has been updated!")
		
	# Printing user information
	def __repr__(self):
		return "User: {user_name}, email: {email}, books read: {no_books}".format(user_name = self.name, email = self.email, no_books = len(self.books))

	#comparison betweein users
	def __eq__(self, other_user):
		if self.name == other_user.name and self.mail == other_user.mail:
			other_user = self.name
		
	def read_book(self, book, rating = None):
		self.book = book
		self.rating = rating
		self.books[book] = rating
		
	#getting average rating	
	def get_average_rating(self):
		total = 0
		rating_samples = []
		for value in self.books.values():
			if value != None:
				rating_samples.append(value)
		for vulue in rating_samples:
			total += value
		return total / len(rating_samples)
		
	
		
#This is a Book class
class Book:

	#Initialzation of Book class
	def __init__(self, title, isbn):
		self.title = title
		self.isbn = isbn
		self.ratings = []
	
	#getting title of the book
	def get_title(self):
	    return self.title
		
	#getting isbn of the book
	def get_isbn(self):
	    return self.isbn
		
	#sitting new isbn 
	def set_isbn(self, new_isbn):
		self.isbn = new_isbn
		print("The ISBN has been changed")
		return self.isbn
		
	#adding the rating for specific book 
	def add_rating(self, rating):
		rating_range = [d/10 for d in range(41)]
		if rating in rating_range or rating == None:
			self.ratings.append(rating)
		else:
		    print("Invalid Rating")
			
	def __eq__(self, other_book):
		if self.title == other_book.title and self.isbn == other_user.isbn:
			other_book = self.title
			
	#calculating the average rating 
	def get_average_rating(self):
		new_ratings = []
		total = 0
		for rating in self.ratings:
			if rating != None:
				new_ratings.append(rating)
		for rating in new_ratings:
			total += rating
		return total / len(new_ratings)
		
	def __hash__(self):
		return hash((self.title, self.isbn))
		
	def __repr__(self):
		return "{title} isbn: {isbn}".format(title = self.title, isbn = self.isbn)
		
		
		
#Fiction Books
class Fiction(Book):
	def __init__(self, title, author, isbn):
		super().__init__(title, isbn)
		self.author = author
		
	def get_author(self):
		return self.author
		
	def __repr__(self):
		return "{title} by {author}".format(title = self.title, author = self.author)
		
		
#Non Fiction Books
class Non_Fiction(Book):
	def __init__(self, title, subject, level, isbn):
		super().__init__(title, isbn)
		self.subject = subject
		self.level  = level
		
	def get_subject(self):
		return self.subject
		
	def get_level(self):
		return self.level
		
	def __repr__(self):
		return "{title}, a {level} maunal on {subject}".format(title = self.title, level = self.level, subject = self.subject)
		

#TomeRater

class TomeRater:
	def __init__(self):
		self.users = {}
		self.books = {}
		
	def create_book(self, title, isbn):
		return Book(title, isbn)
		
	def create_novel(self, title, author, isbn):
		return Fiction(title, author, isbn)
		
	def create_non_fiction(self, title, subject, level, isbn):
		return Non_Fiction(title, subject, level, isbn)
		
	def add_book_to_user(self, book, email, rating = None):
		if email in self.users:
			self.users[email].read_book(book, rating)
			book.add_rating(rating)
			if book in self.books:
				self.books[book] += 1
			else:
				self.books[book] = 1
		else:
			print("No user with this {email}!".format(email = email))
			
	def add_user(self, name, email, user_books = None):
		new_user = User(name, email)
		self.users[new_user.email] = new_user
		if user_books != None:
			for book in user_books:
				self.add_book_to_user(book, email)
	
	
	def print_catalog(self):
		for book in self.books.keys():
			print(book)
		
	def print_users(self):
		for user in self.users:
			print(self.users[user])
		
		
	def most_read_book(self):
		most_read = 0
		m_read_book = ""
		for book in self.books:
			if self.books[book] > most_read:
				most_read = self.books[book]
				m_read_book = book
			else:
				continue
		return m_read_book
		
	def highest_rated_book(self):
		highest_average = 0
		highest_book = ""
		for book in self.books:
			if book.get_average_rating() > highest_average:
				highest_average = book.get_average_rating()
				highest_book = book
			else:
				continue
		return highest_book
		
		
	def most_positive_user(self):
		highest_average = 0
		highest_user = ""
		for user in self.users.values():
			if user.get_average_rating() > highest_average:
				highest_average = user.get_average_rating()
				highest_user = user.name
			else:
				continue
		return highest_user
		
	
		
		
	
		
		
		
		
		
	


	
		


		