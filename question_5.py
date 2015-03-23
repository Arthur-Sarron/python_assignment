counter = 1
a=0
n = input("enter a number\n")
n = int(n)
        

for i in range (1,n+1):
    counter = counter*i
    a=a+1/counter
   
print("the mathematical constante e of this number is", a)
