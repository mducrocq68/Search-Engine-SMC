from flask import Flask, render_template, request
app = Flask(__name__)


# @ route() decorator tell Flask what URL should trigger our function

@app.route('/send/', methods=['GET','POST'])

def send():

	if request.method == 'POST':

		age_post = request.form['age']
		return render_template('age.html', age = age_post)

	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)
