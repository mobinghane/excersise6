import numpy as nup
n, m = map(int, input().split())
i = 0
lst_matrix1 = []
while i < n*m:
    lst_1 = list(map(int, input().split()))
    lst_matrix1.append(lst_1)
    i += 1
lst_2 = []
lst_matrix2 = []
for i in range(n):
    lst_matrix2.append(lst_matrix1[0:m])
    for j in range(m): lst_matrix1.pop(0)
lst_det = []
dict_zarb = dict()
for index, array1 in enumerate(lst_matrix2):
    if index == len(lst_matrix2)-1:
        break
    while index < len(lst_matrix2)-1:
        a = nup.array(array1)
        b = nup.array(lst_matrix2[index + 1])
        zarb = a.dot(b)
        dict_zarb[nup.linalg.det(zarb.tolist())] = [a, b]
        index += 1
lst = [key for key in dict_zarb.keys()]
max_zarb_matrix = dict_zarb[max(lst)]
if nup.linalg.det(max_zarb_matrix[0]) > nup.linalg.det(max_zarb_matrix[1]):
    final_matrix = max_zarb_matrix[0].dot(max_zarb_matrix[1])
else:
    final_matrix = max_zarb_matrix[1].dot(max_zarb_matrix[0])
inv_final_matrix = nup.linalg.inv(final_matrix).tolist()
for row in inv_final_matrix:
    row = [round(num, 3) for num in row]
    print(' '.join(map(str, row)))
