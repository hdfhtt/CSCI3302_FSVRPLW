"""
    CSCI 3302 Data Structures & Algorithms 2 Modified Algorithm
    Name        : Muhammad Hadif Bin Mohd Hatta (hdfhtt)
    Matric no   : 2114589
    Language/IDE: Python 3.9 / PyCharm 2022.3
    Date        : 23/01/2023
"""


# noinspection PyPep8Naming
def F(C, n):  # basic algorithm
    # base case
    if n == 0:
        return 0

    if n == 1:
        return C[0]

    # max { F(n - 1), Cn + F(n - 2) }
    return max(F(C, n - 1), C[n - 1] + F(C, n - 2))


if __name__ == '__main__':
    coins = [5, 1, 2, 10, 6, 2]  # sample input for basic algorithm
    print("Coin-row: ", F(coins, len(coins)))

