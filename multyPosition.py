# 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на введенных пользователем позициях.

N = int(input('Введите число: '))

pozition1 = int(input('Введите позицию первого элемента: ')) 
pozition2 = int(input('Введите позицию второго элемента: '))
numbers = list(range(-N, N))
print(numbers)
countPozition = N * 2
print(f'Всего позиций в списке {countPozition}, произведение элементов на заданных позициях = {numbers[pozition1 - 1] * numbers[pozition2 - 1]}')
# Позиции взяла, начинающиеся с одного, в отличие от индекса.
