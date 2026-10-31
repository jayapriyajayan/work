# 1.highest mark kittiya ale print cheyan
students={
    "Anu":85,
    "Meera":92,
    "Riya":78,
    "Amal":95
}

highestmark=students["Anu"]
for i in students.values():
    if i>highestmark:
        highestmark=i
print("high",highestmark) 

#2.smallest mark

students={
    "Anu":85,
    "Meera":92,
    "Riya":78,
    "Amal":95
}

smallestmark=students["Riya"]
for i in students.values():
    if i<smallestmark:
        smallestmark=i
print("small",smallestmark)        

#3.frequency

text="calculation"
frequency={}
for i in text:
    frequency[i]=frequency.get(i,0)+1
print(frequency)    


#4.sum of numbers
numbers=(12,34,65,3,44)
total=0
for i in numbers:
    total+=i
print(total) 

#5.even numbers
numbers=[1,3,2,4,5,6]
result={"even":[]}
for i in numbers:
    if i%2==0:
     result ["even"].append(i)
print(result)   

#6.largest number
numbers=[12,43,56,78,22,44,55,]
largest=numbers[0]
sec_larg=numbers[0]
for i in numbers:
    if i >largest:
        sec_larg=largest
        largest=i
    elif i> sec_larg and i != largest:
        sec_larg=i
print(sec_larg)            

#7.sammlest number
numbers=[22,34,55,42]
smallest=numbers[0]
for i in numbers:
    if i < smallest:
        smallest=i
print(smallest)

#8.dulipcate element 

numbers = [12,23,45,35,7,7,89,23]

num=[]
for i in numbers:
    if numbers.count(i)==1:
        num.append(i)
print(num)  

#9. oro wordite count kandu pidikan
string1="my name is jayapriya"

new = string1.split()
print(new)
for i in new:
    print(len(i))

#10.how many times a number in list

numbers=(1,2,2,3,4,4,5,6,7,3)
count=0
for i in numbers:
    if i==2:
        count+=1
print(count) 