''' Write a program to find the factorial of a number using functions.'''

num=int(input('Enter number : '))
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
ans=factorial(num)
print(f'the factorial of {num} is {ans}')
