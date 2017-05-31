#print("hello")

a=1
b=2
#print(a,b,c)
def swp():
        #print(a,b,c)
        global a,b
        #a=a+1
        c=a

        print(a,b,c)
        b=c
        print(a,b,c)
        a=b
        print(a,b,c)
swp()
print(a,b)
