class View:
    @staticmethod
    def render_error(message):
        return {"error": message}

    staticmethod
    def render_success(message, book_id=None):
        response = {"message": message}
        if book_id:
            response["book_id"] = book_id
        return response
    
    @staticmethod   
    def render_book(book):
        return {
            "book_id": book.book_id,
            "author_id": book.author_id,
            "book_title": book.book_title,
            "publisher_id": book.publisher_id,
            "vendor_id": book.vendor_id,
            "shelf_id": book.shelf_id,
            "category": book.category,
            "price": book.price,
            "language_name": book.language_name,
            "subject_name": book.subject_name,
            "genre": book.genre,
            "date_of_publishing": book.date_of_publishing,
            "date_of_addition": book.date_of_addition,
            "availability": book.availability,
            "shelf_date": book.shelf_date,
            "bought_on": book.bought_on,
            "cover_page": book.cover_page
        }
