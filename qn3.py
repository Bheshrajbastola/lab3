''' Write a function called show Numbers that takes a parameter called limit.
It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
 For example, if the limit is 3, it should print:0 EVEN1 ODD2 EVEN'''

num=0
def shownumber(limit):
    for i in range(0,limit+1):
        if i%2==0:
            print(i,"even")
        else:
            print(i,"odd")

shownumber(10)
