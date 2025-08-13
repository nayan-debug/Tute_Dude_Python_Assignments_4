#open and read file line by line
#exception handling for FileNotFoundError
try:
    My_obj=open("sample.txt","r")
    My_var=My_obj.read()
    print(My_var)         # Display or print the content of the file
   
#Exception handling for file does not exist
except FileNotFoundError:
    print("The file 'sample.txt' was not found")
finally:
     My_obj.close()
    
