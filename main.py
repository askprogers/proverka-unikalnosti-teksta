def get_ngrams(text, n):
    """
    Функция для получения списка n-грамм из текста.
    """
    # Разбиваем текст на слова
    words = text.split()
    
    # Формируем список n-грамм
    ngrams = [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]
    
    return ngrams

def calculate_uniqueness_percentage(original_text, rewrite_text, n):
    """
    Функция для вычисления процента уникальности рерайта относительно исходного текста по n-граммам.
    """
    # Получаем n-граммы из обоих текстов
    original_ngrams = set(get_ngrams(original_text, n))
    rewrite_ngrams = set(get_ngrams(rewrite_text, n))
    
    # Вычисляем количество уникальных n-грамм в рерайте
    unique_ngrams = rewrite_ngrams - original_ngrams
    
    # Процент уникальности - отношение количества уникальных n-грамм к общему количеству n-грамм в рерайте, умноженное на 100
    uniqueness_percentage = (len(unique_ngrams) / len(rewrite_ngrams) * 100) if rewrite_ngrams else 0
    
    return uniqueness_percentage

# Пример использования
original_text = "Это пример исходного текста для проверки уникальности."
rewrite_text = "Это исходного для проверки уникальности."

n = 3
uniqueness = calculate_uniqueness_percentage(original_text, rewrite_text, n)

print(f"Процент уникальности рерайта относительно исходного текста: {uniqueness:.2f}%")
