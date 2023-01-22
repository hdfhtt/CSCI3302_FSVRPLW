"""
    CSCI 3302 Data Structures & Algorithms 2 Modified Algorithm
    Name        : Muhammad Hadif Bin Mohd Hatta (hdfhtt)
    Matric no   : 2114589
    Language/IDE: Python 3.9 / PyCharm 2022.3
    Date        : 23/01/2023
"""


# Coin-Row (basic algorithm)
def coin_row(c, n):
    # base case
    if n == 0:
        return 0

    if n == 1:
        return c[0]

    # max { F(n - 1), Cn + F(n - 2) }
    return max(coin_row(c, n - 1), c[n - 1] + coin_row(c, n - 2))


if __name__ == '__main__':
    coins = [5, 1, 2, 10, 6, 2]  # sample inputs
    print("Coin-row: ", coin_row(coins, len(coins)))

