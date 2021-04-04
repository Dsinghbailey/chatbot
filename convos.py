convos = {}
### Utility conversations
chat = ["Hello! I'm the RGD :). I'm here to help you fix problems in your code. Here's a good way to debug code:",
    "1. Make sure you have a good understanding of the problem",
    "2. Reproduce the problem and... 3. make sure you can reproduce it quickly",
    "4. Figure out the cause of the problem",
    "5. Plan out how to fix the cause of the problem",
    "6. Figure out if the planned fix will break anything else",
    "7. Fix the problem", 
    "Do you need help with any of these steps?"]
replies = ["I don't totally understand the problem",
    "I can't reproduce the issue",
    "It takes me a minute to reproduce the issue",
    "I can't figure out what is causing the problem",
    "I can't figure out how to fix the cause of the problem",
    "I'm afraid of breaking things with my fix",
    "I have a question about something else"]
replyConvos =["understand_rec1", "reproduce_rec1", "fast_reproduce_rec1"]
convos['greeting'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["This is over my head. Go ask for help from a human. Make sure to mention what you've tried so far"]
replies = ["I need help with something else"]
replyConvos = ["greeting2"]
convos['ask_for_help'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["Sorry there was an error"]
replies = ["restart"]
replyConvos = ["greeting"]
convos['error'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

## Understand recs
chat = ["Can you go ask the user for more information?", "(go do it if you can)"]
replies = ["No", "Do you have another way to understand the problem?", "I understand the problem now."]
replyConvos = ["understand_rec2", "understanding_rec2", "greeting2"]
convos['understand_rec1'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

chat = ["Can you fill in the blanks in this statement?: when a user does ___ the program should do ___ but it does ___ instead"]
replies = ["No", "Do you have another way to understand the problem?", "I understand the problem now."]
replyConvos = ["ask_for_help", "ask_for_help", "greeting2"]
convos['understand_rec2'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}

## Reproduce recs
chat = ["You don't need to reproduce all parts of the original bug. Can you strip it done to its essential parts and test those?"]
replies = ["Yep.  I have reproduced the problem.", "I don't understand. Do you have an example?", "No I can not."]
replyConvos = ["greeting2", "reproduce_rec1_example", "greeting2"]
convos['repoduce_rec1'] = {'chat': chat, 'replies': replies, 'reply_convos': replyConvos}




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
