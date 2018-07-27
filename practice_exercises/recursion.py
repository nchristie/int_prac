'''
Press the run button above to start
'''


def q1(rerun=False):
    question = input("1. In a recursive function which calculates n factorial, what would the base case be?\n\n")
    return check(question.replace(' ', ''), 'n==1', False)


factorial_gapfill = '''
    def factorial(n):\n
      if n == 1:
        return (2a)__
      else:
        return (2b)______________

    Fill the gaps in the function above
    '''


def q2(rerun=False):
    print(factorial_gapfill)
    question = input("(2a) ")
    return check(question, '1', False)


def q3(rerun=False):
    print(factorial_gapfill) if rerun == True else None
    question = input("(2b) ")
    return check(question.replace(' ', ''), 'n*factorial(n-1)', False)


countdown_gapfill = '''
  This function will count down from a given number to 1 and then print 'Blastoff!' If the number is below 1 then it'll simply print 'Blastoff!'
  example:
  countdown(3)

  3
  2
  1
  Blastoff!

    def countdown(n): 
      if n (3a)_____:
        print(n)
      if n (3b)_____: 
        print('Blastoff!')
      else: 
        (3c)_____________

  Fill the gaps
  '''


def q4(rerun=False):
    print(countdown_gapfill)
    question = input("(3a) ")
    return check(question.replace(' ', ''), '>=1', False)


def q5(rerun=False):
    print(countdown_gapfill) if rerun == True else None
    question = input("(3b) ")
    return check(question.replace(' ', ''), '<=1', False)


def q6(rerun=False):
    print(countdown_gapfill) if rerun == True else None
    question = input("(3c) ")
    return check(question.replace(' ', ''), 'returncountdown(n-1)', False)


add_all_gapfill = '''
  This function takes an integer and adds it to all the integers below until 1.
  e.g. 
  add_all(5):
    # performs this calculation: 5 + 4 + 3 + 2 + 1
    return 15

  def add_all(n): 
    if n < (4a)__ or type(n) != (4b)____: 
      raise (4c)_________('Function only takes positive integers') 
    if n == 1: 
      return 1 
    else: 
      return (4d)______________

  Fill the gaps
  '''


def q7(rerun=False):
    print(add_all_gapfill)
    question = input("(4a) ")
    return check(question, '1', False)


def q8(rerun=False):
    print(add_all_gapfill) if rerun == True else None
    question = input("(4b) ")
    return check(question, 'int', False)


def q9(rerun=False):
    print(add_all_gapfill) if rerun == True else None
    question = input("(4c) ")
    return check(question, 'Exception', False)


def q10(rerun=False):
    print(add_all_gapfill) if rerun == True else None
    question = input("(4d) ")
    return check(question.replace(' ', ''), 'n+add_all(n-1)', False)


def bonus():
    pass
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
                print('''\n

                                        __  __
       _________  _____________  _____/ /_/ /
      / ___/ __ \/ ___/ ___/ _ \/ ___/ __/ / 
     / /__/ /_/ / /  / /  /  __/ /__/ /_/_/  
     \___/\____/_/  /_/   \___/\___/\__(_)                                                               
        \n''')
                input()
                return True
            else:
                print('=> ', end='')
                eval(question) if eval_it else 0
                print('\nCorrect\n')
                return True
        else:
            print('\nIncorrect\n')
            input()
            return False
    except:
        print('\nIncorrect\n')
        return False


def run_questions(score, retry_dict, number_of_questions, rerun):
    remove_list = []
    for i in retry_dict:
        if i(rerun):
            remove_list.append(i)
            score += 1
    for i in remove_list:
        retry_dict.remove(i)
    print('You got {}/{} questions right\n'.format(score, number_of_questions))
    return {'score': score, 'retry_dict': retry_dict}


def main():
    rerun = False
    score = 0
    retry_dict = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    number_of_questions = len(retry_dict)
    res = run_questions(score, retry_dict, number_of_questions, rerun=False)

    while res['score'] < number_of_questions:

        retry = input("\nTry again? (type 'Y' for yes, any other key for no)\n")

        if retry.upper() != 'Y':
            sure = input(
                "\nAre you sure you want to quit the quiz?(type 'Y' for yes, any other key for no)\n").upper() == 'Y'
            if sure:
                print('''\
    ██████╗  █████╗ ███╗   ███╗███████╗
    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
    ██║  ███╗███████║██╔████╔██║█████╗  
    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝

    ██████╗ ██╗   ██╗███████╗██████╗   
    ██╔═══██╗██║   ██║██╔════╝██╔══██╗  
    ██║   ██║██║   ██║█████╗  ██████╔╝  
    ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗  
    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║  
    ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝

        \n\n''')
                exit()
        else:
            res = run_questions(res['score'], res['retry_dict'], number_of_questions, rerun=True)

    if res['score'] == number_of_questions:
        bonus()


main()

