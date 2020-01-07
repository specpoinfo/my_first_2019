
def gen_bin(M, prefix=''):
    if M == 0:
        print(prefix)
        return
    for digit in '0', '1':
        gen_bin(M-1, prefix+digit)
    



def generate_numbers(N:int, M:int, prefix=None):
    '''Генерирует все числа (с лидирующими незначащими нулями) в N-ричной
    системе счисления (N <= 10)
    длины M
    '''
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()

def find(number, A):
    '''Ищет number в A и возвращает True, если такой есть
       False - если такого нет
    '''
    for x in A:
        if number == x:
            return True
    return False

def generate_permutations(N:int, M:int=-1, prefix=None):
    '''Генерация всех перестановок N чисел в M позициях,
       с префиксом prefix
    '''
    M = N if M == -1 else M # по умолчанию N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        print(*prefix, sep='', end=' ')
        return
    for number in range(1, N+1):
        if find(number, prefix): 
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()



if __name__ == "__main__":
    N = 3 #основание системы счисления
    M = 3 #длина списка
    #generate_numbers(M,N)
    #gen_bin(5)
    generate_permutations(5)
