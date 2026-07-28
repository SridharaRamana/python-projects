contacts = {
'mahesh':9899893902,
'veera':123456789,
'eswar':7787879556
}

while True:
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View All")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        name=input("Enter the name: ")
        phone=int(input("Enter the phoneno: "))
        contacts[name]=phone
        
        
    elif choice == "2":
         name=input("Enter the name: ")
         if name in contacts:
            print(contacts[name])
         else:
            print("Contact not found.")
             
        
    elif choice == "3":
        for key, value in contacts.items():
            print(f'{key}: {value}')

    elif choice == "4":
        break;