'''Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.'''

def case_letter(string):
    a=0
    b=0
    for i in string:
        if i .isupper():
            a=a+1
        elif i.islower():
            b=b+1
    print(f"{a} :upper case letter ")
    print(f"{b} :lower case letter ")
string=str(input("enter  word : "))
case_letter(string)






