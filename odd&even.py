lst = [7,18,45,77,10,9,33,100]

  #method-1
  even=[]
  odd=[]
  for i in lst:
      if i%2==0:
          even.append(i)
      else:
           odd.append(i)
   print{f"sum of even numbers is :{sum(even)}")
   print{f"sum of odd numbers is :{sum(odd)}")

   #method-2
   sum_even=0
   sum_odd=0
   for i in lst:
       if i%2==0:
           sum_even+=i
       else:
           sum_odd+=i
   print(f"sum of even numbers is : {sum_even}")
   print(f"sum of odd numbers is :{sum_odd}")
