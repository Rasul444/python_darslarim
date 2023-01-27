#                                           # klakk va obyeakt davomi

# class Talaba:
#     def __init__(self,ism,familiya,yil):
#         self.ism = ism
#         self.familiya = familiya
#         self.yil = yil
#         self.bosqich = 1

    
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi"
    
#     def set_bosqich(self,yangi_bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = yangi_bosqich

#     def update_bosqich(self):
#          """Talabanining bosqichini 1taga ko'paytirish"""
#          self.bosqich += 1

#     def get_name(self):
#         return self.ism
    
#     def get_lastname(self):
#         return self.familiya
    
#     def get_age(self,yil):
#         return yil - self.yil

# class Fan():
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
    
#     def add_student(self,talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
#     def get_name(self):
#         """Fan nomi"""
#         return self.nomi
    
#     def get_students(self):
#         """Fanga yozilgan talabalar haqida ma'lumot"""
#         return [x.get_info() for x in self.talabalar]
    
#     def get_students_num(self):
#         """Fanga yozilgan talabalar soni"""
#         return self.talabalar_soni
    
# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]

# print(see_methods(Talaba))

# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_info())

# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())

# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())

# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())












