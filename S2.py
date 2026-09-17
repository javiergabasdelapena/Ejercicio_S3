
def insertion_sort(lista):
    lista=[64, 34, 25, 12, 22, 11, 90]
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista
sorted_list = insertion_sort([])
print(sorted_list)