'''
Press the run button above to start
'''


def q1():
    question = input("1. Write the first line of a class called Helloworld?\n\n")
    return check(question, '''class Helloworld:''', False)


def q2():
    question = input('2. Instantiate an instance of the Helloworld class, call it hi\n\n')
    return check(question, 'hi = Helloworld()', False)


def q3():
    question = input('3. Using the hi instance of Helloworld, call the message function\n\n')
    return check(question, 'hi.message()', False)


def bonus():
    pass
    # print('Congratulations on passsing the quiz!!! \o/')
    # print("""
    #                                   .''.
    #       .''.      .        *''*    :_\/_:     .
    #       :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
    #   .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
    # :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
    # : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
    #   '..'  ':::'     * /\ *     .'/.\'.   '
    #       *            *..*         :
    # """)
    # print("\n\n")


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
    retry_dict = [q1, q2, q3]
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

