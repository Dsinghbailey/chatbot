import random
from time import sleep
from nltk.util import ngrams
import pdb

def printo(line):
    if isinstance(line, list):
        line = random.choice(line)
    sleep(random.random()/2)
    print('>>> ' + line)

def process_input(input1):
    input1 = input1.lower()
    input1 = ''.join([c for c in input1 if c.isalpha() or c == ' '])
    sentenceNgrams = []
    for i in range(1,3):
        sentenceNgrams =  sentenceNgrams + [' '.join(ngram) for ngram in ngrams(input1.lower().split(), n=i)]
    return sentenceNgrams

trueWords = ['yes', 'yep', 'sure', 'yea', 'yeah', 'I do', 'true', 'might', 'maybe']
falseWords = ['no', 'don\'t', 'do not', 'false']
noAnswer = ['I don\'t understand', 'error. could you be clearer?', 
    'try answering more simply. I understand yes and no and true and false and other things']
abortWords = ['quit', 'stop', 'go back', 'restart', 'q', 'r', 'ok', 'done', 'ok done', 'finished']

def check_abort(input1):
    if input1.lower().strip() in abortWords:
        return True
    else: 
        return False

def check_truth(checkType, input1):
    if check_abort(input1):
        hello()
        return
    if checkType == 'checkTrue':
        if any(x in process_input(input1) for x in trueWords):
            return True
        elif any(x in process_input(input1) for x in falseWords):
            return False
        else:
            printo(noAnswer)
            input1 = input()
            return check_truth(checkType, input1)
    else:
        if any(x in process_input(input1) for x in falseWords):
            return False
        else:
            return True

encourageWords = ['great.', 'I\'ll see what I can do.', 'neat.', 'yay', 'I\'m on it', 'thinking....']
disappointWords = ['oh ok.' 'got it.' 'processing', 'honk.']
def chat(statement, true_func, false_func, checkType='checkTrue'):
    printo(statement)
    input1 = input()
    if check_abort(input1):
        hello()
        return
    randInt = random.randint(1,5)
    if check_truth(checkType, input1):
        # printo encouragment randomly
        if randInt == 3:
            printo(encourageWords)
        true_func()
        return
    else:
        # printo disappointment randomlytest
        if randInt == 3:
            printo(disappointWords)
        false_func()
        return

def dead_end(statement, func=lambda: hello()):
    printo(statement)
    input1 = input()
    if check_abort(input1):
        func()
    else:
        more_help()

## Flow starts 
def hello():
    chat(['hello. need help fixing your code?', 'hi, do you have broken code that needs fixing?'], 
        reproduction_check, cant_help)

def cant_help():
    dead_end('Sorry I can only help with fixing broken code at the moment. Try searching somewhere else.')

def reproduction_check(problemType=''):
    chat('Are you able to reproduce the ' + problemType +  'problem?', quick_reproduction_check, reproduction_recs)

def reproduction_recs():
    chat('You don\'t need to reproduce all parts of the original bug. can you strip it done to it\'s essential parts and test those?',
        lambda: reproduction_check('core '), hypothesis_check)

def hypothesis_check():
    chat('Can you create hypotheses about why it doesn\'t work and test those?',
        quick_hypothesis_check, more_help)

def more_help():
    dead_end('This is over my head. Go ask for help from a human. I\'ll be here when you get back. (just type restart)')

def quick_hypothesis_check():
    chat('Are you able to test your hypotheses quickly?', cause_check, speedup_debugging)

def quick_reproduction_check():
    chat('Are you able to reproduce the problem quickly?', cause_check, speedup_debugging)

def speedup_debugging():
    pass
    
def cause_check():
    chat('After reproducing and checking, Do you think you know the cause?', fix_check, figure_out_cause)

def figure_out_cause():
    dead_end('Continue testing hypotheses and let me know when you\'ve found something', cause_check)

def fix_check():
    chat('Do you know how to fix the cause?', break_other_check, give_fixes)

def give_fixes():
    dead_end('give fixes')

def break_other_check():
    chat('do you think it will break anything else?', regression_test, go_fix)

def go_fix():
    dead_end('Great! go fix it. I\'ll be here for your next problem. (type restart)')

def regression_test():
    chat('h')

if __name__ == '__main__':
    hello()