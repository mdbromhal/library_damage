# With help from Copilot AI
from flask import Flask, render_template
import requests
import pandas as pd

app = Flask(__name__) # Starting flask app


def get_book_data(title, author):
    """
    Uses Open Library API to grab the book cover url and description for each book, given the title and author.
    """

    # Open Library API endpoint
    api_url = f"https://openlibrary.org/search.json?title={title}&author={author}"

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        
        if data['docs']: # Checking if books found
            first_entry = data['docs'][0] # Getting first result
            cover_id = first_entry.get('cover_i', '')
            description = first_entry.get('description', 'No description available.')
            cover_url = f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg" if cover_id else ""

            return {
                "title": title,
                "author": author,
                "cover_url": cover_url,
                "description": description
            }
        
        else:
            return {"title": title, "author": author, "cover_url": "", "description": "No data found."}
    
    else:
        return {"title": title, "author": author, "cover_url": "", "description": "API error."}


def read_books_csv(filepath):
    """
    Reading the book title and author from a csv file. Transforming into a list of dictionaries.
    """
    df = pd.read_csv(filepath)
    books = df.to_dict(orient='records')
    return books


@app.route('/') # setting as home url
def book_gallery():
    """
    Home page for book gallery. 
    Reads books in from csv file and gets book data with Open Library API.
    Uses html template to display book covers and titles on a webpage.
    """

    # books = [
    #     {"title": "1984", "author": "George Orwell"},
    #     {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    #     {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
    # ]

    books = read_books_csv('books.csv')


    book_data = [get_book_data(book['Title'], book['Author']) for book in books]

    return render_template('books.html', book_data=book_data)


if __name__ == '__main__':
    app.run(debug=True)

