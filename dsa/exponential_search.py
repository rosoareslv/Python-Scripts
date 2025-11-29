from binary_search import binary_search


# Mesma complexidade da binary search e utiliza esse algoritmo em sua busca, serve para arrays muito grande
# vai dobrando o index para achar o target, ou passar do valor para gerar uma substring, com o start do index /2 e o final index
# para ser jogado no algoritmo da binary search
def exponential_search(arr: list, target: int):
    if arr[0] == target:
        return 0
    i = 1
    while i < len(arr) and arr[i] < target:
        i *= 2
    if arr[i] == target:
        return i
    return binary_search(arr, target, i // 2, i if i < (len(arr) - 1) else len(arr) - 1)
