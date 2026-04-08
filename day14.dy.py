'''
recursion is a programming technique where a function calls itself either
directly or indirectly to slove a problem by breaking it into smaller subproblems.
recursion is espically useful for problems that can be divided into identical smaller
tasks, such as mathematical calculations, tree traversals or divide-and-conquer algorithms.

def fibbonaci_pin(self)
    while self.remaining_attempts > 0:
        use_pin = input("enter 4 digit pin: ")
        if len(user pin) == 4 and user_pin == self.user_info["atm pin"]:
            print("welcome to the atm")
            return true
        else:
             self.remaining_attemts -= 1
             if self.remaining_attempts > 0:
                 print(f" invalid pin. attempts left:  {self.remaning_attempts}")
             else:
                  print(" card blocked. please contact customer care")
                  return false


#prime number
prime_num = 7
count = 0
def prime_check(prime_num,k):
    for j in range(1,prime_num+1):
        if prime_num % j == 0 :
            k += 1
    if k== 2:
        print("prime")
    else:
        print("not prime")
prime_check(prime_num,count)
           
#palindrome
palindrome = input("enter word:   ")
def is_palindrome(s):
    if palindrome == palindrome[::-1]:
        print("palindrome")
    else:
        print("not a palindrome")
is_palindrome(palindrome)



#even number
even= int(input("enter num:   "))
def is_even(s):
    if even %2==0:
        print("even number")
    else:
        print("not even number")
is_even(even)




def vowel_consonets(sai,vowels_list,consonets_list):
    for j in sai:
        if j in "AEIOUaeiou":
            vowels_list.append(j)
        else:
            consonets_list.append(j)
    print(f"{vowel_list} these are all vowel in the string")
vowel_consonets(sai=input("enter data"),consonets_list=[],vowels_list=[])

'''
SBI_deepak = {"Name" : "deepak",
                      "ATM PIN" : "2391",
                      "Balance":5000}
user_pin = input (" Enter Pin: ")
if len(user_pin) == 4:
    if user_pin in SBI_deepak["ATM PIN"]:
        user_choice = int(input("enter your choice : "))
        if user_choice == 1:
            money_w = int(input("enter money you want to withdraw"))
            if money_w <= SBI_deepak["Balance"]:
                SBI_deepak["Balance"] -= money_w
                print ( SBI_deepak["Balance"])
            else:
                print("Insufficient balance")
        elif user_choice == 2:
            Deposite_M = int(input("pls enter the money you want to deposite"))
            if Deposite_M % 100 == 0 and Deposite_M>=1000:
             SBI_deepak['Balance'] += Deposite_M
             print(f"you have deposite {Deposite_M} and the total  is {SBI_deepak}")
            else:
                print(f"{Deposite_M} you have entered  is change or less than 5000/-")
    else:
            print("You have enetered invalid pin")
else:
    print("Pls enter 4 digit pin")
             
        

    
