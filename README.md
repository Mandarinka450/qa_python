# qa_python

**test_add_new_book_added_book_has_no_genre()** - данный тест проверяет, что у только что добавленной книги отсутствует жанр (следует из условия задания).

**test_add_new_book_get_name_new_added_book_from_books_genre()** - данный тест проверяет, что в словарь действительно добавилась книга с нужным названием.

**test_set_book_genre_new_book_has_genre()** - данный тест является параметризованным, и написаны тестовые данные в виде пары Название книги: жанр.
Тест проверяет, что новой книге присвоился конкретный жанр, проверяем каждый жанр.

**test_get_book_genre_book_has_genre_is_comedy()** - тест проверяет, что у полученной книги "Зеленая книга" действительно жанр "Комедии".

**test_get_books_genre_add_book_and_books_genre_not_empty()** - тест проверяет, что при добавлении книги словарь books_genre
не является пустым, так как он содержит уже одну книгу.

**test_add_book_in_favorites_get_name_added_book_from_favorites()** - тест проверяет, что книга с нужным названием действительно добавлена в список Избранного.
Проверяем название только что добавленной книги в список, книга с определенным названием существует в этом списке.

**test_delete_book_from_favorites_is_empty_after_delete_book()** - тест проверяет, что после добавления и удаления книги список favorites стал пустым.

**test_get_list_of_favorites_books_is_not_empty_after_added_books()** - тест проверяет, что если добавить в список favorites книги, то он не должен быть пустым.

**test_get_books_with_specific_genre_get_list_of_books_with_genre_is_horror()** - тест проверяет длину списка книг по жанру "Ужасы", 
если добавили 3 книги, значит, длина должна быть равной 2.

**test_get_books_for_children_add_three_books_len_equals_three()** - тест проверяет, что при добавлении трех книг длина списка станет равной 3.

