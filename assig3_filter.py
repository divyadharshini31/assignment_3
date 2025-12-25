#extract all even numbers from a list
lst=[1,2,3,4,5,6,8]
even_num=filter(lambda x: (x%2==0), lst)
print(list(even_num))
#op: [2,4,6,8]

#select all words from a list that start with a vowel
e=["apple","eagle","donkey","icecream","mango","owl"]
vowel=filter(lambda x: (x[0] in 'aeiou'), e)
print(list(vowel))
#op: ['apple', 'eagle', 'icecream', 'owl']

#use filter() to remove all negative numbers
num=[1,-3,56,-70,-90,0]
neg=filter(lambda x: x>=0, num)
print(list(neg))
#op: [1,56,0]

#find numbers greater than 50 from a list
n=[12,45,57,908,3,50]
lst=filter(lambda x: x>50, n)
print(list(lst))
#op:[57,908]

#extract all palindromic strings from a list.
string=["buffalo","malayalam","apple","civic","level","cricket"]
palindrome=filter(lambda x: x==x[::-1],string)
print(list(palindrome))
#op=['malayalam', 'civic', 'level']