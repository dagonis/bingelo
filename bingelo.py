import random


class Problem(object):
    BASES = dict(bin=2, int=10, hex=16)
    DIFFICULTY = {1: 255, 2: 65535, 3: 4294967295}

    def __init__(self, sbase, dbase, diff):
        self.sbase = sbase
        self.dbase = dbase
        self.num = random.randint(0, self.DIFFICULTY[diff])

    def solve(self):
        while True:
            answer = raw_input("What is {} in base {}?: ".format(self.sbase(self.num), self.BASES[self.dbase.__name__]))
            try:
                if int(answer, self.BASES[self.dbase.__name__]) == self.num:
                    print("Correct")
                    user_cc = raw_input("Want another problem? y/N: ")
                    if user_cc.lower() == 'y':
                        return True
                    else:
                        return False
                else:
                    user_c = raw_input("Incorrect. Try again? y/N: ")
                    if user_c.lower() == 'y':
                        continue
                    else:
                        return False
            except:
                return "Something is weird about your answer"


def main():
    BANNER = "{1}\n{0} Welcome to Bingelo! {0}\n{1}".format("*", "*"*23)
    PROBLEM_MENU = """What kind of problem do you want to solve?
{}) Decimal to Binary
{}) Decimal to Hex
{}) Hex to Decimal
{}) Hex to Binary
{}) Binary to Decimal
{}) Binary to Hex
Your choice: """.format(*[str(x) for x in range(1, 7)])
    DIFFICULTY_MENU = """Select difficulty
{}) Easy
{}) Medium
{}) Hard
Your choice: """.format(1, 2, 3)
    print(BANNER)
    user_choice = int(raw_input(PROBLEM_MENU))
    user_difficulty = int(raw_input(DIFFICULTY_MENU))
    CHOICES = {1: (int, bin, user_difficulty), 2: (int, hex, user_difficulty),
               3: (hex, int, user_difficulty), 4: (hex, bin, user_difficulty),
               5: (bin, int, user_difficulty), 6: (bin, hex, user_difficulty)}
    try:
        p = Problem(*CHOICES[user_choice])
        return p.solve()
    except:
        print("Something went wrong along the way, please try again")
        main()

if __name__ == '__main__':
    play = True
    while play:
        play = main()
    print("Exiting")