# -*- coding: utf-8 -*-
"""scpt2_between_prime.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1upBw34gis1XTGhov72SpJOQU0etMuaY3
"""

l_value = int(input("enter the Lowest Range value: "))
u_value = int(input("enter the Uppper Range value: "))

for num in range(l_value,u_value + 1):
  if num > 1:
    for i in range(2,num):
      if (num % i) == 0:
        break
    else:
      print(num)