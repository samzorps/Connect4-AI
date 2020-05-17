#
# ps9pr4.py  (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four
#
"""Author: Sam Zorpette"""

import random
from connect_four import *

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """ initializes aiplayer with checker tiebreak lookahead
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)

        super().__init__(checker)

        self.checker = checker
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        s= 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        return s

    def max_score_column(self, scores):
        maxx = max(scores)

        indexes = [i for i in range(len(scores)) if scores[i]==maxx]

        if self.tiebreak == 'LEFT' :
            return indexes[0]
        elif self.tiebreak == 'RIGHT' :
            return indexes[-1]
        else:
            return random.choice(indexes)

    def scores_for(self, b):
        scores = [50] * b.width

        for i in range(b.width):
            if b.can_add_to(i) == False:
                scores[i] = -1
            elif b.is_win_for(self.checker) == True:
                scores[i] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[i] = 0
            elif self.lookahead==0:
                scores[i] = 50
            else:
                b.add_checker(self.checker, i)
                opp = AIPlayer(self.opponent_checker(), self.tiebreak, (self.lookahead -1))
                oppscores = opp.scores_for(b)

                oppmax = max(oppscores)

                if oppmax == -1:
                    scores[i] = -1
                else:
                    scores[i] = 100 - oppmax

                b.remove_checker(i)
        return scores

    def next_move(self, b):
        self.num_moves += 1
        return self.max_score_column(self.scores_for(b))
