from flask import Flask, render_template, session, request
app = Flask(__name__)
import json
from convos import convos

@app.route('/')
def hello_world():
    session['userPath'] = ['greeting']
    convo = convos['greeting']
    return render_template('site.html', firstChat=convo['chat'], replyOptions=convo['replies'])

@app.route('/reply', methods=['POST'])
def reply():
    numArg = int(request.form['num']) - 1

    prevConvo = convos.get(session['userPath'][-1], convos['error']) 
    convoID = prevConvo['reply_convos'][numArg]
    session['userPath'] += [convoID]

    convo = convos.get(convoID, convos['error'])
    return json.dumps({"chat": convo['chat'], "replies": convo['replies']})

app.secret_key = 'honsdkfln'
if __name__ == "__main__":
	app.run('0.0.0.0', 8080)
