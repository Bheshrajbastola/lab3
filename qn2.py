''' Write a function called fizz_buzz that takes a number.
If the number is divisible by 3, it should return “Fizz”.
If it is divisible by 5, it should return “Buzz”.
If it is divisible by both 3 and 5, it should return “FizzBuzz”.
Otherwise,it should return the same number.'''

def fizzbuzz(num): #defining
    if num%3==0 and num%5==0: #formula with if statenment
         print("FizzBuzz")
    elif  num%3==0:
        print("Fizz")
    elif  num%5==0:
        print("Buzz")
    else:
        print("not divisible by 5&3")
num=int(input("num : "))
fizzbuzz(num) # calling the function
