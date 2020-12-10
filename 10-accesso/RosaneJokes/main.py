from flask import Flask, render_template, request
from model import getDadJoke
from gtts import gTTS
import random 

web_site = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

@web_site.route('/', methods=['GET','POST'])
@web_site.route('/index', methods=['GET','POST'])
def index(background="DeepSkyBlue",fontsize="medium"):
    return render_template('index.html', background=background, fontsize=fontsize)
    
    
@web_site.route('/dadjoke', methods=['GET','POST'])
def dadjoke():
    if request.method == 'GET':
        return "Please use the form."
    else:
        userdata=request.form
        print(userdata)
        joke=getDadJoke(userdata['search'])
        language = 'en'
        myobj = gTTS(text=joke, lang=language, slow=False) 
        myobj.save("static/output.mp3") 
        return render_template('dadjoke.html',joke=joke, rand=random.random())


web_site.run(host='0.0.0.0', port=8080)