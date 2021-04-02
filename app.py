from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    firstChat = ["Hello! I'm the RGD :). I'm here to help you fix problems in your code. Here's how you debug code:",
        "1. Make sure you can reproduce the problem and... 2. make sure you can reproduce it quickly",
        "3. Figure out the cause of the problem",
        "4. Plan out how to fix the cause of the problem",
        "5. Figure out if the planned fix will break anything else",
        "6. Fix the problem", 
        "Do you need help with any of these steps?"]
    replyOptions = ["I can't reproduce the issue",
        "It takes me a minute to reproduce the issue",
        "I can't figure out what is causing the problem",
        "I can't figure out how to fix the cause of the problem",
        "I'm afraid of breaking things with my fix",
        "I have a question about something else"]

    return render_template('site.html', firstChat=firstChat, replyOptions=replyOptions)

if __name__ == "__main__":
	app.run('0.0.0.0', 8080)
