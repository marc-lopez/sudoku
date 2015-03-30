'''
Created on Mar 30, 2015

@author: Marc

'''


def is_segment_valid(segment, expected_segment_sum):
    if len(segment) != len(set(segment)) or sum(segment) != expected_segment_sum:
        return False
    return True

def is_valid(board):
    board_size = len(board)
    expected_segment_sum = sum(range(1, 10))
    row = []
    col = []
    square = []
    for i in range(board_size):
        for j in range(board_size):
            row.append(board[i][j])
            col.append(board[j][i])
            square.append(board[((i / 3) * 3) + (j / 3)][((i % 3) * 3) + (j % 3)])
        
        if not all([is_segment_valid(segment, expected_segment_sum) for segment in [row, col, square]]):
            return False
        
        row = []
        col = []
        square = []
        
    return True

if __name__ == '__main__':
    board = []
    
    with open('input.txt') as infile:
        for line in infile:
            board.append(map(int, line.strip().split(' ')))
    
    print is_valid(board)
