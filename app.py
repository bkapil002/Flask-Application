from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 2"}
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

@app.route('/books', methods=['POST'])
def add_book(): 
    new_book = request.json
    books.append(new_book)
    return jsonify({'message': 'Book added successfully', 'book': new_book}), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            book.update(request.json)
            return jsonify({'message': 'Book updated successfully', 'book': book})
    return jsonify({'error': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for index, book in enumerate(books):
        if book['id'] == book_id:
            books.pop(index)
            return jsonify({'message': 'Book deleted successfully'})
    return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':          
    app.run(debug=True)
