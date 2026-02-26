"""
ЗАДАЧА: Анализ чатов пользователей

Даны сообщения в чате. Каждое сообщение представлено словарём
со следующими ключами:
- "user"      : имя пользователя (строка)
- "text"      : текст сообщения (строка)
- "timestamp" : время сообщения (целое число, возрастает не строго)

Пример входных данных:
messages = [
    {"user": "Алиса", "text": "привет здравствуй",     "timestamp": 1},
    {"user": "Боб",   "text": "здравствуй",            "timestamp": 2},
    {"user": "Алиса", "text": "как дела у тебя",       "timestamp": 3},
    {"user": "Боб",   "text": "привет Алиса",          "timestamp": 4},
    {"user": "Алиса", "text": "привет привет здравствуй", "timestamp": 10},
    {"user": "Боб",   "text": "пока",                  "timestamp": 20},
]

НЕОБХОДИМО РЕАЛИЗОВАТЬ:

1. Посчитать количество сообщений каждого пользователя.
   Результат сохранить в словарь вида:
   {
       "Алиса": 3,
       "Боб": 2
   }

2. Для каждого пользователя:
   2.1 Найти множество уникальных слов, которые он использовал
       (слова разделяются методом split()).
   2.2 Найти самое частое слово пользователя.
       Если самых частых слов несколько — можно выбрать любое.

3. Найти пользователя с самым большим словарным запасом,
   где словарный запас — это количество уникальных слов,
   использованных пользователем.

4. Найти множество слов, которые использовали ВСЕ пользователи
   (пересечение множеств слов пользователей).

5. Для каждого пользователя определить максимальный перерыв
   между его сообщениями:
   - перерыв = разница между timestamp текущего и предыдущего сообщения
   - найти пользователя с самым большим таким перерывом
"""


messages = [
    {"user": "Алиса", "text": "привет здравствуй",     "timestamp": 1},
    {"user": "Боб",   "text": "здравствуй",            "timestamp": 2},
    {"user": "Алиса", "text": "как дела у тебя",       "timestamp": 3},
    {"user": "Боб",   "text": "привет Алиса",          "timestamp": 4},
    {"user": "Алиса", "text": "привет привет здравствуй", "timestamp": 10},
    {"user": "Боб",   "text": "пока",                  "timestamp": 20},
]

messages_count = {}
user_words = {}
last_timestamp = {}
max_time = {}
for message in messages:
    user = message["user"]
    messages_count[user] = messages_count.get(user, 0) +1
    words = message["text"].split()

    if user not in user_words:
        user_words[user] = set()
    user_words[user].update(words)

    timestamp = message["timestamp"]
    if user in last_timestamp:
        gap = timestamp - last_timestamp[user]
        if gap > max_time.get(user, 0):
            max_time[user] = gap
        else:
            max_time[user] = 0 
        last_timestamp[user] = timestamp


most_freq_words = {}
for user_name in user_words:
    freq = {}
    for message in messages:
        if user_name == message["user"]:
            for word in message["text"].split():
                freq[word] = freq.get(word, 0) + 1
    max_word = None
    max_count = 0
    for word, count in freq.items():
        if count > max_count:
            max_word = word
            max_count = count
    most_freq_words[user_name] = max_word

user_vocabularies = None
max_unique_words_count = 0 
for user, word_set in user_words.items():
    unique_count = len(word_set)
    if unique_count > max_unique_words_count:
        max_unique_words_count = unique_count
        user_vocabularies = user

common_words = set.intersection(*user_words.values())


print(user_words)
print(messages_count)
print(most_freq_words)
print(user_vocabularies)
print(common_words)