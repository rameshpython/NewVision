#1. Loading Image to Python Programme
#By Default Image will be loaded to bytes ---->Because it is immutable
import sys

with open("D:\\NewVision\\SampleImage.jpeg","rb") as f: #read --r, write -w, read and write -rw
    x=f.read()

print((sys.getsizeof(x)),"in bytes") #7366 in bytes
print(x) # encrypted text
print(type(x)) #<class 'byte'>
print(len(x)) #original size-Indexed manner


#Converting bytes to ByteArray
convertedByteArray = bytearray(x)

print(type(convertedByteArray)) # <class 'bytearray'>
print(sys.getsizeof(convertedByteArray),"in bytes") #7366 in bytes
print(convertedByteArray) # encrypted text
print(len(convertedByteArray)) #7633

#checking Encryped data equall in both cases, that is "x and convertedByteArray"

if(x==convertedByteArray):
    print("Both are Equally matched\n--------------------------------------------")


#convertedByteArray values modifying at index 40
convertedByteArray[40]=244

#Comparing again each other
if(x==convertedByteArray):
    print("again comparing both ---Now also both are equal")
else:
    print("Oh! Both are not Equal after modification ")

# again I am going to modify index 40 in bytes also
# x[40]=244  #Here, Expecting the error, becuase, bytes is the IMMUTABLE Object, we can not change

print("*************\nEnd of the programme")