#1. count even numbers in a tuple..

a=(1,2,3,4,5,6,7,8)

count=0
for i in a:
    if i %2==0:
        count+=1
print(count)        

#2.frequency

word="numbers"
frequency={}
for i in word:
    frequency[i]=frequency.get(i,0)+1
print(frequency)    


#3.smallest number

numbers=(12,34,56,7)
smallest=numbers[0]
for i in numbers:
    if i< smallest:
        smallest=i
print(smallest)        

#4.sum of numbers
numbers=(10,20,30,40)
total=0
for i in numbers:
    total+=i
print(total)    


#5.count the odd numbers   in a tuple 
numbers=(1,2,3,4,5,6,7)
count=0
for i in numbers:
    if i %2!=0:
        count+=1
print(count)        

#6.count the vowels in a string 

word="education"
count=0
for i in word:
    if i in "aeiou":
        count+=1
print(count)        

#7.how many times a number in list

numbers=(1,2,2,3,4,4,5,6,7,3)
count=0
for i in numbers:
    if i==2:
        count+=1
print(count)    


#8.second largest number

numbers=(10,25,35,46,34,76,99)
largest=numbers[0]
secondlargest=numbers[0]
for i in numbers:
    if i > largest:
        secondlargest=largest
        largest=i
    elif i > secondlargest and i != largest:
        secondlargest=i      
print(secondlargest)                    


#9.even and odd numbers using a dictonary

numbers=[1,2,3,4,5,6]
result={"even":[],"odd":[]}

for i in numbers:
    if i %2==0:
        result["even"].append(i)
    else:
        result["odd"].append(i)
print(result)       

# #10.frequent number in list

numbers=[2,3,1,2,5,5,4,3]
count=0
num=numbers[0]
for i in numbers:
    if numbers.count(i)>count:
        count = numbers.count(i)
        num=i
print(num)        

