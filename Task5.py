revenue = float(input('Выручка, млн. руб.: ')) #выручка
costs = float(input('Издержки, млн. руб: ')) #издержки
delta = revenue - costs
if delta > 0:
    print(f'Прибыль компании составила: {delta} млн. руб.')
    print(f'Рентабельность составила: {delta / revenue:.2} ')
    staff = int(input('Укажите количество сотрудников: '))
    print(f'Прибыль в расчете на одного сотрудника составила: {delta / staff} млн. руб.')

elif delta < 0:
    print(f'Убытки компании составили: {-delta} млн. руб.')