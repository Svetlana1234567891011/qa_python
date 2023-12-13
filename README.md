# qa_python
def test_add_new_book_add_two_books(self)  - добавление двух книг
def test_negative_add_new_book(self, name) - негативный сценарий добавления книг с некорректными названиями
def test_set_book_genre(self, name, genre) - проверка установки жанра
def test_get_books_with_specific_genre(self, name, genre) - выбор книги по жанру
def test_get_books_with_specific_genre_2(self, name, genre) - выбор нескольких книг из списка с одинаковым жанром
def test_get_books_for_children(self, name, genre) - выбор книг для детей
def test_negative_get_books_for_children(self, name, genre) - негативный тест, что неподходящие по жанру книги не добавляются в список для детей
def test_add_book_in_favorites(self, name, genre) - добавление книг в избранное
def test_add_book_in_favorites_twice(self, name, genre) - проверка невозможности добавить в избранное несколько раз
