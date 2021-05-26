from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route('/covid19')
def covid19():
    return render_template('covid19.html')


@app.route('/')
def home():
    return render_template('home.html')
@app.route('/team')
def team():
    return render_template('team.html')
@app.route('/ourparners')
def ourpartners():
    return render_template('ourpartners.html')
if __name__=='__main__':
    app.run(debug=True)