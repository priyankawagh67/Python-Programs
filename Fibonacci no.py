nterms = int(input("How Many terms Do You Want-?"))
n1,n2=0,1
count=0
if nterms <=0:
  print("plz enter positive integer number")
elif nterms ==1:
  print("Fibonacci Sequence upto",nterms,":")
  print(n1)
else:
    print("Fibonacci Squence Is:")
    while count<nterms:
      print(n1)
      nth=n1+n2
      n1=n2
      n2=nth
      count +=1
      
