class State:
    def __init__(self, lc, lm, rc, rm):
        self.lc = lc
        self.lm = lm
        self.rc = rc
        self.rm = rm

    def __repr__(self):
        return f"{self.lc},{self.lm}-{self.rc},{self.rm}"

    def is_done(self):
        return self.rc == 3 and self.rm == 3

    def is_valid(self):
        if self.lc < 0 or self.lm < 0 or self.rc < 0 or self.rm < 0:
            return False
        elif (self.lc + self.lm + self.rc + self.rm) != 6:
            return False
        # Keep it or make it a valid state?
        elif (self.lc > self.lm and self.lm > 0) or (self.rc > self.rm and self.rm > 0):
            return False
        else:
            return True
    
