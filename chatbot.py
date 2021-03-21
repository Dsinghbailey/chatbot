
def chat(statement, true_func, false_func):
    print('statement')
    input1 = input() 
    if 'yes' in input1:
        true_func()
    else:
        false_func()

def hello():
    statement = '''hello
    need help fixing your code?'''
    chat(statement, reproduction_check, lambda: print('No can do'))

def reproduction_check():
    chat('Are you able to reproduce the problem?', quick_reproduction_check, reproduction_recs)

def reproduction_recs():
    pass

def quick_reproduction_check():
    chat('Are you able to reproduce the problem quickly?', cause_check, speedup_debugging)

def speedup_debugging():
    pass

def cause_check():
    chat('Do you know the cause?', fix_check, figure_out_cause)

def figure_out_cause():
    pass

def fix_check():
    chat('Do you know how to fix the cause?', break_other_check, give_fixes)

def give_fixes():
    pass

def break_other_check():
    chat('do you think it will break anything else?', regression_test, go_fix)

def go_fix():
    print('search the internet')

def regression_test():
    chat('h)