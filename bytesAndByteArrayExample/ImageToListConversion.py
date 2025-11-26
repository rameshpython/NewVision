#1. Loading Image to Python Programme
#By Default Image will be loaded to bytes ---->Because it is immutable
import sys
from traceback import print_tb

with open("D:\\NewVision\\SampleImage.jpeg","rb") as f:
    y=f.read()
    mylist = list(y)

    print(type(y)) #<class 'bytes')
    print(type(mylist)) #<class 'list')
    print(sys.getsizeof(y)) #7366 --Because it is a raw data
    print((sys.getsizeof(mylist))) #58728 ---Because it is un-encrypted-not raw data --META-DATA


#Cheking Index Length in both cases

print(len(y)) #7333
print(len(mylist)) #7333


#Question : bytes is taking less memory compare to list, then why don't we take everything in Bytes? instead of list
#Answer : Bytes will be there in Enceryped , not Developer friendly, and it will be used for only specific cases.
#Examples --Images, Videos,Audios and Networking

print(y) #Encryped manner
print((mylist)) #Encrypted manner only because, we took it from bytes only at line number 7


if(y==mylist):
    print("Both are equall")
else:
    print("Both are not EQUAL, becuase, internally charcter converts to ASCII\n------------------------------------------------------")
