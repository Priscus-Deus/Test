def min_operations(n):
    # Создаем массив для хранения количества операций
    dp = [0] * (n + 1)
    # Список для хранения последовательности операций
    sequence = [[] for _ in range(n + 1)]

    for i in range(2, n + 1):
        # Для каждого числа i ищем минимальное количество операций
        # и последовательность операций, приводящих к i
        dp[i] = dp[i - 1] + 1
        sequence[i] = sequence[i - 1] + [3]  # Операция 3: вычитание 1

        if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1
            sequence[i] = sequence[i // 2] + [2]  # Операция 2: деление на 2

        if i % 5 == 0 and dp[i // 5] + 1 < dp[i]:
            dp[i] = dp[i // 5] + 1
            sequence[i] = sequence[i // 5] + [1]  # Операция 1: деление на 5

    # Возвращаем минимальное количество операций и последовательность операций
    return dp[n], sequence[n]


    

# Пример использования
n = 6
dp, sequence = min_operations(n)
print(dp)
print(*list(reversed(sequence)))
