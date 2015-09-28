#inlude<stdio.h>
#include<string.h>

vars = "Oxso","OXO","123454321","ROTATOR","12345 54321"

for i in range(len(vars)):
  if vars[i] == vars[i][::-1]:
    print("true")
  else:
     print("false")