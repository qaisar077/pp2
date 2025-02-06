#1
def covert_to_ounces(n:float):
    result=n*28.3495231
    return result
grams=float(input())

print(covert_to_ounces(grams))

# 2


# "Fahrenheit temperature"

# def centigrade(n):
#     result=(5/9)*(n-32)
#     return result

# fahrenheit=int(input())
# print(centigrade(fahrenheit))

#3
# "classic puzzle"

# def solve(numheads, numlegs):
#     for i in range(1,numheads):
#         if i*4+(numheads-i)*2==numlegs:
#             return i, numheads-i



# numheads=int(input())
# numlegs=int(input())
# print(solve(numheads,numlegs))

# 4


# "Prime"

# def lter_prime (list1:list):
#     prime_numbers=[]
#     for i in list1:
#         cnt=0
#         for j in range(2,i):
#             if i%j==0:
#                 cnt+=1
#         if cnt==0:
#             prime_numbers.append(i)
#     return prime_numbers

# numbers=[1,2,3,4,5,6,7,8,9,10,11,12,14,1,4,2,2123,432,12,41,32,4234,23]
# print(lter_prime(numbers))

# 5

# "permutations"

# from itertools import permutations
# def permutatio(s:str):
#     result=[''.join(p) for p in permutations(s)]
#     return result

# string =str(input())
# print(permutatio(string))


# 6
# "reversed sentences"

# def reversed_sentences(s:str):
#     for i in range(len(s)-1,-1,-1):
#         print(s[i])



# reversed_sentences("1 2 3 ")

 

# 7

# "a 3 next to a 3"

# def has_33(nums):
#     for i in range(len(nums)-1):
#         if nums[i]==3:
#             if nums[i-1]==3 or nums[i+1]==3:
#                 return True
#     return False

# print(has_33([1, 3, 1, 3]))

# 8
# "007 in order"

# def spy_game(nums:list):
#     result=[]
#     for i in nums:
#         if i==0 or i==7:
#             result.append(i)
#     if result[0]==0 and result[1]==0 and result[2]==7:
#         return True
#     else:
#         return False
    
# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))

# 9

# "Volume a sphere"

# def volume_sphere(r:int):
#     volume=(4/3)*3.14*(r**3)
#     return volume

# volume_sphere(5)



# 10
# "unique elements"

# def unique_elem(list1:list):
#     result=[]
#     for i in list1:
#         if i not in result:
#             result.append(i)
#     return result

# unique_elem([1,2,3,2,1,2,32,1])



# 11
# "polindrom"

# def is_polindrom(s:str):
#     result=''
#     for i in range(len(s)-1,-1,-1):
#         result+=s[i]
        

#     if s==result:
#         return True
#     else:
#         return False
    
    
# 12



# def histogram(n):
#     for i in n:
#         for j in range(0,i):
#             print('*',end=' ')
#         print("\n")

# histogram([4,5,9])



# from random import randint
# print("Hello! What is your name?")
# name=input()
# print(f"Well, {name}, I am thinking of a number between 1 and 20.")
# guess=int(input())
# n=randint(1,20)
# attempts=0
# while True:
#     attempts+=1
#     if guess>n:
#         print("Your guess is too high")
#     elif guess<n:
#         print("Your guess is too low.")
#     else:
#         print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
#         break
#     guess=int(input())
