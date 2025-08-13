#Takes user input and write it to a file
# again take user input and append to the same file
#read the file by adding "Final optput of the file " at the first line
# We have to carefully insert the print statements
#use /n to break the lines
User_Input1 = input("Enter text to write to the file : ")
file1 =open("output.txt","w")
file1.write(User_Input1+"\n")
file1.close()
print("Data sucessfully written to output.txt")
print()                  #for extra space
# Appending user input to the file
User_input2 = input("Enter Additional text to append :")
li=open("output.txt","a")
li.write(User_input2+"\n")
li.close()
print("Data sucessfully appended to output.txt")
print()
print("Final content of output.txt:")
fly=open("output.txt","r")
rea=fly.read()
print(rea)
fly.close()



