import timeit
from kmp import kmp_search
from bm import boyer_moore_search
from rk import rabin_karp_search

f = open("стаття 1.txt", "r", encoding='utf8')
article1 = f.read()
f = open("стаття 2.txt", "r", encoding='utf8')
article2 = f.read()

substring1 = "національний технічний університет"
substring2 = "I killed him, yeah."

print(f"Пошук алгоритмом Кнута-Морріса-Пратта в статті 1 стрічки '{substring1   :34}' зайняв {timeit.timeit(lambda: kmp_search        (article1, substring1), number=1):.8f} секунд.")
print(f"Пошук алгоритмом Кнута-Морріса-Пратта в статті 2 стрічки '{substring1   :34}' зайняв {timeit.timeit(lambda: kmp_search        (article2, substring1), number=1):.8f} секунд.")
print(f"Пошук алгоритмом Боєра-Мура           в статті 1 стрічки '{substring1   :34}' зайняв {timeit.timeit(lambda: boyer_moore_search(article1, substring1), number=1):.8f} секунд.")
print(f"Пошук алгоритмом Боєра-Мура           в статті 2 стрічки '{substring1   :34}' зайняв {timeit.timeit(lambda: boyer_moore_search(article2, substring1), number=1):.8f} секунд.")
print(f"Пошук алгоритмом Рабіна-Карпа         в статті 1 стрічки '{substring1   :34}' зайняв {timeit.timeit(lambda: rabin_karp_search (article1, substring1), number=1):.8f} секунд.")
print(f"Пошук алгоритмом Рабіна-Карпа         в статті 2 стрічки '{substring1   :34}' зайняв {timeit.timeit(lambda: rabin_karp_search (article2, substring1), number=1):.8f} секунд.")
print(f"Пошук алгоритмом Кнута-Морріса-Пратта в статті 1 стрічки '{substring2+"'":35} зайняв {timeit.timeit(lambda: kmp_search        (article1, substring2), number=1):.8f} секунд.")
print(f"Пошук алгоритмом Кнута-Морріса-Пратта в статті 2 стрічки '{substring2+"'":35} зайняв {timeit.timeit(lambda: kmp_search        (article2, substring2), number=1):.8f} секунд.")
print(f"Пошук алгоритмом Боєра-Мура           в статті 1 стрічки '{substring2+"'":35} зайняв {timeit.timeit(lambda: boyer_moore_search(article1, substring2), number=1):.8f} секунд.")
print(f"Пошук алгоритмом Боєра-Мура           в статті 2 стрічки '{substring2+"'":35} зайняв {timeit.timeit(lambda: boyer_moore_search(article2, substring2), number=1):.8f} секунд.")
print(f"Пошук алгоритмом Рабіна-Карпа         в статті 1 стрічки '{substring2+"'":35} зайняв {timeit.timeit(lambda: rabin_karp_search (article1, substring2), number=1):.8f} секунд.")
print(f"Пошук алгоритмом Рабіна-Карпа         в статті 2 стрічки '{substring2+"'":35} зайняв {timeit.timeit(lambda: rabin_karp_search (article2, substring2), number=1):.8f} секунд.")
