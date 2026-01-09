n_terms=int(input("how many terms:"))
n1=0
n2=1
count=2 #To keep a track
if n_terms<=0:
    print("Please Enter positive Number!")
elif n_terms==1:
    print("Fibonacci Series up to",n_terms,":")
    print(n1)
else:
    print("Fibonaaci series up to",n_terms,":")
    print(n1,",",n2,end=",")
    while count < n_terms:
        nth=n1+n2
        print(nth,end=",")
        n1=n2
        n2=nth
        count+=1
