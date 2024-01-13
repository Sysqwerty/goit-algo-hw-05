from rabin_karp_search import rabin_karp_search
from kmp_search import kmp_search
from boyer_moore_search import boyer_moore_search
from read_file_content import read_file_content
from timeit import timeit


def main():
    article_1_data = read_file_content('стаття 1.txt')
    article_2_data = read_file_content('стаття 2.txt')

    article_1_search = "сортування набору даних"
    article_2_search = "ключі потомку"

    rabin_time_1 = timeit(
        lambda: rabin_karp_search(article_1_data, article_1_search), number=10)
    kmp_time_1 = timeit(lambda: kmp_search(
        article_1_data, article_1_search), number=10)
    boyer_time_1 = timeit(
        lambda: boyer_moore_search(article_2_data, article_2_search), number=10)

    rabin_time_2 = timeit(
        lambda: rabin_karp_search(article_2_data, article_2_search), number=10)
    kmp_time_2 = timeit(lambda: kmp_search(
        article_1_data, article_1_search), number=10)
    boyer_time_2 = timeit(
        lambda: boyer_moore_search(article_2_data, article_2_search), number=10)

    print(f"{'| Алгоритм': <25} | {'Стаття 1': <10} | {'Стаття 2': <10} |")
    print(f"| {'-'*23} | {'-'*10} | {'-'*10} |")
    print(f"{'| Боєра-Мура': <25} | {boyer_time_1: <10.5f} | {boyer_time_2: <10.5f} |")
    print(f"{'| Кнута-Морріса-Пратта': <25} | {kmp_time_1: <10.5f} | {kmp_time_2: <10.5f} |")
    print(f"{'| Рабіна-Карпа': <25} | {rabin_time_1: <10.5f} | {rabin_time_2: <10.5f} |")


if __name__ == "__main__":
    main()
