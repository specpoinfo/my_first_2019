def sum_of_curent_numbers(number):
    sum = 0
    number = list(str(number))
    if len(number)>1:
        for n in number:
            sum += int(n)
        return sum_of_curent_numbers(sum)
    else:
        return number[0]




x = []
n = 1
key_input = input("Введите номер билета №" + str(n)+ ": ")
while key_input != '0':
    x.append(key_input)
    n += 1
    key_input = input("Введите номер билета №"+ str(n)+ ": ")

for i in range(len(x)):
    print(str(i + 1),"Билет №" + x[i], "Сумма цифр:" + sum_of_curent_numbers(x[i]))

