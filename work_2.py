#1.tuplene dictonary convert

numbers=(10,20,10,30,20,10)

result={}
for i in numbers:
    result[i]=result.get(i,0)+1
print(result)  

# 2.highest mark kittiya ale print cheyan
students={
    "Anu":85,
    "Meera":92,
    "Riya":78,
    "Amal":95
}

# highestmark=0
# for i in students:
#     if highestmark[i]>students:
#         students=highestmark[i]
# print(highestmark)        


#3.common ayit ulla numbers kandu pidiakan..

a={10,20,30,40,50}
b={30,40,50,60,70}
print(b &a)
print(a.intersection(b))

#4.a yil mathram ulla elementine print cheyan..

a={10,20,30,40,50}
b={30,40,50,60,70}

print(a.difference(b))

#5.stringil ulla vowels

text="hello world"
count=0
for i in text:
    if i in "aeiou":
        count+=1
print(count)        

#6.tuple ulla even numbers count cheyan

numbers=[5,10,15,20,25,30]
count=0
for i in numbers:
    if i %2==0:
        count+=1
print(count)          


# 7.smallest mark
students={
    "Anu":85,
    "Meera":92,
    "Riya":78,
    "Amal":95
}

#8.reverse order

