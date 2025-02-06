# # #1
# class String:
#     def __init__(self):
#         self.string = ""
#     def getString(self):
#         self.string = input("Введите строку: ")
#     def printString(self):
#         print(self.string.upper())
# string = String()
# string.getString()  
# string.printString()  



# # #2
# # class Shape:
# #     def __init__(self, length):
# #         self.length = length
# # class Square(Shape):
# #     def __init__(self, length):
# #         super().__init__(length)  
# #     def area(self): 
# #         return self.length * self.length
# # n = Square(9)
# # print(n.area())  

    
# # #3
# # class Shape:
# #     def __init__(self, length):
# #         self.length = length

# # class Square(Shape):
# #     def __init__(self, length):
# #         super().__init__(length)  
# #     def area(self):  
# #         return self.length ** 2  
# # n = Square(3)
# # print(n.area())  

# # # #5
# # class Shape:
# #     def __init__(self, length):
# #         self.length = length  
# # class Rectangle(Shape):
# #     def __init__(self, length, width):
# #         super().__init__(length)
# #         self.width = width  
# #     def area(self): 
# #         return self.length * self.width
# # n = Rectangle(2, 5)
# # print(n.area()) 

# # #6
# from math import sqrt
# class Point():
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def show(self):
#         return self.x, self.y
#     def move(self,a,b):
#         return self.x+a,self.y+b
#     def dist(self,x1,y1):
#         return sqrt((x1-self.x)**2+(y1-self.y)**2)

# n=Point(3,4)
# print(n.show())

# print(n.move(1,2))

# print(n.dist(6,7))

# (3, 4)
# (4, 6)
# 4.242640687119285



# class Account:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.balance=balance


#     def deposit(self,deposits):
#         return deposits
#     def withdraw(self,withdraws):
#         if withdraws>self.balance:
#             return False
#         else:
#             return f"You recieved {withdraws} amount of money"
        
# customer=Account('Qaisar',10000)
# print(customer.deposit(2000))
# print(customer.withdraw(70000))

# # 2000
# # False