# qa_python
    
1. **test_add_new_book_add_two_books** - проверка, что добавились именно 2 книги;
2. **test_add_new_book_duplicated_book** - проверка, что две одиаковые книги не добавятся в коллекцию;
3. **test_set_book_rating_book_is_apsent** - проверка, что нельзя выставить рейтинг книге, которой нет в коллекции;
4. **test_set_book_rating_rating_less_than_one** - проверка, что нельзя выставить рейтинг меньше 1;
5. **test_set_book_rating_more_than_10** - проверка, что нельзя выставить рейтинг больше 10;
6. **test_set_book_rating_not_added_book** - проверка, что у недобавленной книги нет рейтинга;
7. **test_add_book_in_favorites** = проверка, что книга добавилась в избранное;
8. **test_add_book_in_favorites_not_in_books_rating** - проверка, что если книга не в списке рейтингов, то она не добавится в избранное;
9. **test_delete_book_from_favorites** - проверка, что книга удаляется из избранного.
10. **test_get_books_with_specific_rating_get_books_with_rating_7_return_2_books** - проверка, что книги с одинаковым рейтингом попадут в список со специфическим рейтингом
