def dec2bin(n:int)->int:
  n2="" 
  while n=>2:
    n2=str(n%2)+n2
    n=n//2
  n2="1"+n2
  n=int(n2) 
  n2=""
  return n 
