from main import BooksCollector
import pytest

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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_added_book_has_no_genre(self):
        name_book = 'Девушка в поезде'
        collector = BooksCollector()
        collector.add_new_book(name_book)
        assert collector.books_genre[name_book] == ''

    def test_add_new_book_get_name_new_added_book_from_books_genre(self):
        name_book = 'Барат'
        collector = BooksCollector()
        collector.add_new_book(name_book)
        assert list(collector.books_genre.keys())[-1] == 'Барат'

    @pytest.mark.parametrize('name,genre', [
        ['Пятый элемент', 'Фантастика'],
        ['28 дней спустя', 'Ужасы'],
        ['Достать ножи', 'Детективы'],
        ['Русалочка', 'Мультфильмы'],
        ['Зеленая книга', 'Комедии']
    ])
    def test_set_book_genre_new_book_has_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    def test_get_book_genre_book_has_genre_is_comedy(self):
        book_name = 'Зеленая книга'
        book_genre = 'Комедии'
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.books_genre[book_name] == 'Комедии'

    def test_get_books_genre_add_book_and_books_genre_not_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Ходячие мертвецы')
        assert len(collector.books_genre) != {}

    def test_add_book_in_favorites_get_name_added_book_from_favorites(self):
        book_name = 'Ходячие мертвецы'
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert collector.favorites[-1] == 'Ходячие мертвецы'

    def test_delete_book_from_favorites_is_empty_after_delete_book(self):
        book_name = 'Ходячие мертвецы'
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert collector.favorites == []

    def test_get_list_of_favorites_books_is_not_empty_after_added_books(self):
        books_name = ['Криминальное чтиво', 'От заката до рассвета', 'Четыре комнаты']
        collector = BooksCollector()
        for name in books_name:
            collector.add_new_book(name)
            collector.add_book_in_favorites(name)
        assert collector.favorites != []

    def test_get_books_with_specific_genre_get_list_of_books_with_genre_is_horror(self):
        collector = BooksCollector()
        names_book = ['Рассвет мертвецов', 'Война миров Z']
        set_genre = 'Ужасы'
        for book_name in names_book:
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, set_genre)
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 2

    def test_get_books_for_children_add_three_books_len_equals_three(self):
        collector = BooksCollector()
        collector.books_genre['Бременские музыканты'] = 'Мультфильмы'
        collector.books_genre['Последний богатырь'] = 'Комедии'
        collector.books_genre['Спирит Душа Прерий'] = 'Мультфильмы'
        assert len(collector.get_books_for_children()) == 3