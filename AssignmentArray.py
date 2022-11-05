print("\n\t\t********PROGRAMMED BY:********")
print("\t\t***BEVERLY ANN L. RODRIGUEZ***\n")

#Write a python program that do the following:
#- display the initial content of the array.
#- display a menu of options.
#- allow user to select item in the menu.
#- perform the selected option.
#- display the resulting values of the array.


Array = [5,30,2,19,11,8,16,24,50,10]

def menu(): 
    print("""
           >>>>> WELCOME TO RODRIGUEZ`S PROGRAM <<<<<
             _____________________________________
            |            MENU OPTIONS             |
            |_____________________________________|   
            |      1. ADD AN ELEMENT              |
            |      2. INSERT AN ELEMENT           |
            |      3. MODIFY AN ELEMENT           |
            |      4. DELETE AN ELEMENT           |
            |      5. SMALLEST ELEMENT            |
            |      6. LARGEST ELEMENT             |
            |      7. ASCENDING ORDER             |
            |      8. DESCENDING ORDER            |
            |      9.SUM OF THE ELEMENTS          |
            |      10. EXIT                       |
            |_____________________________________|
    """)

def end():
    print("THANK YOU FOR USING THIS PROGRAM!")
    
menu()
option = int(input("\t\nSELECT AN OPTION (Choose from 1-10): "))
    
while option != 11:
    if option == 1:
        num = int(input("\tPlease enter the number you want to add: "))
        Array.append(num)
        print("\tThank you!!The element has been added.")
        print(f"\tTHIS IS NOW THE NEW ARRAY!! = {Array}")
       
    elif option == 2:
        insert = int(input("Please enter the number you want to insert: "))
        insert_idx = int(input(f"Enter the index you want to insert {insert}: "))
        Array.insert(insert_idx, insert)
        print("\tThank you!! The element has been inserted.")
        print(f"\tTHIS IS NOW THE NEW ARRAY!! = {Array}")
        
    elif option == 3:
        modify = int(input("\tPlease enter the index you want to change: "))
        modify_idx = int(input(f"\tPlease enter the element you want to modify: "))
        Array[modify] = modify_idx
        print("\tThe element has been modified.")
        print(f"\tTHIS IS NOW THE NEW ARRAY!! = {Array}")
        
    elif option == 4:
        delete = int(input("\tPlease enter the element you want to delete: "))
        Array.remove(delete)
        print("\tThank you! The element has been deleted.")
        print(f"\tTHIS IS NOW THE NEW ARRAY!! = {Array}")

    elif option == 5:
        small = min(Array)
        print("\tThank you! The element has been deleted.")
        print(f"\tTHE SMALLEST ELEMENT IN THE ARRAY IS: = {small}")

    elif option == 6:
        large = max(Array)
        print("\tThank you!! The largest element has now been identified.")
        print(f"\tTHE LARGEST ELEMENT IN THE ARRAY IS: = {large}")

    elif option == 7:
        Array.sort()
        print("\tThank you!! The list is now in ascending order.")
        print(f"\tTHIS IS NOW THE NEW ARRAY= {Array}")

    elif option == 8:
        Array.sort()
        Array.reverse()
        print("\tThank you!! The list is now in descending order.")
        print(f"\tTHIS IS NOW THE NEW ARRAY= {Array}")

    elif option == 9:
        sum = sum(Array)
        print("Thank you!! The sum of the elements has been defined.")
        print(f"\tTHIS IS THE TOTAL SUM OF THE ELEMENTS: = {sum}")
    elif option == 10:
        end()
        break
    menu()
    option = int(input("\t\nSELECT AN OPTION (Choose from 1-10): "))
    