# -*- coding: utf-8 -*-
class Match:
    score = []
    opcionset = {"1st": 0, "2nd": 1, "3rd": 2, "4th": 3, "5th": 4}

    def __init__(self, player1, player2, pacted_sets):
        self.p1 = player1
        self.p2 = player2
        self.pacted_sets = pacted_sets
        self.mgn = ""
        self.w1 = 0
        self.w2 = 0
        del self.score[:]
        self.score.append("0-0")
        self.fwinner = "none"

    def score_set(self):
        self.winner()
        return "{0} | {1}".format(self.mgn, self.scoreset())

    def startwinner(self, pw):
        if self.fwinner == "none":
            self.fwinner = pw

    def scoreset(self):
        sscore = ""
        start = 0
        for index in self.score:
            if start == 0:
                sscore = index
                start += 1
            else:
                sscore = sscore + ", " + index
        return sscore

    def sortwinnerscore(self, pw, sp1, sp2):
        self.startwinner(pw)
        if self.fwinner == pw:
            return sp1 + "-" + sp2
        else:
            return sp2 + "-" + sp1

    def save_set_won(self, player):
        if(player == self.p1):
            self.w1 += 1
        else:
            self.w2 += 1

    def save_score_set(self, sp1, sp2, ns, pw):
        if(ns == "1st"):
            self.score[0] = self.sortwinnerscore(
                pw, sp1, sp2)
        else:
            self.score.insert(self.opcionset.get(
                ns), self.sortwinnerscore(pw, sp1, sp2))

    def winner(self):
        nm = 1
        if int(self.pacted_sets) == 5:
            nm = 2

        if((self.w1 + nm) == int(self.pacted_sets)):
            self.mgn = self.p1 + " defeated " + self.p2
        elif ((self.w2 + nm) == int(self.pacted_sets)):
            self.mgn = self.p2 + " defeated " + self.p1
        else:
            self.mgn = self.p1 + " plays with " + self.p2
