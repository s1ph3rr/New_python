a = int(input("Введите результат пробежки первого дня в км>> "))
b = int(input("Введите результат которого хотите достичь в км>> "))
result_days = 1
result_km = a
while result_km < b:
    a = a + 0.1 * a
    result_days += 1
    result_km = result_km + a
print(f"Вы достигните желаемых показателей на %.d день" % result_days)