''' Write a Python program to reverse a string.'''

def reverse(word):
    word=word[::-1] #slice operator [start:stop:step]
    print(word)
word=str(input("enter a string : "))
reverse(word) #function call

