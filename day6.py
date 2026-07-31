#1
# string=input("Enter a string:")
# char=''
# c=''
# maxcount=0
# length=1
# for i in range(len(string)-1):
#     if string[i]==string[i+1]:
#         length+=1
#         c=string[i]
#     else:
#         if length>maxcount:
#             maxcount=length
#             length=1
#             char=c
#             c=''
#         else:    
#             length=1
#             c=''
# if length>maxcount:
#     maxcount=length
#     char=c
# print(f'character = {char}')
# print(f'Length = {maxcount}')    

#2
# string=input("Enter a string:")
# char=input('Enter a charcter:')
# count=0
# count1=0
# for i in string:
#     if i==char:
#         count+=1
# if count>2 or count<2:
#     count1=-1
# else:
#     for i in range(len(string)-1):
#         if string[i]==char:
#             for j in range(i,len(string)):
#                 if string[j+1]!=char:
#                     count1+=1
#                 else:
#                     break    
# print(count1)                    

#3
# string=input("Enter a string:")
# maxcount=0
# word=''
# w=''
# for i in string:
#     if i!=' ':
#         w+=i
#     else:
#         count=0
#         for j in w:
#             if j in "aeiouAEIOU":
#                 count+=1
#         if count>maxcount:
#             maxcount=count
#             word=w
#             w=''
#         else:
#             w=''
# if count>maxcount:
#     word=w     
# print(word)                   

#4
# string=input("Enter a string:")
# count=0
# for i in range(len(string)-1):
#     if ord(string[i+1])-ord(string[i])==1:
#         count=0
#     else:
#         count+=1  
# if count>0:
#     print("No")
# else:
#     print("Yes")                     

#5
# string=input("Enter a string:")
# word=''
# revword=''
# for i in range(len(string)):
#     if string[i]!=' ':
#         word=word+string[i]
#     else:   
#         for j in range(len(word)-1,-1,-1):
#             revword=revword+word[j]
#         revword=revword+' '
#         word=''   
# for j in range(len(word)-1,-1,-1):
#         revword=revword+word[j]         
# print(revword)        

#6
# string=input("Enter a string:")
# maxcount=0
# char=''
# for i in string:
#     vol=''
#     count=0
#     if i in 'aeiouAEIOU':
#         vol=i
#         for j in string:
#             if j==vol:
#                 count+=1
#         if count>maxcount:
#             maxcount=count
#             char=vol
# if count>maxcount:
#     char=vol  
# print(char)                  
            
#7
# string=input("Enter a string:")
# count=0
# count1=0
# for i in string:
#     if i in 'aeiouAEIOU':
#         count+=1
#     else:
#         count1+=1
# if count==count1:
#     print('Balanced')
# else:
#     print('Not Balanced')            

#8
# string=input("Enter a string:")
# length=len(string)
# count=0
# if length%2==0:
#     for i in range(len(string)):
#         for j in range(len(string)-1,-1,-1):
#             if string[i]==string[j]:
#                 count=1
#             else:
#                 count=0
# if count==1:
#     print('Yes')
# else:
#     print('No')                        

#9
string=input("Enter a string:")
count=0
for i in string:
    if 'a'<=i<='z' or 'A'<=i<='Z' or '0'<=i<='9' or i=='_':
        count+=1
print(count)        

