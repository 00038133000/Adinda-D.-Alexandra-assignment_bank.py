# -*- coding: utf-8 -*-
"""bank

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17pcSfqsN6-qsRUcUPW_vK3dEhbAfYTSN
"""

#version 1
#without sample_str

kata = input('Hello, welcome to the Bank! ')
if kata == 'Hello':
  print('$0')
elif kata[0:5] == ('Hello'):
  print('$0')
elif kata[0]== 'H':
  print('$20')
else:
  print('$100')

#version 2
#with sample_str 

sample_str = "Hello"

kata = input('Hello, welcome to the Bank! ')
if kata[0:5] == sample_str:
  print('$0')
elif kata[0] == sample_str[0]:
  print('$20')
else:
  print('$100')

#version 3
#using katahello 

kata = input('Hello, welcome to the Bank! ')
katahello = 'Hello'

if katahello in kata:
  print('$0')
elif katahello[0] in kata:
  print('$20')
else:
  print ('$100')