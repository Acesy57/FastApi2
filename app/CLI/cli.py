import requests



url = "http://127.0.0.1:8000"

def authentication(username, password):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"username": username, "password": password}
    resp = requests.post(f"{url}/login/", headers=headers, data=data)
    if resp.status_code == 200:
        return resp.json()["access_token"]
    return None

def list_books(token):
    if not token:
        print("Failed to authenticate")
        return
    resp = requests.get(f"{url}/books/", headers={"Authorization": f"Bearer {token}"})
    if resp.status_code == 200:
        books = resp.json()
        for i, book in enumerate(books, 1):
            print("*" * 25)
            print(f"{book['id']}: {book['title']}")
            print(book["author"])
    else:
        print("Failed to get books")
        print(resp.text)

def add_book(token):
     if not token:
          print("failed to authenticate")
          return
     title = input("Enter book name: ")
     author = input("Enter author of the book: ")
     isbn = input("Enter isbn: ")
     publication_year = input("Enter publication_year")
     available = input("It is available??")
     data = {
          "title": title,
          "author": author,
          "isbn": isbn,
          "publication_year": publication_year,
          "available": available
     }
     
     resp = requests.post(f"{url}/books/", headers={"Authorization": f"Bearer {token}"}, json=data)
     if resp.status_code == 201:
          print("book was added successfully")
     else:
          print("failed to add book")
          print(resp.text)

def update_book(token):
     if not token:
          print("failed to authenticate")
          return
     book_id = input("Enter id of the book to update")
     title = input("Enter book name: ")
     author = input("Enter author of the book: ")
     isbn = input("Enter isbn: ")
     publication_year = input("Enter publication_year")
     available = input("It is available??")
     data = {
          "title": title,
          "author": author,
          "isbn": isbn,
          "publication_year": publication_year,
          "available": available
     }
     resp = requests.put(f"{url}/books/{book_id}/", headers={"Authorization": f"Bearer {token}"}, json=data)
     if resp.status_code == 200:
          print("book was updated successfully")
     else:
          print("failed to update book")
          print(resp.text)

def delete_book(token):
     if not token:
          print("failed to authenticate")
          return
     book_id = input("Enter id of the book to delete")
    #  title = input("Enter book name: ")
    #  author = input("Enter author of the book: ")
    #  isbn = input("Enter isbn: ")
    #  publication_year = input("Enter publication_year")
    #  available = input("It is available??")
    #  data = {
    #       "title": title,
    #       "author": author,
    #       "isbn": isbn,
    #       "publication_year": publication_year,
    #       "available": available
    #  }
     resp = requests.delete(f"{url}/books/{book_id}/", headers={"Authorization": f"Bearer {token}"})
     if resp.status_code == 204:
          print("book was deleted successfully")
     else:
          print("failed to delete book")
          print(resp.text)

def search_book(token):
     if not token:
          print("failed to authenticate")
          return
     query = input("Enter the title of the book to search: ")

     resp = requests.get(f"{url}/books/?search={query}", headers={"Authorization": f"Bearer {token}"}, json=query)
     if resp.status_code == 200:
        books = resp.json()
        for i, book in enumerate(books, 1):
            print("*" * 25)
            print(f"{i}: {book['title']}")
            print(book["author"])
     else:
        print("No book found")
        print(resp.text)
print("Welcome to LIBRARY MANAGEMENT SYSTEM")
while True:
    print("""
Choose an Option:

1. Login
0. Exit
""")
    option = input(" Choose your choice: ")
    if option == '1':
        print("Please enter credentials")
        username = input("Username: ")
        password = input("Password: ")
        token = authentication(username=username, password=password)


        if not token:
            print('Invalid credentials')
            break
        print("Successfully Logged In")
        while True:
            print("""
Choose a choice:

1. List books
2. Add book
3. Update book
4. Delete book
5. Search book
0. Logout
""")
   
    
            logged_in_option = input("Enter your input: ")
            if logged_in_option == '1':
                 list_books(token)

            elif logged_in_option == '2':
                 add_book(token)
            elif logged_in_option == '3':
                 update_book(token)
            elif logged_in_option == '4':
                 delete_book(token)
            elif logged_in_option == '5':
                 search_book(token)
            elif logged_in_option == '0':
                 print('Successfully logged out')
                 break
            else:
                 print("\n\nInvalid Option selected\n\n")
    elif option == '0':
                print("Thank you for using the system")
                break
    else:
                 print("\n\nInvalid option selected\n\n")
    