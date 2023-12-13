import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2

        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector
    @pytest.mark.parametrize(
        'name',
        [
            '',  # Пустое название книги
            'TooLongBookNameTooLongBookNameTooLongBookNameTooLongBookName',  # Слишком длинное название книги

        ]
    )
    def test_negative_add_new_book(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert not collector.get_books_genre()

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Alien', 'Ужасы'],
            ['Незнайка на Луне', 'Фантастика']
        ]
    )
    def test_set_book_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Alien', 'Ужасы'],
            ['Незнайка на Луне', 'Фантастика']
        ]
    )
    def test_get_books_with_specific_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        books_with_specific_genre = collector.get_books_with_specific_genre(genre)
        assert name in books_with_specific_genre

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Alien', 'Ужасы'],
            ['Дети кукурузы', 'Ужасы']
        ]
    )
    def test_get_books_with_specific_genre_2(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book('Alien')
        collector.add_new_book('Дети кукурузы')
        collector.set_book_genre('Alien', 'Ужасы')
        collector.set_book_genre('Дети кукурузы', 'Ужасы')
        books_with_specific_genre = collector.get_books_with_specific_genre(genre)
        assert len(books_with_specific_genre) == 2

    @pytest.mark.parametrize(
        'name, genre',
        [

            ['Незнайка на Луне', 'Фантастика']
        ]
    )
    def test_get_books_for_children(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        books_for_children = collector.get_books_for_children()
        assert name in books_for_children

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Alien', 'Ужасы']

        ]
    )
    def test_negative_get_books_for_children(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        books_for_children = collector.get_books_for_children()
        assert name not in books_for_children

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Alien', 'Ужасы'],

        ]
    )
    def test_add_book_in_favorites(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)
        books_favorites = collector.get_list_of_favorites_books()
        assert name in books_favorites

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Alien', 'Ужасы'],

        ]
    )
    def test_add_book_in_favorites_twice(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book('Alien')
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites('Alien')
        collector.add_book_in_favorites('Alien')
        books_favorites = collector.get_list_of_favorites_books()
        assert len(books_favorites) == 1
