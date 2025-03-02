BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __int__(self, id_: int, pages: int, name: str):

        if not insistance(id_, int):
            raise TypeError("Идентификатор должен быть типа int")
        if id_ < 0:
            raise ValueError("Идентификатор не может быть отрицательным числом")
        self.id_ = id_

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages < 0:
            raise ValueError("Количество страниц не может быть отрицательным числом")
        self.pages = pages

        if not isinstance(name,str):
            raise TypeError("Название книги должно быть типа str")
        self.name = name

    def __str__(self)->str:
        return f'Книга "{self.name}"'
    def __repr__(self) -> str:
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})'


class Library:
    def __init__(self, books: list = None):
        self.books = [] if books is None else books
    def get_next_book_id(self) -> int:
        return 1 if not self.books else self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_: int) -> int:
        for index, book in enumerate(self.books):
            if id_ == books.id_:
                return index
            raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
