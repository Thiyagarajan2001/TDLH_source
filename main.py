from flask import Flask, render_template,url_for,request,redirect
import Feedback
app = Flask(__name__)
@app.route('/', methods=['POST','GET'])
def Home():
  return render_template('index.html',status='')

@app.route("/Submit", methods=['POST','GET'])
def Submit():
    if request.method == 'POST':
        name = (request.form['name'])
        email = (request.form['email'])
        phone_number = (request.form['phone_number'])
        feedback = (request.form['feedback'])
        Feedback.submit(name,email,phone_number,feedback)
        return render_template('index.html',status='Form submission successful!')
    else:
      return render_template('index.html',status='')
if __name__ == '__main__':
    app.run(debug=True,port=5000)
