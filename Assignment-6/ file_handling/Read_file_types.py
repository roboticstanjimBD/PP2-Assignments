"""Read Only Parts of the File
By default the read() method returns the whole text, but you can also specify how many characters you want to return:"""



with open("dump.txt") as f:
    print(f.read(500))



"""Read Lines
You can return one line by using the readline() method:"""

with open("dump.txt") as f:
    print(f.readlines())
     


### for loop can be used :

with open("dump.txt") as f:
    for x in f:
        print(x)
