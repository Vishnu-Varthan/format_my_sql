from flask import Flask, render_template, session, url_for, request
import sqlparse

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def home():
	if request.method == 'GET':
		return render_template('home.html')
	else:
		print("ok")
		text = request.form['output']
		res = sqlparse.format(text, reindent=True, keyword_case='upper')
		return render_template('home.html' , data=res)

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == '__main__':
	app.secret_key = 'some secret key'
	app.run(debug=True)