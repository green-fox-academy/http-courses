def rotate_left(matrix):
    output = []
    rowLength = len(matrix[0])
    for i in range(rowLength)[::-1]:
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        output.append(new_row)

    return output

left = rotate_left([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(left)