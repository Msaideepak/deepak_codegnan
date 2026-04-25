'''
File handling
-------------
--> file handling is an object oriented file to maintain several functions of file such as
    creating, reading, writing and update also deleting the file.
1.open()
--> this open() takes 2 parameter and in this we have to close the file by calling close()
    function after program.
    
2. with open()
Modes ("r","w","a","x","t")
---------------------
1. "r" -- read
------
--> to read the file we will this mode and if the file doesn't exist. it will through the error

any = open("demofile","r")
print(any.read())
any.close()

2. "w" -- write
----------------
--> to write the text into the file we will use this mode and it will create the file if it doesn't exist
any = open("demofile","w")
print(any.write())
any.close()

3. "a" -- append
-----------------
--> to add the text into the file this is used and it will create the file if it doesn't
any = open("demofile","a")
print(any.write("i am codegnan student"))
any.close()

4. "x" -- create
----------------
--> this is used to create th file, but is the is already in the system it raise an error

any = open("demofile","x")
any.close()

To read a file
--------------
1.read() --> this method can read the entire file chunk by chunk we can also specify the size
any = open ("demofile","r")
print(any.read(1000))
any.close()

2.readline()--> this method can read only one line at a time
any = open ("demofile","r")
print(any.readline())
any.close()

3.readlines()--> this method can read the entire file and return into list with each line is one index in the list.
'''
any = open ("demofile","r")
print(any.readlines())
any.close()














