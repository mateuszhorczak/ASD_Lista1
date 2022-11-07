# Kod pisany w jezyku python w wersji 3.10.7 w PyCharm'ie na systemie linux

# Wariant C:

# WP: n – liczby naturalne takie, ze 0 <= n <= 10000
# WK: Liczba Catalana dla wartosci n

def factorial_iterative(x):  # Silnia iteracyjna
    if x == 0:
        return 1
    result = 1
    for j in range(1, x + 1):
        result *= j
    return result


def catalan_number_recursive(n):  # liczba catalana wyliczana przez rekurencje
    if n < 2:
        return 1
    result = 0
    for k in range(n):
        result += catalan_number_recursive(k) * catalan_number_recursive(n - 1 - k)
    return result


def catalan_number_iterative(n):  # liczba catalana wyliczana iteracyjnie przy użyciu silni
    return factorial_iterative(2 * n) / (factorial_iterative(n + 1) * factorial_iterative(n))


if __name__ == '__main__':
    stdin = int(input())
    print(catalan_number_iterative(stdin))
    print(catalan_number_recursive(stdin))
