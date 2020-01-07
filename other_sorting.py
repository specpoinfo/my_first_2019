def merge(A:list, B:list):
    '''Функция создает новый список в который будет передавать меньшее число из двух списков
       тем самым создавая возвращая один отсортированный список
    '''
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C

def merge_sort(A):
    '''Сортировка слиянием
    '''
    if len(A) <= 1:
        return
    middle = len(A)//2
    L = [A[i] for i in range(middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C [i]





if __name__ == "__main__":
    listik = [1,5,5,3,5,3,6,4,7,8,5,6,3,8,6,4,1,4,3,1,5,4,3,2,5,6,7,8,9]
    merge_sort(listik)
    print(listik)