seq=str(input("Sequence?"))
import math
C="0,"
k=1
while k!=math.inf and len(str(k))<=len(str(seq)) and seq not in C:
  C=C+str(k)
  k=k+1
print(C)
if seq in C:
  print("seq in C")
else:
  print("seq not in C")
