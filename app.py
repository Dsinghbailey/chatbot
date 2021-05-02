from flask import Flask, render_template, session, request
app = Flask(__name__)
import json
from convos import convos

@app.route('/')
def hello_world():
    session['userPath'] = ['greeting']
    session['googleSearch'] = ""
    convo = convos['greeting']
    return render_template('site.html', firstChat=convo['chat'], replyOptions=convo['replies'])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/reply', methods=['POST'])
def reply():
    numArg = int(request.form['num']) - 1
    # Check for text box
    if numArg == -1:
        numArg = 0
        textArg = request.form['text'] 
        session['googleSearch'] += textArg + ' '

    prevConvo = convos.get(session['userPath'][-1], convos['error'])
    print(prevConvo['reply_convos'])
    print(numArg)
    try:
        convoID = prevConvo['reply_convos'][numArg]
    except:
        print('missing reply')
        convoID = 'error'
        
    session['userPath'] += [convoID]
    
    convo = convos.get(convoID, convos['error'])
    if convoID == 'search_google':
        convo['chat'] = ["""Here is a search link that might solve your problem: <br>""",
            "If it's not helpful try to redescribe your problem"]   
        convo['chat'][0] += '<a target="_blank" href="https://google.com/search?q=' + session["googleSearch"] + '"> Click Here</a>'
        session["googleSearch"] = ''
    return json.dumps({"chat": convo['chat'], "replies": convo['replies']})

app.secret_key = 'honsdkfln'
if __name__ == "__main__":
	app.run('0.0.0.0', 8080)
