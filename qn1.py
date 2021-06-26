'''Write a Python function to find the Max of three numbers'''
a=3
b=4
c=5
def  max (a,b,c):
    if a>b :
        return a
       # print("a is max")
    elif b>c:
        return b
       # print("b is max")
    elif c>a:
        return c
        #print("c is max")
#max (1,2,3)
print(max(a,b,c))

