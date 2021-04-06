convos = {}
### Utility conversations
chat = ["Hello! I'm the RGD :). I'm here to help you fix problems in your code. Here's a good way to debug code:",
    "1. Make sure you have a good understanding of the problem",
    "2. Reproduce the problem and... 3. make sure you can reproduce it quickly",
    "4. Figure out the cause of the problem",
    "5. Plan out how to fix the cause of the problem",
    "6. Figure out if the planned fix will break anything else",
    "7. Fix the problem and verify that it is fixed", 
    "Do you need help with any of these steps?"]
replies = ["I don't totally understand the problem",
    "I can't reproduce the issue",
    "It takes me a minute to reproduce the issue",
    "I can't figure out what is causing the problem",
    "I can't figure out how to fix the cause of the problem",
    "I'm afraid of breaking things with my fix",
    "I don't think my fix is working",
    "I have a question about something else"]
replyConvos = ["understand_rec1", "reproduce_rec1", "fast_reproduce_rec1", "cause_rec1", "breaking_rec1", "verify_rec1", "error"]
convos['greeting'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["Ok! As a reminder here are my recommended steps to debugging a problem:",
    "1. Make sure you have a good understanding of the problem",
    "2. Reproduce the problem and... 3. make sure you can reproduce it quickly",
    "4. Figure out the cause of the problem",
    "5. Plan out how to fix the cause of the problem",
    "6. Figure out if the planned fix will break anything else",
    "7. Fix the problem and verify that it is fixed", 
    "Do you need help with any of them?"]
replies = ["I don't totally understand the problem",
    "I can't reproduce the issue",
    "It takes me a minute to reproduce the issue",
    "I can't figure out what is causing the problem",
    "I can't figure out how to fix the cause of the problem",
    "I'm afraid of breaking things with my fix",
    "I don't think my fix is working",
    "I have a question about something else"]
replyConvos = ["understand_rec1", "reproduce_rec1", "fast_reproduce_rec1", "cause_rec1", "breaking_rec1", "verify_rec1", "error"]
convos['greeting2'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

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
replyConvos = [ "greeting2", "understand_rec2", "understand_rec2"]
convos['understand_rec1'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["Can you fill in the blanks in this statement?: When a user does ___ the program should do ___ but it does ___ instead"]
replies = ["Yes. I understand the problem now.", "No", "Do you have another way to understand the problem?"]
replyConvos = ["greeting2", "ask_for_help", "ask_for_help"]
convos['understand_rec2'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

## Reproduce recs
chat = ["You don't need to reproduce all parts of the original bug. Can you strip it done to its essential parts and test those?"]
replies = ["Yep.  I have reproduced the problem.", "I don't understand. Do you have an example?", "No I can not."]
replyConvos = ["greeting2", "reproduce_rec1_example", "reproduce_rec2"]
convos['reproduce_rec1'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["You don't need to reproduce all parts of the original bug. Can you strip it done to its essential parts and test those?"]
replies = ["Yes. Show me the debugging steps again", "I still need help reproducing the bug"]
replyConvos = ["greeting2", "reproduce_rec2"]
convos['reproduce_rec1_example'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["Can you try to recreate the environment that the issue occured in programmatically?"]
replies = ["Yep. I have reproduced the problem.", "No I can not."]
replyConvos = ["greeting2", "reproduce_rec3"]
convos['reproduce_rec2'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["Sometimes the inability to recreate a problem is the result of not fully understanding the problem."]
replies = ["I think I understandstand the problem, I just can't recreate it", "Give me tips about understanding the problem"]
replyConvos = ["reproduce_rec4", "understand_rec1"]
convos['reproduce_rec3'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["Sometimes we can't always reproduce a bug due to complex causes like race conditions, in these cases we should fix the likely cause of the bug and automatically the bug if it happens again."]
replies = ["ok. I need help with something else", "How do you automatically log the bug?", "I need help figuring out the cause of the issue"]
replyConvos = ["greeting2", "reproduce_rec4_logging", "cause_rec1"]
convos['reproduce_rec4'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["Place a logging statement that triggers when your problem triggers. For example if you encounter a value error on a server, have that server email you in event of that value error."]
replies = ["ok. I need help with something else", "I don't understand"]
replyConvos = ["greeting2", "ask for help"]
convos['reproduce_rec4_logging'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

## Fast Reproduce recs
chat = ["You don't need to reproduce all parts of the original bug. Can you strip it done to its essential parts and test those?"]
replies = ["Yep.  I have reproduced the problem.", "I don't understand. Do you have an example?", "No I can not."]
replyConvos = ["greeting2", "fast_reproduce_rec1_example", "greeting2"]
convos['fast_reproduce_rec1'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

## Cause recs
chat = ["Can you write down several top hypotheses and determine the most likely cause?"]
replies = ["Yep.  I have the most likely cause.", "I have no hypotheses", "I don't know how"]
replyConvos = ["greeting2", "cause_rec2", "cause_rec1_explanation"]
convos['cause_rec1'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

## Afraid of breaking other things (regression testing)
chat = ["List all of the things you're afraid of breaking, then for each of them list a way to check if they broke.",
"Also make sure you have a way to undo the effects of your code!"]
replies = ["ok. Done"]
replyConvos = ["greeting2"]
convos['breaking_rec1'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}


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
