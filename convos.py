convos = {}
### Utility conversations
chat = ["Hello! I'm the RGD :). What can I help you with today?"]
replies = ["I need help debugging code", "I need help writing some code", "I need help with something else"]
replyConvos = ["debug", 'write', "error"]
convos['greeting'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["What else can I help you with?"]
replies = ["I need help debugging code", "I need help writing some code", "I need help with something else"]
replyConvos = ["debug", 'write', "error"]
convos['greeting2'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

######
## Writing
chat = ["Here's a way to write code:",
    """1. Create an outline that describes each part of your program in steps <br>
    2. Turn the outline into comments and fill in each step with code <br>
    3. Look up things that you don't know how to do <br>
    4. Debug the program <br>""",
    "Do you need help with any of these steps?"]
replies = ["I need help creating an outline", "I need help writing code under a comment",
     "I need help looking up something I don't know how to do", "I need help debugging code", "I need help with something else"]
replyConvos = ["outline", 'lookup', "lookup", 'debug', 'greeting2']
convos['write'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

# Outline
chat = ["""Check out this article on creating a code outline: <br>
    <a href='https://medium.com/swlh/how-to-plan-a-coding-project-a-programming-outline-fc5917c60553'>
    https://medium.com/swlh/how-to-plan-a-coding-project-a-programming-outline-fc5917c60553
    </a>"""]
replies = ["Ok. Done. Restart."]
replyConvos = ['greeting2']
convos['outline'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

# lookup
chat = ["""Ok! Can you describe what you're trying to do in the box below?"""]
replies = ["text_box"]
replyConvos = ['language_check']
convos['lookup'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

# Language Check
chat = ["""Which programming language are you using?"""]
replies = ["text_box"]
replyConvos = ['search_google']
convos['language_check'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

# Search Google
chat = ["""Here is a search link that might solve your problem: <br>""",
"If it's not helpful try to redescribe your problem"]
replies = ["It's not helpful, let me redescribe my problem", "ok I'm done"]
replyConvos = ['lookup', 'greeting2']
convos['search_google'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

######
## Debugging
chat = ["Here's a good way to debug code:",
    """1. Make sure you have a good understanding of the problem <br>
    2. Reproduce the problem and... 3. make sure you can reproduce it quickly <br>
    4. Figure out the cause of the problem <br>
    5. Plan out how to fix the cause of the problem <br>
    6. Figure out if the planned fix will break anything else <br>
    7. Fix the problem and verify that it is fixed""", 
    "Do you need help with any of these steps?"]
replies = ["I don't totally understand the problem",
    "I can't reproduce the issue",
    "It takes me a minute to reproduce the issue",
    "I can't figure out what is causing the problem",
    "I can't figure out how to fix the cause of the problem",
    "I'm afraid of breaking things with my fix",
    "I don't think my fix is working",
    "I have a question about something else"]
replyConvos = ["understand_rec1", "reproduce_rec1", "fast_reproduce_rec1", "cause_rec1", "fix_rec1", "breaking_rec1", "verify_rec1", "greeting2"]
convos['debug'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["Ok! As a reminder here are my recommended steps to debugging a problem:",
    """1. Make sure you have a good understanding of the problem <br>
    2. Reproduce the problem and... 3. make sure you can reproduce it quickly <br>
    4. Figure out the cause of the problem <br>
    5. Plan out how to fix the cause of the problem <br>
    6. Figure out if the planned fix will break anything else <br>
    7. Fix the problem and verify that it is fixed <br>""",
    "Do you need help with any of them?"]
replies = ["I don't totally understand the problem",
    "I can't reproduce the issue",
    "It takes me a minute to reproduce the issue",
    "I can't figure out what is causing the problem",
    "I can't figure out how to fix the cause of the problem",
    "I'm afraid of breaking things with my fix",
    "I don't think my fix is working",
    "I have a question about something else"]
replyConvos = ["understand_rec1", "reproduce_rec1", "fast_reproduce_rec1", "cause_rec1", "fix_rec1", "breaking_rec1", "verify_rec1", "error"]
convos['debug2'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["This is over my head. Go ask for help from a human. Make sure to mention what you've tried so far"]
replies = ["I need help with something else"]
replyConvos = ["greeting2"]
convos['ask_for_help'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["Sorry... My ability to talk about that topic is still being built"]
replies = ["restart"]
replyConvos = ["greeting"]
convos['error'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

## Understand recs
chat = ["Can you go ask the user for more information?", "( Go do so if you can )"]
replies = ["Yep. I understand the problem now.", "No", "Do you have another way to understand the problem?"]
replyConvos = [ "debug2", "understand_rec2", "understand_rec2"]
convos['understand_rec1'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["Can you fill in the blanks in this statement?: When a user does ___ the program should do ___ but it does ___ instead"]
replies = ["Yes. I understand the problem now.", "No", "Do you have another way to understand the problem?"]
replyConvos = ["debug2", "ask_for_help", "ask_for_help"]
convos['understand_rec2'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

## Reproduce recs
chat = ["You don't need to reproduce all parts of the original bug. Can you strip it done to its essential parts and test those?"]
replies = ["Yep.  I have reproduced the problem.", "I don't understand. Do you have an example?", "No I can not."]
replyConvos = ["debug2", "reproduce_rec1_example", "reproduce_rec2"]
convos['reproduce_rec1'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["A backend error could be caused by messed up parameter, It's enough to be able to check that the parameter is messed up"]
replies = ["ok. Show me the debugging steps again", "I still need help reproducing the bug"]
replyConvos = ["debug2", "reproduce_rec2"]
convos['reproduce_rec1_example'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["Can you try to recreate the environment that the issue occured in programmatically?"]
replies = ["Yep. I have reproduced the problem.", "No I can not."]
replyConvos = ["debug2", "reproduce_rec3"]
convos['reproduce_rec2'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["Sometimes the inability to recreate a problem is the result of not fully understanding the problem."]
replies = ["I think I understandstand the problem, I just can't recreate it", "Give me tips about understanding the problem"]
replyConvos = ["reproduce_rec4", "understand_rec1"]
convos['reproduce_rec3'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["Sometimes we can't always reproduce a bug due to complex causes like race conditions, in these cases we should fix the likely cause of the bug and automatically log the bug if it happens again."]
replies = ["ok. I need help with something else", "How do you automatically log the bug?", "I need help figuring out the cause of the issue"]
replyConvos = ["debug2", "reproduce_rec4_logging", "cause_rec1"]
convos['reproduce_rec4'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["Place a logging statement that triggers when your problem triggers. For example if you encounter a value error on a server, have that server email you in event of that value error."]
replies = ["ok. I need help with something else", "I don't understand"]
replyConvos = ["debug2", "ask_for_help"]
convos['reproduce_rec4_logging'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

## Fast Reproduce recs
chat = ["You don't need to reproduce all parts of the original bug. Can you strip it done to its essential parts and test those?"]
replies = ["Yep.  I have reproduced the problem.", "I don't understand. Do you have an example?", "No I can not."]
replyConvos = ["debug2", "fast_reproduce_rec1_example", "fast_reproduce_rec2"]
convos['fast_reproduce_rec1'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["A backend error could be caused by messed up parameter, It's enough to be able to check that the parameter is messed up"]
replies = ["ok. Show me the debugging steps again", "I still need help speeding up reproducing the bug"]
replyConvos = ["debug2", "fast_reproduce_rec2"]
convos['fast_reproduce_rec1_example'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["Can you narrow down the place where the programming is going wrong and run that part only?"]
replies = ["Yep.  I have reproduced the problem.",  "No I can't."]
replyConvos = ["debug2", "ask_for_help"]
convos['fast_reproduce_rec2'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

## Cause recs
chat = ["Can you write down several top hypotheses and determine the most likely?"]
replies = ["Yep.  I have the most likely cause.", "I have no hypotheses", "I don't know how"]
replyConvos = ["debug2", "cause_rec2", "cause_rec1_explanation"]
convos['cause_rec1'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["Example causes could be: "
"1. a variable is getting sent incorrectly",
"2. a value is wrong in the database",
"3. Theres a typo on line 10"
"Causes can be surface level or deep, Try to find the root of an issue"]
replies = ["Yep.  I wrote some causes and I know which one is most likely.", "This doesn't help. Any other hints?"]
replyConvos = ["debug2", "cause_rec2"]
convos['cause_rec1_explanation'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["Can you narrow down the block of code where the bug is happening?",
"try to go as deep as possible!"]
replies = ["What do you mean by 'deep'?", "yep. I think I know where it is happening"]
replyConvos = ["cause_rec2_explanation", "cause_rec3", ]
convos['cause_rec2'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["If the error happens during after function call, going 'deep' means to step through the function definition instead of just looking at the call"]
replies = ["Ok. I've found the deepest troublesome block of code", "This doesn't help. Any other hints?"]
replyConvos = ["cause_rec3", "ask_for_help"]
convos['cause_rec2_explanation'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["Identify the values of variables coming into this block of code and leaving it when the problem happens",
 "Are they what you expect?"]
replies = ["No.I found one that be the cause!", "This isn't helpful"]
replyConvos = ["debug2", "ask_for_help", ]
convos['cause_rec3'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

## Fix recs
chat = ["Have you tried googling the issue or looking on stack overflow?"]
replies = ["Yeah I found a good fix I'm going to try", "I need help googling the issue", "This isn't helpful"]
replyConvos = ["debug2", 'lookup', "fix_rec2", ]
convos['fix_rec1'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["Sometimes when we're uncertain of a fix it means that we haven't found the root cause."]
replies = ["Ok show me tips on how to find the root cause", "This isn't helpful"]
replyConvos = ["fix_rec3", "ask_for_help", ]
convos['fix_rec2'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["To find the root cause you should go deeper."]
replies = ["What do you mean?", "This isn't helpful"]
replyConvos = ["fix_rec2_explanation", "ask_for_help", ]
convos['fix_rec2'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["Going 'deeper' means to look at the causes behind the cause. Why is your cause happening."]
replies = ["Ok. I think I understand.", "I don't get it still"]
replyConvos = ["debug2", "ask_for_help"]
convos["fix_rec2_explanation"] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

## Afraid of breaking other things (regression testing) recs
chat = ["List all of the things you're afraid of breaking, then for each of them list a way to check if they broke.",
"Also make sure you have a way to undo the effects of your code!"]
replies = ["ok. Done"]
replyConvos = ["debug2"]
convos['breaking_rec1'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

## Verify Fix recs
chat = ["Are you sure your fix isn't working?",
    "Were you able to reproduce the problem and is it still happening?"]
replies = ["I was able to reproduce the problem, but it is still happening.", 
    "I don't think I'm able to fully recreate the issue"]
replyConvos = ["verify_rec2", 'reproduce_rec1']
convos['verify_rec1'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["That's ok.", 
    "Sometimes problems have multiple causes."]
replies = ["Ok. I need help with something else.", 
    "Can you give me recommendations on how to figure out the cause?"]
replyConvos = ["debug2", 'cause_rec1']
convos['verify_rec2'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

"""
('This is over my head. Go ask for help from a human. I\'ll be here when you get back. (just type restart)')
'Great! go fix it. I\'ll be here for your next problem. 
'Continue testing hypotheses and let me know when you\'ve found something'
'After reproducing and checking, Do you think you know the cause?'
Can you create hypotheses about why it doesn\'t work and test those?',
'You don\'t need to reproduce all parts of the original bug. can you strip it done to it\'s essential parts and test those?'
'Sorry I can only help with fixing broken code at the moment. Try searching somewhere else.'
'Are you able to reproduce the ' + problemType +  'problem?
     "Can you narrow down a block of code that might contain the problem?",
            "Sometimes we can't always reproduce a bug due to complex causes like race condition"
"""

def convo_complete():
    global convos
    for eachConvo in convos.values():
        for eachConvoID in eachConvo['reply_convos']:
            if eachConvoID not in convos:
                print(eachConvoID) 

if __name__ == "__main__":
	convo_complete()
