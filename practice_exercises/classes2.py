'''
Press the run button above to start
'''


class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def halfway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)


def q1():
    question = input(
        "1. Imagine we've got a class called Point, it's going to return us an x coordinate and a y coordinate. Write the first line of the constructor for that class (it doesn't take an arguments)\n\n")
    return check(question, 'def __init__(self):', False)


def q2():
    question = input(
        "2. Imagine we're now on line 2 of the constructor, you're going to set x = 0, how would you do that?\n\n")
    return check(question, 'self.x = 0', False)


def q3():
    question = input('3. Now set y equal to zero\n\n')
    return check(question, 'self.y = 0', False)


def q4():
    question = input(
        "4. Let's rewrite this constructor so it can take two arguments called initx and inity, they will be the coordinate values. Write the first line of the constructor \n\n")
    return check(question, 'def __init__(self, initx, inity):', False)


def q5():
    question = input("5. Assign the value of x in the constructor to initx \n\n")
    return check(question, 'self.x = initx', False)


def q6():
    question = input("6. Assign the value of y in the constructor to inity \n\n")
    return check(question, 'self.y = inity', False)


def q7():
    question = input(
        "7. instantiate an instance of the Point class called p, assign x the value of 3 and y the value of 4\n\n")
    return check(question, 'p = Point(3,4)', False)


def q8():
    question = input("8. Point has a __str__ method, find out what it prints out for p\n\n")
    p = Point(3, 4)
    if check(question, 'print(p)', False):
        print(p)
    return check(question, 'print(p)', False)


def bonus():
    print('Congratulations on passsing the quiz!!! \o/')
    print("""
                                    .''.       
        .''.      .        *''*    :_\/_:     . 
        :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
    .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
  :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
  : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
    '..'  ':::'     * /\ *     .'/.\'.   '
        *            *..*         :
  """)
    print("\n\n")


def check(question, keyword=None, eval_it=True):
    try:
        if keyword in question or keyword == None:
            if keyword != 'print':
                print('=> {}'.format(eval(question))) if eval_it else 0
                print('\nCorrect\n')
                return True
            else:
                print('=> ', end='')
                eval(question) if eval_it else 0
                print('\nCorrect\n')
                return True
        else:
            print('\nIncorrect\n')
            return False
    except:
        print('\nIncorrect\n')
        return False


def run_questions(score, retry_dict, number_of_questions):
    remove_list = []
    for i in retry_dict:
        if i():
            remove_list.append(i)
            score += 1
    for i in remove_list:
        retry_dict.remove(i)
    print('You got {}/{} questions right\n'.format(score, number_of_questions))
    return {'score': score, 'retry_dict': retry_dict}


def main():
    score = 0
    retry_dict = [q1, q2, q3, q4, q5, q6, q7, q8]
    number_of_questions = len(retry_dict)
    res = run_questions(score, retry_dict, number_of_questions)

    while res['score'] < number_of_questions:

        retry = input("Try again? (type 'Y' for yes, any other key for no)\n")

        if retry.upper() != 'Y':
            sure = input(
                "Are you sure you want to quit the quiz?(type 'Y' for yes, any other key for no)\n").upper() == 'Y'
            if sure:
                print('\nGame Over\n\n')
                exit()
            print('\n')
        else:
            res = run_questions(res['score'], res['retry_dict'], number_of_questions)

    if res['score'] == number_of_questions:
        bonus()


main()

