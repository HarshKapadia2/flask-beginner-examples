from flask import Flask, render_template

app = Flask(__name__)



@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home_page():
    return render_template('home_page.html')


@app.route('/home/<int:num>', methods=['GET'])
def factorial(num):
    fact = 1

    while(num > 1):
        fact = fact*num
        num -= 1

    return render_template('factorial.html', fact = fact)



if __name__ == '__main__':
    app.run(debug = True)