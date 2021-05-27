from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route('/covid19')
def covid19():
    return render_template('covid19.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/health')
def health():
    return render_template('health.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/livelyhood')
def livelyhood():
    return render_template('livelyhood.html')    

@app.route('/ourpartners')
def ourpartners():
    return render_template('ourpartners.html')

@app.route('/relief')
def relief():
    return render_template('relief.html')

@app.route('/samskara')
def samskara():
    return render_template('samskara.html')

@app.route('/social')
def social():
    return render_template('social.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/tribal')
def tribal():
    return render_template('tribal.html')

@app.route('/vanavasi')
def vanavasi():
    return render_template('vanavasi.html')

if __name__=='__main__':
    app.run(debug=True)