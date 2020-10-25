#initializing starting 2 nos.
#taking input of nth no. upto which fibonacci series is to be printed
a,b = 0,1
n = int(input())
s = 0 #counter to be incremented
while s < n:
  print(a)
  s = a + b
  print(s)
  a = b
  b = s
  s += 1
  
  # USING FUNCTIONS :
  def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))
print("fibonacci series is :")
n = int(input("enter range:"))
print("\n")
if n < 0:
    print("provide range in positives")
else:
    for i in range(n):
        print(fib(i))
