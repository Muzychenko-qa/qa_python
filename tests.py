import pytest
from main import BooksCollector

class TestBooksCollector:

    books_list = [
            ['Чемодан', 'Комедии'],
            ['Алиса в стране чудес', 'Мультфильмы'],
            ['Чапаев и Пустота', 'Фантастика']
        ]
    book_long_name = 'Очень длинное Очень длинное Очень длинное Очень длинное Очень длинное Очень длинное название'

    def test_add_new_book_add_book_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book('Кладбище домашних животных')
        assert 'Кладбище домашних животных' in collector.books_genre

    def test_add_new_book_name_longer_than_40_characters_book_not_in_list(self):
        collector = BooksCollector()
        collector.add_new_book(self.book_long_name)
        assert self.book_long_name not in collector.books_genre

    @pytest.mark.parametrize('name, genre', books_list)
    def test_set_book_genre_set_genre_positive_result(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_set_book_genre_genre_not_in_list_not_set_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Кладбище домашних животных')
        collector.set_book_genre('Кладбище домашних животных', 'Триллер')
        assert collector.get_book_genre('Кладбище домашних животных') == ''

    @pytest.mark.parametrize('name, genre', books_list)
    def test_get_book_genre_get_genre_positive_result(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert [name] == collector.get_books_with_specific_genre(genre)

    @pytest.mark.parametrize('name, genre', books_list)
    def test_get_books_with_specific_genre_get_books_positive_result(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert name in collector.get_books_with_specific_genre(genre)

    def test_get_books_genre_get_dict_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book('Чемодан')
        collector.set_book_genre('Чемодан', 'Комедии')
        books_genre = collector.get_books_genre()
        assert books_genre == {'Чемодан': 'Комедии'}

    @pytest.mark.parametrize('name, genre', books_list)
    def test_get_books_for_children_get_books_positive_result(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.get_books_for_children()
        assert name in collector.get_books_for_children()

    def test_get_books_for_children_genre_age_rating_did_not_pass(self):
        collector = BooksCollector()
        collector.add_new_book('Злая Алиса в стране чудес')
        collector.set_book_genre('Злая Алиса в стране чудес', 'Ужасы')
        collector.get_books_for_children()
        assert 'Злая Алиса в стране чудес' not in collector.get_books_for_children()

    def test_add_book_in_favorites_add_valid_value_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book('Злая Алиса в стране чудес')
        collector.add_book_in_favorites('Злая Алиса в стране чудес')
        assert 'Злая Алиса в стране чудес' in collector.favorites

    def test_delete_book_from_favorites_delete_book_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book('Злая Алиса в стране чудес')
        collector.add_book_in_favorites('Злая Алиса в стране чудес')
        collector.delete_book_from_favorites('Злая Алиса в стране чудес')
        assert 'Злая Алиса в стране чудес' not in collector.favorites

    def test_get_list_of_favorites_books_get_list_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book('Злая Алиса в стране чудес')
        collector.add_book_in_favorites('Злая Алиса в стране чудес')
        assert collector.get_list_of_favorites_books() == ['Злая Алиса в стране чудес']
