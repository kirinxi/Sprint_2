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
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_duplicated_book(self):
        collector = BooksCollector()
        collector.add_new_book('Generation P')
        collector.add_new_book('Generation P')
        assert len(collector.get_books_rating()) == 1
    def test_set_book_rating_book_is_apsent(self):
        collector = BooksCollector()
        collector.set_book_rating('Преступление и наказание', 10)
        assert collector.books_rating.get('Преступление и наказание') != 10

    def test_set_book_rating_rating_less_than_one(self):
        collector = BooksCollector()
        collector.add_new_book('Духless')
        collector.set_book_rating('Духless', 0)
        assert collector.get_book_rating('Духless') == 1

    def test_set_book_rating_more_than_10(self):
        collector = BooksCollector()
        collector.add_new_book('Неудобное прошлое')
        collector.set_book_rating('Неудобное прошлое', 11)
        assert collector.get_book_rating('Неудобное прошлое') == 1

    def test_set_book_rating_not_added_book(self):
        collector = BooksCollector()
        collector.set_book_rating('Злость и ярость', 7)
        assert collector.get_book_rating('Злость и ярость') is None

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Тайная опора')
        collector.add_book_in_favorites('Тайная опора')
        assert collector.get_list_of_favorites_books() == ['Тайная опора']

    def test_add_book_in_favorites_not_in_books_rating(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Преступление и наказание')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_books_with_specific_rating_get_books_with_rating_7_return_2_books(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_rating('Война и мир', 7)
        collector.add_new_book('Горе от ума')
        collector.set_book_rating('Горе от ума', 7)
        collector.add_new_book('Евгений Онегин')
        specific_books = collector.get_books_with_specific_rating(7)
        assert len(specific_books) == 2 and 'Война и мир' in specific_books and 'Горе от ума' in specific_books

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites('Тринадцатая сказка')
        assert len(collector.get_list_of_favorites_books()) == 0