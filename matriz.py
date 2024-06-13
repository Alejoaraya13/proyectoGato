def findall(element, matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                result.append((i,j))
    return result

matrix = [["x","x","0"],["v","v","v"],["0","0","x"]]
print(matrix[0], "\n", matrix[1], "\n", matrix[2])
print("Diga el elemento que quiere encontrar:")
element = input()
print(findall(element, matrix))
