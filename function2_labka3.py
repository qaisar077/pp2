
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#1
# def func(n:dict):
#     for i in n:
#         if i["imdb"]>5.5:
#             print("True")
# func(movies)

 #2

# def filter(movies_list):
#     result = [movie["name"] for movie in movies_list if movie["imdb"] > 5.5]
#     return result
# print(filter(movies))

#3

# def category(s: str):
#     result = [movie["name"] for movie in movies if movie["category"] == s]
#     return result

# n = input("Введите категорию фильма: ")
# print(category(n))


#4

# def avr(movies: list):
#     total = 0
#     count = 0

#     for movie in movies:
#         total += movie["imdb"]
#         count += 1

#     return total / count if count > 0 else 0  

# print(avr(movies))  


#5

# def category_avr_imdb(s: str):
#     total = 0
#     count = 0

#     for i in movies:  
#         if i["category"] == s:
#             total += i["imdb"]
#             count += 1 
#     return total / count if count > 0 else 0  
# n = input("Введите категорию: ")
# print(category_avr_imdb(n))


