## Library books API ##

This API project implements a FastApi that created to manage books in library,collection of SQLALchemy packages to interact with databases and models validation by Pydantic.The API helps users to perform operations such as creating,reading,deleting and updating  books and also allows to search for a book either by title or author.

## How to run FastAPI application ##

    -Installation of Python  on your system
    -setting the virtual environment for new project
    -Install database  tool POSTGRESQL 
    -Configure environment variable by connecting database with your python codes
    -install uvicorn for run application
        "pip install uvicorn"
    -Run FastApi server by command
        "uvicorn main:app --reload"

## How to access FastApi ##
To access fastapi visit "http://127.0.0.1:8000





## Endpoints and Their Purpose ##
    1.GET /books
        Retrieves a list of all books in the library also the purpose is to fetch the entire catalog of books and return a list of books in JSON format.

    2.GET /books/{book_id}
        Retrieves details of a specific book by its id also the purpose is to fetch information about a single book and returns the book's details if it exists, 404 if not found.

    3.POST /books
        Adds a new book to the library also purpose is to allows the addition of a new book by providing the required details (title, author, etc.) and returns the created book and its ID.

    4.PUT /books/{book_id}
        Updates an existing book's information by id also the purpose is to modify the details of an existing book and returns the updated book, 404 if not found.

    5.DELETE /books/{book_id}
        Deletes a book from the library by its id also the purpose is to remove a book from the system and returns 204 No Content if successful, 404 if not found.

    6.GET /books/search? title=*** & author=***
        Searches for books by title or author also the purpose is to enables querying the book catalog by title, author and returns the list of books matching the search criteria.

## Assumptions and Design Decisions ##
    1.PostgreSQL Database:
        The application assumes a PostgreSQL database setup for the library database. Database URL is stored in environment variables for flexibility.

    2.ORM with SQLAlchemy:
        SQLAlchemy is used to map the books table to a Python class, allowing object-oriented interaction with the database.

    3.Error Handling:
        Proper error handling is implemented to return appropriate HTTP status codes includes 404 for resources not found,
        422 for invalid data input (e.g., missing required fields when adding or updating books) and 500 for internal server errors.

    4.Pydantic Models:
        Pydantic models are used for input validation, ensuring the correct data structure when creating or updating books.

    5.Search Functionality:
        The search functionality supports querying books by title, author, or both. This design decision adds flexibility to the API for library users looking for specific books.

## Modifying our system ##
    User Authentication
     -Creating new user table with columns ID, Username, and 
     password
     -Implementing user login endpoints
     -The use of JWT Tokens for authentication
     -Add new field "user_id" to a books table

## Simple interface on how to use ##
    I create a simple CLI Application to interacts with my API
      -This application can give user the following accessess.
       .User login
       .User can create,read,update and delete book to or from the table
       .The use of search functionality.

    This application i build by using "request library" so as i can make HTTP requests to my API