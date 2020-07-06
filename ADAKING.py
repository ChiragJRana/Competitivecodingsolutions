from sys import stdin, stdout
def function(val):

# for T in range(int(input())):
    board = [['.' for i in range(8)] for j in range(8)]
    board[0][0] = 'O'
    # val = int(input())
    remainder = val % 8
    quotient = int(val / 8)
    # print(f'value: {val}, quotient: {quotient}, remainder:{remainder}')
    for j in range(remainder, 8):
        if quotient != 8:
            board[quotient][j] = 'X'
        else:
            break
    if quotient < 7:
        board[quotient+1] = ['X'] * 8
    for item in board:
        print(''.join(item))

if __name__ == '__main__':
    for i in range(1,65):
        function(i)
    