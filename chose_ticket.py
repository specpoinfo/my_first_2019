def sum_of_curent_numbers(number:int, sum=0):
    number = str(number)
    if len(number) == 1:
        return number[0]
    for n in number:
        sum += int(n)
    return sum_of_curent_numbers(sum)

def protection_only_int(x):
    '''This function trying to change type of x to int
       If we can returns True
       Else return False
    '''
    try:
        x = int(x)
    except:
        print("Можно вводить только цифры!")
        return False
    return True

if __name__ == "__main__":
    x = [] #all_tickets
    n = 1 #count_of_current_ticket
    key_input = input("Введите номер билета №" + str(n)+ ": ")
    
    while key_input != '0':
        if protection_only_int(key_input):    
            x.append(key_input)
            n += 1
        key_input = input("Введите номер билета №"+ str(n)+ ": ")

    for i in range(len(x)):
        print(str(i + 1),"Билет №" + x[i], "Сумма цифр:" + sum_of_curent_numbers(x[i]))

