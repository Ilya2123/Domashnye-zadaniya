# Курс: «Введение в язык
# программирования Python

# Модуль 10. Объектно-ориентированное
# программирование
# Тема: Классы. Объекты. Часть 1

# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска,
# производителя, объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных,
# реализуйте доступ к отдельным полям через методы класса.

# class Car:
# 	model_name = 'Lexus'
# 	year_of_issue = 2009
# 	manufacturer = 'Japan'
# 	engine_capacity = 3500
# 	car_color = 'Black'
# 	price = 15000
#  def change_model(self, new_model):
# 		self.model_name = new_model

#  def show_new_model(self):
# 		return 'Do you want this model? ' + self.model_name

#  def change_color(self, new_color):
# 		self.car_color = new_color

#  def show_new_color(self):
# 		return 'Do you want this color? ' + self.car_color

#  def lux_model(self, new_price):
# 		self.price = new_price
# 		print('Do you want a business model?')

#  def change_price(self):
# 		return 'New price business model: ' + str(self.price)

# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

# class Book:
# 	name_book = 'My life'
# 	year_publishing = '1933'
# 	genre = 'Detective'
# 	author = 'Georgi Monovets'
# 	price = 90

# 	def new_name_book(self, new_name):
# 		self.name_book = new_name

# 	def my_book(self):
# 		print('Buy book')

# 	def information(self, x):
# 		if x == 1:
# 			print(f'Autor name: ' + self.author)
# 		if x == 2:
# 			print(f'Genre book: ' + self.genre)
# 		if x == 3:
# 			print(f'Year piblishing:' + self.year_publishing)

# 	def price_book(self, a):
# 		print(f'Price {a} books?:', int(self.price) * a, 'uah')

# library = Book()
# library.new_name_book(input('Enter new name book: '))  # Asus
# print(f'Here is your book: ' + library.change_name_book())
# library.price_book(int(input('How many books do you need: ')))
# library.my_book()
# library.information(int(input('What information is needed 1-autor, 2-genre, 3-year_publishing : ')))

# Задание 3

# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к
# отдельным полям через методы класса

# class Stadium:
#  stadium_name = 'Dinamo'
#  opening_date = '1989'
#  country = 'Ukraine'
#  city = 'Kiev'
#  capacity = '7000'
#
#  def new_name(self, new_name):
# 		self.stadium_name = new_name
#
#  def change_stadium_name(self):
# 		return self.stadium_name
#
#  def repair_start(self, new_opening_date):
# 		self.opening_date = new_opening_date
# 		print('Repair start date 2014')
#
#  def new_opening_date(self):
# 		return self.opening_date

# newg = Stadium()
# print('Stadium name', games.stadium_name)
# print('Opening date', games.opening_date)
# print('In the country', games.country)
# print('In the town', games.city)
# print('Its capacity', games.capacity)
# newg.new_name('Tatarbunary')

# print('New name stadium', games.change_stadium_name())
# games.repair_start(2015)
# print('New opening date', games.new_opening_date())

