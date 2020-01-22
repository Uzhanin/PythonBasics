n = (input('Введите целое положительное число: '))
print('*' * 40)
n_len = len(n)
n = int(n)
i = 1
rest = n
biggest = 0
while i <= n_len:
    new_biggest = rest // 10 ** (n_len - i)
    if new_biggest > biggest:
        biggest = new_biggest
    rest = rest % 10 ** (n_len - i)
    i += 1
print(f'Наибольшая цифра в числе {n} это {biggest}')
