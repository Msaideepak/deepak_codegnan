'''

a = 9
print(b)
for j in range(1,10):
    print(j) #if u print b and j for b is show name error because we never called b but after for j is intial variable

range()---> this is used to generate number
systax()---> range (start,end,step)

any = ("123")
print(int(any))
print(list(any))
print(tuple(any))

so = 123
print(str(so))
print(flaot(123))

an = [1,2,3]
vs = str(an)
print(type(vs))
print(vs)
print(tuple(an))

ab = [(1,2),(3,4)]
print(dict(ab))

rev_str = "mam"
empty_ = ""
for j in rev_str:
    empty_ = j+ empty_ 
if empty_==rev_str:
    print(f"{rev_str} is palin")
else:
       print(f"{rev_str} is not a palin")
'''
for num  in range(1,100):
    if num % 2 == 0:
        print(f"{num} is a even num")
    else:
        print(f"{num} is a odd num")
        
    


