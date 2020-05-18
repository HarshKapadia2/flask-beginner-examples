from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)

app.secret_key = 'Harsh'



@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'GET':
        return render_template('home_page.html')

    elif request.method == 'POST':
        log_in_details = {1: 'Selena', 2: 'Lucas', 3: 'Felix'}

        user_id = int(request.form['user-id'])
        password = request.form['password']

        if user_id in log_in_details and log_in_details[user_id] == password:
            return redirect('/dashboard')

        else:
            flash('Incorrect e-mail or password...', 'error')
            return redirect('/')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')



if __name__ == '__main__':
    app.run(debug = True)