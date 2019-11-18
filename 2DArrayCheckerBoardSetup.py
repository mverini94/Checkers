rows, cols = (8, 8)

init1 = [0, 1, 2, 5, 6, 7]
init2 = [0, 2, 4, 6]
init3 = [1, 3, 5, 7]

arr = [["." for i in range(cols)] for j in range(rows)]

# This is going to initialize our checkerboard

for i in init1:
    if i < 4:
        if i % 2 == 0:
            for j in init2:
                arr[i][j] = "b"

        else:
            for j in init3:
                arr[i][j] = "b"

    if i > 4:
        if i % 2 == 0:
            for j in init2:
                arr[i][j] = "r"

        else:
            for j in init3:
                arr[i][j] = "r"


for row in arr:
    print(row)
