"""Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
a) до минуты: <s> сек;
b) до часа: <m> мин <s> сек;
c) до суток: <h> час <m> мин <s> сек;
d) * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
	Примеры:
duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек
duration = 400153
4 дн 15 час 9 мин 13 сек


Примечание: можете проверить себя здесь, подумайте,можно ли использовать цикл для 
проверки работы кода сразу для нескольких значений продолжительности, будет ли тут полезен список?
"""

duration = int(input("Введите целое положительное число: "))

minute = 60
hour = minute * 60
day = hour * 24

duration_seconds = duration % minute
duration_minutes = duration % day % hour // minute
duration_hour = duration % day // hour 
duration_day = duration // day

print(f"{duration_day} дн {duration_hour} час {duration_minutes} мин {duration_seconds} сек")


durations_list = [12345678, 54, 4000, 2100, 100100, 0]

for duration in durations_list:
        duration_seconds = duration % minute
        duration_minutes = duration % day % hour // minute
        duration_hour = duration % day // hour 
        duration_day = duration // day
        print(f"{duration_day} дн {duration_hour} час {duration_minutes} мин {duration_seconds} сек")

for duration in durations_list:
    if duration == 0:
        print(f"Временной отрезок равен 0")
    elif duration < minute:
        duration_seconds = duration
        print(f"{duration_seconds} сек")
    elif duration < hour:
        duration_seconds = duration % minute
        duration_minutes = duration % day % hour // minute
        print(f"{duration_minutes} мин {duration_seconds} сек")
    elif duration < day:
        duration_seconds = duration % minute
        duration_minutes = duration % day % hour // minute
        duration_hour = duration % day // hour
        print(f"{duration_hour} час {duration_minutes} мин {duration_seconds} сек")
    else:
        duration_seconds = duration % minute
        duration_minutes = duration % day % hour // minute
        duration_hour = duration % day // hour 
        duration_day = duration // day
        print(f"{duration_day} дн {duration_hour} час {duration_minutes} мин {duration_seconds} сек")
