
Table_size=10
ascii_key=0

while True:
    print("\n -----HASH PROGRAM----")
    print("1.if key is integer")
    print("2.if key is string")
    print("3.End the program")

    option=int(input("choice your option:"))
    if option==1:
        key=int(input("\nenter your rollNo:"))
    
        Hash_Table1=[]
        Hash_Table2=[]

        Hash_index=key%Table_size
        Hash_Table1.append(Hash_index)

        for i in range(0,Table_size):
            Hash_Table2.append([])

        if Hash_index in Hash_Table1:
            Hash_Table2[Hash_index-1]=[key]

        for i in range(0,len(Hash_Table2)):
            print("Index of "+ str(i) +":"+" "+ str(Hash_Table2[i]))
        
    elif option==2:
        key=input("\nenter your name:")
        for i in key:
            a=ord(i)
            ascii_key=ascii_key+a

        Hash_Table1=[]
        Hash_Table2=[]

        Hash_index=ascii_key%Table_size
        Hash_Table1.append(Hash_index)

        for i in range(0,Table_size):
            Hash_Table2.append([])

        if Hash_index in Hash_Table1:
            Hash_Table2[Hash_index-1]=[key]

        for i in range(0,len(Hash_Table2)):
            print("Index "+ str(i) + ": "+ " "+str(Hash_Table2[i]))
    
    elif option==3:
        print("end of the program")
        break
    else:
        print("invalid option")

        

      
        





    
    