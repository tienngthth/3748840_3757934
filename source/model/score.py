"""
Class Score is to store, update score for a particular player and check for winner 
"""
class Score:
    def __init__(self, target_score = 30):
        self.__score = 0
        self.__target_score = target_score

    def get_score(self):
        return self.__score

    def update_score(self, score):
        self.__score += score
        return self.__check_winner()

    def __check_winner(self):
        if (self.__score >= self.__target_score):
            return True
        return False