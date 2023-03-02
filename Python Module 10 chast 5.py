# Курс: «Введение в язык
# программирования Python
# Модуль 10. Объектно-ориентированное программирование
# Тема: Перегрузка операторов. Часть 5

# Задание 1
# Создайте класс Circle (окружность).
# Для данного класса реализуйте ряд перегруженных операторов:
# Проверка на равенство радиусов двух окружностей (операция = =);
# Сравнения длин двух окружностей (операции >, <,<= ,>=);
# Пропорциональное изменение размеров окружности,
# путем изменения ее радиуса (операции + - += -=).

# class circle:

# 	def __init__(self, radius):
# 		self.radius = radius

# 	def __str__(self):
# 		return f'{self.radius}'

# 	def __int__(self):
# 		return self.radius

# 	def __add__(self, sum: int):
# 		return circle(self.radius + sum)

# 	def circ_len(self):
# 		return self.radius + 3

# 	def __eq__(self, other):
# 		return other.radius == self.radius

# 	def __lt__(self, other):
# 		return other.radius < self.radius

# 	def __le__(self, other):
# 		return other.radius <= self.radius

# circle = circle()
# circle2 = circle()
# c = circle + 3
# c2 = circle2 + 3
# print(circle2.circle_len())
# print(circle + 3)
# print(circle.circ_len())
# print(circle2 + 3)
# print(circle == circle2)
# print(circle < circle2)
# print(circle <= circle2)
# print(circle == circle2)
# print(circle2 > circle)


# Задание 2
# Создайте класс Complex (комплексное число).
# Более подробно ознакомиться с комплексными числами можно по ссылке.
# Создайте перегруженные операторы для реализации арифметических операций для по работе с комплексными числами
# (операции +, -, *, /).

# class Complex:
# 	def __init__(self, Complexx):
# 		self.Complexx = Complexx

# 	def __str__(self):
# 		return f'{self.Complexx}'

# 	def __add__(self, other):
# 		return self.Complexx + other.Complexx

# 	def __sub__(self, other):
# 		return self.Complexx - other.Complexx

# 	def __mul__(self, other):
# 		return self.Complexx * other.Complexx

# 	def __truediv__(self, other):
# 		return self.Complexx / other.Complexx

# 	def __eq__(self, other):
# 		return self.Complexx == other.Complexx

# a1 = Complexx(2)
# a2 = Complexx(2)
# c1 = Complexx(a1)
# c2 = Complexx(a2)
# print(c1, c2)
# print(c1 + c2)
# print(c1 - c2)
# print(c1 * c2)
# print(c1 / c2)
# print(c1 == c2)

# Задание 3
# Вам необходимо создать класс Airplane (самолет).
# С помощью перегрузки операторов реализовать:
# Проверка на равенство типов самолетов (операция = =);
# Увеличение и уменьшение пассажиров в салоне самолета (операции +  - +=  -=);
# Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции ><  <=  >=)

# class Airplane:

# 	def __init__(self, passenger):
# 		self.passenger = passenger

# 	def __str__(self):
# 		return f'{self.passenger}'

# 	def __add__(self, num: int):
# 		return self.passenger + num

# 	def __sub__(self, num: int):
# 		return self.passenger - num

# 	def __lt__(self, other):
# 		return self.passenger <= other.passenger

# 	def __ge__(self, other):
# 		return self.passenger >= other.passenger

# 	def __eq__(self, other):
# 		return self.passenger == other.passenger

# airplane1 = Airplane()
# airplane2 = Airplane()
# print(airplane1 + 2)
# print(airplane1 - 2)
# print(airplane2 + 4)
# print(airplane2 - 4)
# print(airplane1 < airplane2)
# print(airplane1 > airplane2)
# print(airplane1 >= airplane2)
# print(airplane1 <= airplane2)
# print(airplane1 == airplane2)

# Задание 4
# Создать класс Flat (квартира). Реализовать перегруженные операторы:
# Проверка на равенство площадей квартир (операция ==);
# Проверка на неравенство площадей квартир (операция !=);
# Сравнение двух квартир по цене (операции >  <  <= >=).

# class Flat:
# 	def __init__(self, area, price):
# 		area = self.area
# 		price = self.price

# 	def __eq__(self, other):
# 		return self.area == other.area

# 	def __ne__(self, other):
# 		return self.area != other.area

# 	def __lt__(self, other):
# 		return self.price < other.price

# 	def __ge__(self, other):
# 		return self.price >= other.price

# flat1 = Flat()
# flat2 = Flat()
# print(flat1 == flat2)
# print(flat1 != flat2)
# print(flat1 => flat2)
# print(flat1 <= flat2)
