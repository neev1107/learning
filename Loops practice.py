# def main():
#     number=get_number()
#     meow(number)
    
# def get_number():
#     while True:
#         n=int(input("Enter a number: "))
#         if n>0:
#             return n

# def meow(n):
#     for i in range(n):
#         print("meow")
        
# main()
        
# #number divisible by 5       
# n=int(input())
# arr=map(int,input().split())
# divisible_by_5=[n for n in arr if n%5==0]
# if divisible_by_5:
#     print(*divisible_by_5)
    

# N_string = input()
# digit_sum = 0
# for digit in N_string:
#     digit_sum += int(digit)
# print(digit_sum)

# num=int(input())
# for i in range(1,num+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
    
    
# Step 1: Get the maximum number of stars from the user
'''n = int(input("Enter a number: "))'''

# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end=" ")
#     print()
    
# for i in range(n-1,0,-1):
#     for j in range(i):
#         print(i,end=" ")
#     print()

'''for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
for i in range(n,0,-1):
    for j in range(1,i):
        print(j,end=" ")
    print()
    
n=int(input("Enter a number: "))

for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()
    
for i in range(n-1,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()'''
    
'''n=int(input("Enter: "))
ch=65'''

'''for i in range(1,n+1):
    print(f'{chr(ch)} '*i)
    ch+=1
print()'''


'''for i in range(n-1,0,-1):
    print(f'{chr(ch)} '*i)
    ch+=1
print()'''
'''n=int(input())
ch=65 
for i in range(1,n+1):
    for j in range(i):
        print(chr(ch),end=" ")
    ch+=1
    print()
    
for i in range(n-1,0,-1):
    print(chr(ch+i),end=" ")'''
    
# Step 1: Get user input
'''n = int(input("Enter a number: "))'''

# Step 2: Upper part (Increasing)
'''for i in range(1, n + 1):
    # Convert row number to its corresponding letter ('A' starts at 65)
    letter = chr(64 + i) 

    for j in range(i):
        print(letter, end=" ")
    print()

# Step 3: Lower part (Decreasing)
for i in range(n - 1, 0, -1):
    # Convert row number to its corresponding letter
    letter = chr(64 + i)
    
    for j in range(i):
        print(letter, end=" ")
    print()'''
    
# n=int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

'''total=0
count=0
while True:
    num=int(input())
    if num==-1:
        break
    else:
        total+=num
        count+=1
    
print(f"Sum: {total} Count: {count}")'''

# n=int(input())
# arr=list(map(int,input().split()))
# for number in arr:
#     if number>0:
#         print(number,end=" ")
#     elif number==0:
#         break
#     else:
#         continue

'''s= input()
vowels="aeiouAEIOU"
consonants=0
vowel=0
for letter in s:
    if letter.isalpha():
        if letter in vowels:
            vowel+=1
        else:
            consonants+=1
        
print(f"vowels: {vowel} Consonants: {consonants}")'''

'''n=int(input())
if n>=10:
    b=n/10
    c=int(b)
    print(c%10)
else:
    print("Invalid number")'''
    
'''n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''
    

# number_list=[]   
# while True:
#     n=int(input())
#     number_list.append(n)
#     if n<=0:
#         break

# print("Largest number:", max(number_list))
    
'''n=input()
arr=list(map(str,input().split()))
x=0
for letter in arr:
    if letter== "++X" or letter== "X++" in arr:
        x+=1
    elif letter=="--X" or letter=="X--" in arr:
        x-=1
    
print(x)'''

'''def main():
    n= int(input())
    arr = list(map(int, input().split()))

def print_array(arr):
    for number in arr:
        if number==-1:
            break  
        
main()
print_array()'''
#arr=[]
'''while True:
    n=int(input("Enter a number(-1 to stop): "))
    if n == -1:
        break
    else:
        arr.append(n)
print(arr)'''
    
'''s=input()
count=0
for letter in s:
    if " " in s:
        count+=1
print(count)'''
    
'''a="Hi I am Neev"
b=a.split()
print(len(b))'''

'''n=int(input())
result=1
for i in range(1,n+1):
    result*=i
print(result)'''


'''n=int(input())
count=0
for i in range(1,n+1):
    for j in range(1,i+1): 
        count+=1
        print(count,end=" ")
    print()'''
    
'''n=int(input())
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(i,end=" ")
    print()'''
    
'''n=int(input())
arr=list(map(int,input().split()))'''
         
'''n=int(input())
budget=list(map(int,input().split()))
spent=list(map(int,input().split()))
count = 0
for i in range(n):
    if spent[i] > budget[i]:
        count+=1
print(count)'''

'''print("Welcome to CodeRail Railway Booking System")
name=(input("Enter your name: "))
age=int(input("Enter your age: "))
print("Choose travel class: ")
print("1. First class -  ₹1500")
print("2. Second class -  ₹1000")
print("3. Sleeper class -  ₹500")
Class=int(input("Enter choice(1/2/3): "))
meal=input("Do you want to add a meal? (yes/no): ")
First_class=1500
Second_class=1000
Third_class=500
meal=200
total=0
while True:
    if Class==1 and meal=="yes":
        total+=First_class+meal  
    elif Class==2 and meal=="yes":
        total+=Second_class+meal
    elif Class==3 and meal=="yes":
        total+=Third_class+meal
    elif age>=5:
        total==0
    elif age>65 and Class==1 and meal=="yes":
        total+=1200+200
    elif age>65 and Class==2 and meal=="yes":
        total=Second_class-200+200
    elif age>65 and Class==3 and meal=="yes":
        total+=Third_class-100+200
    break
print(total)'''

'''Question 1'''
'''n=int(input())
arr=list(map(int,input().split()))
N=int(input())
x_part=arr[:N]
y_part=arr[N:n+1]
print(x_part)
print(y_part)
result=[]
for i in range(N):
    result.append(x_part[i])
    result.append(y_part[i])
print(result)'''

'''Question 2'''
'''employees=int(input())
hours=list(map(int,input().split()))
target_hours=int(input())
count=0
for i in hours:
    if i>=target_hours:
        count+=1
    else:
        continue
print(count)
print'''

emails = {"a@x", "b@x", "a@x", "c@x", "b@x"}
unique=set(emails)
print(unique)
print(len(unique))

allowed = {"admin", "editor", "viewer"}
print("editor" in allowed)
print("guest" in allowed)
tags= {"python","code"}
tags.add("lists")
tags.add("python")
print(tags)
tags.discard("code")
tags.remove("lists")
print(tags)
coding={"Ana", "Ravi", "Sam"}
music = {"Sam","Meera", "Kabir"}
print(coding | music)
print(coding & music)
print(coding - music)
print(coding ^ music)

coding = {"Ana", "Ravi", "Sam","Priya"}
music = {"Sam", "Meera", "Kabir"}
all_students = {"Ana", "Ravi", "Sam", "Meera", "Kabir", "Zoya", "Priya"}
chess = {"Priya", "Zoya"}
print(coding.issubset(all_students))
print(coding.isdisjoint(chess))
import requests
print("Requests is installed")
print(requests.__version__) 
import flask    