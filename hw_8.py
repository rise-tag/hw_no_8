# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Депозит: {amount} добавлено. Новый баланс: {self.balance}")
#         else:
#             print("Сумма депозита должна быть положительной.")
    
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Недостаточно средств для снятия.")
#         elif amount <= 0:
#             print("Сумма снятия должна быть положительной.")
#         else:
#             self.balance -= amount
#             print(f"Снятие: {amount} снято. Новый баланс: {self.balance}")
#     def get_balance(self):
#         return self.balance
# account1 = BankAccount()
# account2 = BankAccount(500)
# account1.deposit(100)  
# account1.withdraw(50)  
# print(f"Текущий баланс account1: {account1.get_balance()}")  
# account2.deposit(300)  
# account2.withdraw(1000)  
# account2.withdraw(200)  
# print(f"Текущий баланс account2: {account2.get_balance()}") 

# class Course:
#     def __init__(self, name, credits):
#         self.name = name
#         self.credits = credits

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.courses = []

#     def add_course(self, course):
#         if isinstance(course, Course):
#             self.courses.append(course)
#             print(f"Курс {course.name} добавлен студенту {self.name}.")
#         else:
#             print("Можно тольк Course.")

#     def total_credits(self):
#         total = sum(course.credits for course in self.courses)
#         return total

#     def list_courses(self):
#         if self.courses:
#             print(f"Студент {self.name} записан на следующие курсы")
#             for course in self.courses:
#                 print(f"- {course.name} ({course.credits} кредитов)")
#         else:
#             print(f"Студент {self.name} не записан на курсы.")

# course1 = Course("Математика", 2)
# course2 = Course("Информатика", 4)
# course3 = Course("Программирование", 5)

# student1 = Student("Байбол")
# student2 = Student("Султан")

# student1.add_course(course1)
# student1.add_course(course3)
# student2.add_course(course2)
# student2.add_course(course1)
# student2.add_course(course3)
# student1.list_courses()
# print(f"Общее количество кредитов для {student1.name}: {student1.total_credits()}\n")
# student2.list_courses()
# print(f"Общее количество кредитов для {student2.name}: {student2.total_credits()}")

# чо такие сложные задания (

# class Book:
#     def __init__(self, title, author, publication_year):
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year
#     def __str__(self):
#         return f"'{self.title}' by {self.author}, {self.publication_year}"

# class Library:
#     def __init__(self):
#         self.books = []
#     def add_book(self, book):
#         self.books.append(book)
#         print(f"Книга '{book.title}' добавлена в библиотеку.")
#     def find_book_by_title(self, title):
#         for book in self.books:
#             if book.title.lower() == title.lower():
#                 return book
#         return None
#     def display_books(self):
#         if not self.books:
#             print("В библиотеке нет книг.")
#         else:
#             print("Список книг в библиотеке:")
#             for book in self.books:
#                 print(book)

# book1 = Book("Война и мир", "Лев Толстой", 1869)
# book2 = Book("Преступление и наказание", "Фёдор Достоевский", 1866)
# book3 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)

# library = Library()

# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)

# library.display_books()

# search_title = "Война и мир"
# found_book = library.find_book_by_title(search_title)
# if found_book:
#     print(f"Найдена книга: {found_book}")
# else:
#     print(f"Книга с названием '{search_title}' не найдена.")

# import math

# class Shape:
#     def area(self):
#         pass
#     def perimeter(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * (self.radius ** 2)
#     def perimeter(self):
#         return 2 * math.pi * self.radius

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2 * (self.width + self.height)

# circle1 = Circle(5)
# circle2 = Circle(7)
# rectangle1 = Rectangle(4, 6)
# rectangle2 = Rectangle(3, 8)

# print(f"Круг с радиусом {circle1.radius}: площадь = {circle1.area():.2f}, периметр = {circle1.perimeter():.2f}")
# print(f"Круг с радиусом {circle2.radius}: площадь = {circle2.area():.2f}, периметр = {circle2.perimeter():.2f}")
# print(f"Прямоугольник с шириной {rectangle1.width} и высотой {rectangle1.height}: площадь = {rectangle1.area()}, периметр = {rectangle1.perimeter()}")
# print(f"Прямоугольник с шириной {rectangle2.width} и высотой {rectangle2.height}: площадь = {rectangle2.area()}, периметр = {rectangle2.perimeter()}")

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def __str__(self):
#         return f"{self.year} {self.make} {self.model}"

# class Garage:
#     def __init__(self):
#         self.cars = []
#     def add_car(self, car):
#         self.cars.append(car)
#         print(f"Автомобиль {car} добавлен в гараж.")
#     def remove_car(self, make, model):
#         for car in self.cars:
#             if car.make.lower() == make.lower() and car.model.lower() == model.lower():
#                 self.cars.remove(car)
#                 print(f"Автомобиль {car} удалён из гаража.")
#                 return
#         print(f"Автомобиль {make} {model} не найден в гараже.")
#     def display_cars(self):
#         if not self.cars:
#             print("В гараже нет автомобилей.")
#         else:
#             print("Список автомобилей в гараже:")
#             for car in self.cars:
#                 print(car)

# car1 = Car("Toyota", "Camry", 2010)
# car2 = Car("Ford", "Mustang", 2015)
# car3 = Car("Honda", "salarys", 2018)
# car4 = Car("Chevrolet", "Huracane", 1967)

# garage = Garage()
# garage.add_car(car1)
# garage.add_car(car2)
# garage.add_car(car3)
# garage.add_car(car4)
# garage.display_cars()
# garage.remove_car("Ford", "Mustang")
# garage.display_cars()
