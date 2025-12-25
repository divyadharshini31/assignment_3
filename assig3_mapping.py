#list of integers to their squares
lst=[2,67,45,90,78]
res=map(lambda x: x**2, lst)
print(list(res))
#op: [4, 4489, 2025, 8100, 6084]

#all strings in a list to uppercase
l=["how","when","what","where"]
res=map(lambda x: x.upper(),l)
print(list(res))
#op: ['HOW', 'WHEN', 'WHAT', 'WHERE']

#convert celsius to Fahrenheit
temp=[23,45,78,90,56]
fah=map(lambda x: (x*9/5)+32 , temp)
print(list(fah))
#op: [73.4, 113.0, 172.4, 194.0, 132.8] 

#length of each word in a list of strings
string=["cat","dog","elephant",'monkey','dolphin']
length=map(lambda x: len(x), string)
print(list(length))
#[3, 3, 8, 6, 7]

#add 10 to each element 
element=[67,900,786,543,4321]
a=map(lambda x: x+10,element)
print(list(a))
#op: [77, 910, 796, 553, 4331]