from random import randint


import random

message = input("tell mes something and ill encrypt it --> ")

#setting up keys and lists 
input_list = []
encrypt_list = []
cryptkey1 = randint(1,9)


#putting letters into list
for i in message:
    input_list.append(i)
print(input_list)

#incrypt characters
for letter in input_list:
    encrypt_list.append(ord(letter)+cryptkey1)

print(encrypt_list)

print(cryptkey1)

#un-encrypt
final = ''
for num in encrypt_list:
    final += chr(num-cryptkey1)

input("hit any button to see your message") 

print(f"your message was <{final}>")








