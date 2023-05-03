#!/usr/bin/env python
# coding: utf-8

# In[ ]:


scores = {0: ' ', 1: ' ' , 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' '}
winner = 'no'
turn_num = 1

# updating tic tac toe board
def score_board():
    print('''
     
     |     |    
  ''' + scores[0] + '''  |  ''' + scores[1] + '''  |  ''' + scores[2] +   '''
 ____|_____|____
     |     |    
  ''' + scores[3] + '  |  ' + scores[4] + '  |  ' + scores[5] + 
'''
 ____|_____|____''' +
'''
     |     |    '''
''' 
  ''' + scores[6] + '''  |  ''' + scores[7] + '''  |  ''' + scores[8] +'''
     |     |''')
    
# winning conditions
def x_winner():
    global winner
    if scores[0] == 'X' and scores[1] == 'X' and scores[2] == 'X':
        print('You Win Player X!')
        winner = 'yes'
    elif scores[3] == 'X' and scores[4] == 'X' and scores[5] == 'X':
        print('You Win Player X!') 
        winner = 'yes'
    elif scores[6] == 'X' and scores[7] == 'X' and scores[8] == 'X':
        print('You Win Player X!') 
        winner = 'yes'
    elif scores[0] == 'X' and scores[3] == 'X' and scores[6] == 'X':
        print('You Win Player X!')
        winner = 'yes'
    elif scores[1] == 'X' and scores[4] == 'X' and scores[7] == 'X':
        print('You Win Player X!')  
        winner = 'yes'
    elif scores[2] == 'X' and scores[5] == 'X' and scores[8] == 'X':
        print('You Win Player X!') 
        winner = 'yes'
    elif scores[0] == 'X' and scores[4] == 'X' and scores[8] == 'X':
        print('You Win Player X!')    
        winner = 'yes'
    elif scores[6] == 'X' and scores[4] == 'X' and scores[2] == 'X':
        print('You Win Player X!')  
        winner = 'yes'
    else:
        winner = 'no'

def o_winner():
    global winner
    if scores[0] == 'O' and scores[1] == 'O' and scores[2] == 'O':
        print('You Win Player O!')
        winner = 'yes'
    elif scores[3] == 'O' and scores[4] == 'O' and scores[5] == 'O':
        print('You Win Player O!') 
        winner = 'yes'
    elif scores[6] == 'O' and scores[7] == 'O' and scores[8] == 'O':
        print('You Win Player O!') 
        winner = 'yes'
    elif scores[0] == 'O' and scores[3] == 'O' and scores[6] == 'O':
        print('You Win Player O!')
        winner = 'yes'
    elif scores[1] == 'O' and scores[4] == 'O' and scores[7] == 'O':
        print('You Win Player O!')  
        winner = 'yes'
    elif scores[2] == 'O' and scores[5] == 'O' and scores[8] == 'O':
        print('You Win Player O!')   
        winner = 'yes'
    elif scores[0] == 'O' and scores[4] == 'O' and scores[8] == 'O':
        print('You Win Player O!')  
        winner = 'yes'
    elif scores[6] == 'O' and scores[4] == 'O' and scores[2] == 'O':
        print('You Win Player O!') 
        winner = 'yes'
    else:
        winner = 'no'

# turn conditions
def x_turn():
    move = input("Enter your move X player: ")
    while move not in ['top left', 'top middle', 'top right', 'middle left', 'middle', 'middle middle', 'middle right', 'bottom left', 'bottom middle', 'bottom right']:
        print('Invalid move! Please say top/middle/bottom and left/middle/right')
        move = input("Enter your move X player: ")    

    index = 9
    if move == 'top left' and scores[0] == ' ':
        index = 0
    elif move == 'top middle' and scores[1] == ' ':
        index = 1
    elif move == 'top right' and scores[2] == ' ':
        index = 2
    elif move == 'middle left' and scores[3] == ' ':
        index = 3
    elif move == 'middle' and scores[4] == ' ':
        index = 4
    elif move == 'middle middle' and scores[4] == ' ':
        index = 4
    elif move == 'middle right' and scores[5] == ' ':
        index = 5
    elif move == 'bottom left' and scores[6] == ' ':
        index = 6
    elif move == 'bottom middle' and scores[7] == ' ':
        index = 7
    elif move == 'bottom right' and scores[8] == ' ':
        index = 8    
  
    if index != 9:
        scores[index] = 'X'
    else:
        print('Space is already occupied! Pick again!')
        x_turn()
        
    x_winner()

def o_turn():
    move = input("Enter your move O player: ")
    while move not in ['top left', 'top middle', 'top right', 'middle left', 'middle', 'middle middle', 'middle right', 'bottom left', 'bottom middle', 'bottom right']:
        print('Invalid move! Please say top/middle/bottom and left/middle/right')
        move = input("Enter your move O player: ")
        
    index = 9
    if move == 'top left' and scores[0] == ' ':
        index = 0
    elif move == 'top middle' and scores[1] == ' ':
        index = 1
    elif move == 'top right' and scores[2] == ' ':
        index = 2
    elif move == 'middle left' and scores[3] == ' ':
        index = 3
    elif move == 'middle' and scores[4] == ' ':
        index = 4
    elif move == 'middle middle' and scores[4] == ' ':
        index = 4
    elif move == 'middle right' and scores[5] == ' ':
        index = 5
    elif move == 'bottom left' and scores[6] == ' ':
        index = 6
    elif move == 'bottom middle' and scores[7] == ' ':
        index = 7
    elif move == 'bottom right' and scores[8] == ' ':
        index = 8
        
    if index != 9:
        scores[index] = 'O'
    else:
        print('Space is already occupied! Pick again!')
        o_turn()
        
    o_winner()

while turn_num < 10:                  
    if winner == 'no':
        if turn_num % 2 > 0:
            score_board()
            x_turn()
            turn_num += 1
        elif turn_num % 2 == 0:
            score_board()
            o_turn()
            turn_num += 1
    elif winner != 'no':
        score_board()
        exit()

if turn_num == 10:
    print("It's a tie!")
    exit()
    


# In[ ]:




