class Boy:
    def __init__(self, userid house, tutor, form, fname, initial, lname):
        self.userid = userid
        self.house = house
        self.tutor = tutor
        self.form = form
        self.fname = fname
        self.lname = lname
        self.initial = initial

    def full_name(self):
        return self.fname, self.initial, self.lname

    def fancy_name(self):
        return self.fname[0].upper() + "." + self.initial.upper() + "." + self.lname.upper()

    def fancy_form(self): 
        if self.form <= 3:
            return "I" * self.form

        elif self.form == 4:
            return "IV"

        elif self.form == 5:
            return "V"
        
        elif self.form == 6:
            return "VI"
        
        else:
            return "Error"


class Score:
    def __init__(self, test, score, boy):
        self.test = test
        self.score = score
        self.boy = boy

class Test:
    scores = []

    def __init__(self, title):
        self.title = title
    
    def add_score(self, score, boy):
        scores += [Score(self, score, boy)]

    def top_mark(self):
        top = 0
        for score in self.scores:
            if score.score > top:
                top = score.score

        return top

    def lowest_mark(self):
        low = self.scores[0]
        for score in self.scores:
            if score.score < low:
                low = score.score

        return low

    def average(self):
        total = 0
        for score in self.scores:
            total += score.score

        return total / len(self.scores) # Note: Floor Division

class Class:
    tests = []

    def add_test(self, name):
        self.tests += [Test(name)]
