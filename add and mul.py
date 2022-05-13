def add(x):
    b=0
    for a in range(x+1):
        b=a+b
    return(b)

def mul(y):
    c=1
    for a in range(1,y+1):
        c=a*c
    return(c)
        
z=add(10)
s=mul(10)
print(z)
print(s)