# mashiqlar5_2511
# 1 - masala
sozlar = ["apple", "banana", "cherry", "avocado", "grape", "strawberry"]

natija = list(filter(lambda w: len(w) > 5 and "a" in w, sozlar))

# 2 - masala
roy = [3, 126, 4.21, 701, 99.9, 1001, 100, 7]

natija = list(filter(lambda x: isinstance(x, int) and 100 <= x <= 999, roy))

# 3 - masala
sites = ["google.com", "example.uz", "test.uz", "mail.ru"]

natija = list(filter(lambda s: s.endswith(".uz"), sites))
