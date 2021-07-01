'''Write a Python function that checks whether a passed string is palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.'''

def palindrome():
    string=str(input("enter word : "))
    reversed_word=string[::-1]
    if reversed_word==string:
        print("palindrome")
    else:
        print("not a palindrome")
palindrome()



