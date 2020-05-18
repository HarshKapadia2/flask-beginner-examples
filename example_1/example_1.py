from flask import Flask, render_template

app = Flask(__name__)



@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home_page():
    return render_template('home_page.html')


@app.route('/teacher', methods=['GET'])
def teacher():
    return render_template('teacher.html')


@app.route('/student', methods=['GET'])
def student():
    return render_template('student.html')



if __name__ == '__main__':
    app.run(debug = True)