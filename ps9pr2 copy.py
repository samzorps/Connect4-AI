#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below

class Player:
    def __init__(self, checker):
         assert(checker== 'X' or checker== 'O')
         self.checker=checker
         self.num_moves=0
    
    def __repr__(self):
        return 'Player ' + self.checker
    
    def opponent_checker(self):
        if self.checker== 'O' :
            return 'X'
        return 'O'
    
    def next_move(self, b):
        while True:
            c= int( input('Enter a column: ') )
            if b.can_add_to(c)== True:
                break
            else:
                print('invalid column')
        self.num_moves+=1
        return c