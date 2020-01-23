print('Переводим время в секундах в формат чч:мм:сс')
user_time = int(input('Введите время в секундах: '))
if user_time // 86400 > 0:
    print('Да здесь же больше одних суток! Сутки при переводе не будут учтены')
user_time = user_time % 86400
hours = user_time // 3600
min = (user_time % 3600) // 60
sec = (user_time % 3600) % 60
print(f'{user_time} секунд в формате чч:мм:сс это {hours:02}:{min:02}:{sec:02}')