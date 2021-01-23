from flask import Flask, render_template
app = Flask(__name__)

'''
#TODO: nakon sto se istilizuju strane, da se napravi logovanje
@app.route('/')
def login():
    return  render_template('Login.html')
'''
@app.route('/') #@app.route('/trosak/') 
def trosak():
    return  render_template('Trosak.html')

@app.route('/prihod/')
def prihod():
    return  render_template('Prihod.html')

@app.route('/pregled/')
def pregled():
    return  render_template('pregled.html')

if __name__ == '__main__' :
    app.run(debug=True)