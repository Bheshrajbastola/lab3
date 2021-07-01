''' Write a Python function that takes a number as a parameter and check the number is prime or not.'''

def prime(num):
    if num%2==0 or num%3==0:
     return "not prime "
    else:
        return "prime number"
number=int(input("enter a number : "))
i=prime(number)
print(i)





