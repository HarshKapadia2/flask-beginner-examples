from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/', methods=['GET'])
def home_page():
        return render_template('home_page.html')


@app.route('/dashboard', methods=['POST'])
def dashboard():
        f_name = request.form['f-name']
        l_name = request.form['l-name']
        age = request.form['age']

        return render_template('dashboard.html', f_name = f_name, l_name = l_name, age = age)



if __name__ == '__main__':
    app.run(debug = True)