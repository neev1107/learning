# number=int(input())
# last_digit=number%10
# print("Last digit is",last_digit)
# if number%2==0:
#     print("Last digit is even")
# else:
#     print("last digit is odd")
# if number>500:
#     print("Number is greater than 500")
# else:
#     print("Number is not greater than 500")
    
# #Students marks
# marks=int(input("Enter your marks: "))
# attendance=float(input("enter your attendence percentage: "))
# if marks>=40 and attendance>=75:
#     print("Pass")
# else:
#     print("fail")

# #Electricity bill
# units=float(input("Enter your units consumed: "))
# bill=0
# if 0<=units<=100:
#     bill=units*s
# elif 101<=units<=200:
#     bill=units*7
# else:
#     bill=units*10
# print("Bill: ",bill)

# age=int(input("Enter your age: "))
# if age>=18:
#     entrance_Exam=input("Passed or not passed the exam?: ")
#     if entrance_Exam=="Passed":
#         Documents=input("verified or not verified?: ")
#         if Documents=="verified":
#             print("You are eligible for admission")
#     elif entrance_Exam=="not passed":
#             print("Entrance exam not cleared")
#     else:
#         print("Documents not verified")
# else:
#     print("Too young!")

#Practice continues
# val1=(1,2,3)
# list=[12,24,94,94]
# list.append(4)
# print(list)
# list.extend([4,9])
# print(list)
# list.sort()
# print(list)
# print(val1)
# runners = ["Alice", "Bob", "Charlie", "David"]

# # Instantly grab the last item
# print("The winner is " + runners[-1])
'''import random
print("="*40)
print("Welcome to number guessing game")
print("="*40)
number=random.randint(1,100)
print("I am thinking  a number between 1-100")
attempts=0
while True:
    guess=int(input("Enter your guess: "))
    attempts+=1
    if guess>number:
        print("Too high! Think a lower number")
    elif guess<number:
        print("Too low! Think a lower number")
    else:
        print(f"Congratulations!!!! You won in {attempts} chances")
        break'''
        
'''largest = None
while True:
    num = int(input())
    if num <= 0:
        break
    if largest is None or num > largest:
        largest = num
print(largest if largest is not None else "No numbers entered")'''

# n=int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
'''Question 1 '''
'''n=int(input())
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(i,end="")
    print()'''

'''Question 2'''
'''suffix=str(input())
prefix=str(input())
if suffix.startswith(prefix):
    print("yes")
else:
    print("No")'''
    
'''Question 3'''
'''num_str = input
num_digits = len(num_str)
total_sum = 0
for digit in num_str:
    total_sum += int(digit) ** num_digits
if total_sum == int(num_str):
    print("Armstrong")
else:
    print("Not Armstrong")'''
    
'''Question 4 '''
'''N=int(input())
integer=list(map(int,input().split()))
for number in integer:'''
    
# n=int(input())
# for i in range(1,n+1):
#     print(i**3,end=" ") 

'''if "a"=="A":
    print("True")
else
    print("False")'''
    
'''THIRD BELT OF PYTHON PRACTICE STARTS HERE'''# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

'''odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)'''

'''word = input()
vowels="AEIOU"
word = word.upper()
for letter in word:
    if letter.isalpha():
        if letter in vowels:
            continue
        else:
            print(letter)'''
'''n = input()
print(n[::-1])'''
            
'''import math
n=int(input)
print(math.factorial(n))'''
'''a = int(input()) 
b = int(input())
result = a ^ (~b)
print(result)'''
'''print(bin(int(input())))''' 
'''from collections import Counter   
a = "silent"
b = "netsil"
print("yes" if sorted(a)==sorted(b) else "No")
print("yes" if Counter(a)==Counter(b) else "NO")
print(Counter(a))
print(Counter(b))'''
'''ch = "b"
print(ord(ch))
s1 = "listen"
s2 = "silent"

if len(s1) != len(s2):
    print("No")
else:
    freq = [0] * 26
    for i in range(len(s1)):
        freq[ord(s1[i]) - 97] += 1
        freq[ord(s2[i]) - 97] -= 1
    print("Yes" if all(x == 0 for x in freq) else "No")'''
'''s1 = input()
s2 = input()
if len(s1)!=len(s2):
    print("No")
else:
    freq =[0] * 26
    for i in range(len(s1)):
        print(i)'''
'''print(5<<2)'''
# Python code for the above approach

'''num1 = 1024

bt1 = bin(num1)[2:].zfill(32)
print(bt1)

num2 = num1 << 1
bt2 = bin(num2)[2:].zfill(32)
print(bt2)

num3 = num1 << 2
bitset13 = bin(num3)[2:].zfill(16)
print(bitset13)'''

'''num1 = 1024
bt1 = bin(num1)[2:].zfill(32)
print(bt1) 
num2 = num1 << 1
bt2 = bin(num2)[2:].zfill(32)
print(bt2)
num3 = num1 << 2
bt3 = bin(num3)[2:].zfill(32)
print(bt3)'''
#Checking if a bit is set
'''def is_bit_Set(num,pos):
    return (num & (1<<pos)) !=0
num = int(input())
pos = int(input())
print(is_bit_Set(num,pos))'''
#setting a bit
'''def set_bit(num,pos):
    return (num | (1<<pos)) 
num  = int(input())
pos = int(input())
print(set_bit(num,pos))'''
#Clearing a bit
'''def clear_bit(num,pos):
    return (num & ~(1<<pos))
num = int(input())
pos = int(input())
print(clear_bit(num,pos))'''

#Toggling a bit
'''def toggle_bit(num,pos):
    return(num^(1<<pos))
num = int(input())
pos = int(input())
print(toggle_bit(num,pos))'''

#Counting Set Bit
'''def count_set_bit(num):
    count= 0
    while num:
        count += num & 1
        num>>=1
    return count
num = int(input())
print(count_set_bit(num))'''

   
'''nums = [10,20,30,40,50]
largest_num = nums[0]
smallest_num = nums[0]
for number in nums:
    if number > largest_num:
        largest_num = number
    elif smallest_num > number:
        smallest_num = number
range = largest_num - smallest_num
print(range)'''

'''nums = [10,20,30,40,50]
for number in nums:
    a= max(nums)
    b= min(nums)
range = a-b
print(range)'''

# Function to check whether any pair exists
# whose sum is equal to the given target value
'''def two_sum(arr, target):
    n = len(arr)

    # Iterate through each element in the array
    for i in range(n):
      
        # For each element arr[i], check every
        # other element arr[j] that comes after it
        for j in range(i + 1, n):
          
            # Check if the sum of the current pair
            # equals the target
            if arr[i] + arr[j] == target:
                return True
              
    # If no pair is found after checking
    # all possibilities
    return False'''

'''arr = list(map(int,input().split()))
target = int(input())

# Call the two_sum function and print the result
if two_sum(arr, target):
    print("true")
else:
    print("false")
    
n= int(input())
for i in range(n):
    for j in range(i+1,n):
        print(j,end=" ")
    print()'''
'''def is_palindrome(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1

    return True


# --- Running Test Cases ---

# Test 1: Palindrome list
numbers1 = list(map(int,input().split()))
print(f"{is_palindrome(numbers1)}")'''

#Two Sum Problem
'''nums = list(map(int,input().split()))
target = int(input())
def two_sum(nums,target):
    left = 0
    right = len(nums) -1
    while left < right:
       current = nums[left] + nums[right]
       if current == target:
            return [left,right]
       elif current > target:
            right-=1
       else:
            left+=1  
    return[] 
two_sum(nums,target)'''


'''def remove_duplicate(arr):
    if not arr:
        return 0
    slow = 0
    for fast in range(1,len(arr)):
        if arr[fast]!=arr[slow]:
            slow +=1
            arr[slow] = arr[fast]
    return slow + 1

arr = list(map(int,input().split()))
length = remove_duplicate(arr)
print(*arr[:length])'''

'''arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
result = []
i = 0
j = 0
while i < len(arr1) and j <= len(arr2):
    if arr1[i] <= arr2[j]:
        result.append(arr1[i])
        i+=1
    else:
        result.append(arr2[j])
        j +=1
while i < len(arr1):
        result.append(arr1[i])
        i += 1

while j < len(arr2):
        result.append(arr2[j])
        j += 1
print(result)'''


'''arr = list(map(int,input().split()))
target = input()
def reversed_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left +=1
        right -=1
    return arr
print(*reversed_array(arr))'''

'''times = [int(input()) for _ in range(6)]
late_entry = int(input())
print(f"Recorded times: {times}")
times.sort()
print(f"Sorted: {times}")
print(f"Podium: {times[:3]}")
print(f"fastest: {times[0]}, Slowest: {times[-1]}")
removed = times.pop(0)
print(f"Disqualified: {removed}")
times.append(late_entry)
print(f"Updated: {times}")
total = sum(times)
print(f"total: {total}")
average = total / len(times)
print(f"Average is : {average:.2f}")'''


'''def reverse(arr,start,end):
    while start < end:
        arr[start],arr[end]=arr[end],arr[start]
        start +=1
        end -=1
    return arr
n, d = map(int,input().split())
arr = list(map(int,input().split()))
d = d % n
reverse(arr,0,d-1)
reverse(arr,d,n-1)
reverse(arr,0,n-1)
print(*arr)'''

'''def reversed_arr(arr):
    left = 0
    right = len(arr) -1
    while left < right:
        arr[left],arr[right]=arr[right],arr[left]
        left +=1
        right -=1
    return arr
arr = list(map(int,input().split()))
length = int(input())
print(*reversed_arr(arr))'''
'''[1,2,3,3,4,4,5]'''
'''[1,2,3,4,5]'''
'''def remove_duplicate(arr):
    slow = 0

    for fast in range(1, len(arr)):
        if arr[slow] != arr[fast]:
            slow += 1
            arr[slow] = arr[fast]

    return arr[:slow + 1]
        
n=int(input())
arr=list(map(int,input().split()))
print(*remove_duplicate(arr))'''

'''def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1'''

