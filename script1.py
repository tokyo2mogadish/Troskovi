from flask import  Flask, g, render_template, redirect, url_for, request, session # g is gonna be available across flask context for one specific reques (so one user)
app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'

#if the session exists i wanna put that information inside the g object so its gonna be available
@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        #we wanna put the user in a global object
        g.user = user
   

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
    
    def __repr__(self):
        return f'<User: {self.username}>'

#global variable that represents all the users; ovo je in-memory radi lakse demonstracije
users = []
users.append(User(id= 1, username= 'admin1', password = 'admin1'))



#TODO: nakon sto se istilizuju strane, da se napravi logovanje
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        session.pop('user_id', None) #svaki put kad user hoce da se uloguje ima da resetuje sesiju; ako hoces da se ulogujes a vec si ulogovan ima da ukloni prethodnu sesiju

        username = request.form['username']
        password = request.form['password']
        if(username == '' or password==''):
            error = 'morate da upisete i username i password'
            return render_template('Login.html', error = error)
        #pretpostavka da je username jedinstven
        #user = [x for x in users if x.username == username][0]
        user = next ((x for x in users if x.username == username), None)
        if (user == None):
            error = 'Ne postoji takav username'
            return render_template('Login.html', error = error)
        if (user and user.password == password) :
            session['user_id'] = user.id # sesija je nesto sto se prenosi u kuki pa mozemo da joj prosledimo samo proste tipove podataka
            return redirect(url_for('trosak')) # url_for() function generates an endpoint for the provided method
        
        else:
            error = 'username ili password nisu ispravni'
            return render_template('Login.html', error = error)
       
    return render_template('Login.html')

@app.route('/') #@app.route('/trosak/') 
def trosak():
    if not g.user:
        return redirect(url_for('login'))

    return  render_template('Trosak.html')

@app.route('/prihod/')
def prihod():
    if not g.user:
        return redirect(url_for('login'))
    return  render_template('Prihod.html')

@app.route('/pregled/')
def pregled():
    if not g.user:
        return redirect(url_for('login'))
    return  render_template('pregled.html')

if __name__ == '__main__' :
    app.run(debug=True)