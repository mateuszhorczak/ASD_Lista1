# Kod pisany w jezyku python w wersji 3.10.7 w PyCharm'ie na systemie linux

# Wariant A:

# WP: n, m – liczby naturalne takie, ze n, m <= 10000 i m <= n
# WK: wartosc symbolu Newtona dla danego n i m

def factorial_iterative(x):  # Silnia iteracyjna wykorzystywana przy liczeniu
    if x == 0:
        return 1
    result = 1
    for j in range(1, x + 1):
        result *= j
    return result


def newton_symbol_iterative(m, n):  # symbol newtona liczony iteracyjnie w oparciu o silnie iteracyjna
    return factorial_iterative(m) / (factorial_iterative(n) * factorial_iterative(m - n))


def newton_symbol_recursive(m, n):  # symbol newtona liczony przez rekurencje
    if n > m:
        return 0
    if m == 0 or m == n:
        return 1
    if 0 < n < m:
        return newton_symbol_recursive(m - 1, n - 1) + newton_symbol_recursive(m - 1, n)
    else:
        return 1


if __name__ == '__main__':

    stdin1 = int(input())
    stdin2 = int(input())

    print(newton_symbol_iterative(stdin1, stdin2))
    print(newton_symbol_recursive(stdin1, stdin2))
