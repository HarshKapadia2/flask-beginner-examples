from flask import Flask, render_template

app = Flask(__name__)



@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home_page():
    return render_template('home_page.html')


@app.route('/home/<int:num>', methods=['GET'])
def factorial(num):
    fact_list = []
    while num > 0:
        fact = 1
        temp = num
        while temp > 0:
            fact = fact*temp
            temp -= 1

        fact_list.append(fact)
        num -= 1
    
    fact_list.reverse()
    fact_list.insert(0, 1)


    return render_template('factorial.html', fact_list = fact_list)



if __name__ == '__main__':
    app.run(debug = True)