# simple knapsack problem
def knapsack(items, capacity):
    '''
    items: list of tuples (weight, value)
    capacity: int
    '''
    # create a matrix to store the values
    matrix = [[0 for x in range(capacity + 1)] for y in range(len(items) + 1)]
    # fill the first row and column
    for i in range(len(items) + 1):
        matrix[i][0] = 0
    for j in range(capacity + 1):
        matrix[0][j] = 0
    # fill the rest of the matrix
    for i in range(1, len(items) + 1):
        for j in range(1, capacity + 1):
            if items[i - 1][0] <= j:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i - 1][j - items[i - 1][0]] + items[i - 1][1])
            else:
                matrix[i][j] = matrix[i - 1][j]
    return matrix[len(items)][capacity]


def main():
    items = [(2, 3), (3, 4), (4, 5)]
    capacity = 5
    print(knapsack(items, capacity))


if __name__ == '__main__':
    main()
