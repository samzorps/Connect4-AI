#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 21:11:49 2019

@author: samzorpette

ps9pr1- Problem Set 9, Problem 1
"""

class Board:
    def __init__(self, height, width):
        """ Initializes objects of the board class.
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]
        
    def __repr__(self):
        """ Returns a string representation for a Board object.
        """
        s = ''         # begin with an empty string
    
        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row
    
        s += ('-' * (self.width*2 + 1)) + '\n '
        
        for n in range(self.width):
            s+= str((n%10)) + ' '

        return s
    
    def add_checker(self, checker, col):
        """ adds a checker to a board in column col
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        
        r = 0
        while r != self.height - 1 and self.slots[r+1][col]== ' ':
            r+=1
            
        self.slots[r][col]= checker
        
    def reset(self):
        """resets board"""
        self.slots = [[' '] * self.width for row in range(self.height)]
        
    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
        
    def can_add_to(self, col):
        if col in range(self.width) and self.slots[0][col] == ' ' :
            return True
        return False
    
    def is_full(self):
        l = [self.slots[0][x]== ' ' for x in range(self.width)]
        if True in l:
            return False
        return True
    
    def remove_checker(self, col):
        r = 0
        while r != self.height - 1 and self.slots[r][col]== ' ':
            r+=1
            
        self.slots[r][col]= ' '
        
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                    self.slots[row][col + 1] == checker and \
                    self.slots[row][col + 2] == checker and \
                    self.slots[row][col + 3] == checker:
                        return True

        # if we make it here, there were no horizontal wins
        return False

    def is_vertical_win(self, checker):
        """ checks for vertical win"""
        for row in range(self.height-3):
            for col in range(self.width):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col] == checker and \
                    self.slots[row + 2][col] == checker and \
                    self.slots[row + 3][col] == checker:
                        return True
        return False
    
    def is_up_diag_win(self, checker):
        """ checks for vertical win"""
        for row in range(3, self.height):
            for col in range(self.width-3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                    self.slots[row - 1][col + 1] == checker and \
                    self.slots[row - 2][col + 2] == checker and \
                    self.slots[row - 3][col + 3] == checker:
                        return True
        return False
    
    def is_down_diag_win(self, checker):
        """ checks for vertical win"""
        for row in range(self.height-3):
            for col in range(self.width-3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col + 1] == checker and \
                    self.slots[row + 2][col + 2] == checker and \
                    self.slots[row + 3][col + 3] == checker:
                        return True
        return False
        
    def is_win_for(self, checker):
        """checks if any player has one"""
        assert(checker=='X' or checker=='O')
        b = [self.is_horizontal_win(checker), \
             self.is_vertical_win(checker), \
             self.is_up_diag_win(checker), \
             self.is_down_diag_win(checker) ]
        
        if True in b:
            return True
        return False
        