# Бесплатная программа проверки уникальности текста
Для проверки уникальности текста по шинглам (n-граммам, на основе этого работают все сервисы проверки уникальности) пользуйтесь моей Python программой, которая будет выполнять следующие шаги:

-Разбивать оба текста на шинглы (n-граммы).

-Сравнивать наборы шинглов.

-Вычислять коэффициент уникальности рерайта относительно исходного текста в процентах.

Пример программы в файле main.py, скачиваете, где original_text - вставляете исходный текст, а rewrite_text - сюда вставляете рерайт и запускаете, программа покажет уникальность между текстами в процентах.

Объяснение:

-Функция get_ngrams разбивает текст на слова и формирует из них n-граммы.

-Функция calculate_uniqueness вычисляет множество n-грамм для обоих текстов и затем определяет уникальные n-граммы рерайта, которых нет в исходном тексте. На основе этого вычисляется коэффициент уникальности.

В примере использования задаются исходный и рерайт тексты, а также значение n для n-грамм (в данном случае 3 - по умолчанию).

Вы можете изменить значение n, чтобы использовать 2-граммы или любое другое количество слов в n-грамме. Бесплатная замена сервисам проверки уникальности. В режиме онлайн также можно <a href="https://sravnenie-online.ru/">проверить тексты на схожесть</a>.
