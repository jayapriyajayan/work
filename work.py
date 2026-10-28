words=["apple","ant","banana","ball","cat","dog"]

#    'a':['apple','ant']
#    'b':['banana','ball']
#    'c':['cat']
#    'd':['dog']
# }
result={}
for i in words:
   result.setdefault(i[0],[]).append(i)
print(result)   
