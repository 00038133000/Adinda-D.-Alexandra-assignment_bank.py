# -*- coding: utf-8 -*-
"""bank

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17pcSfqsN6-qsRUcUPW_vK3dEhbAfYTSN
"""

#version 1
#without sample_str

kata = input('Enter your greetings: ').strip().lower() 
if kata == 'hello':
  print('$0')
elif kata[0:5] == ('hello'):
  print('$0')
elif kata[0] == 'h':
  print('$20')
else:
  print('$100')

#version 2
#with sample_str 

sample_str = "hello"

kata = input('Enter your greetings: ').strip().lower() 
if kata[0:5] == sample_str:
  print('$0')
elif kata[0] == sample_str[0]:
  print('$20')
else:
  print('$100')

#version 3
#using katahello 

kata = input('Enter your greetings: ').strip().lower()
katahello = 'hello'

if katahello in kata:
  print('$0')
elif katahello[0] in kata[0]:
  print('$20')
else:
  print ('$100')