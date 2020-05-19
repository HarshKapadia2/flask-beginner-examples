from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/', methods=['GET'])
def home_page():
        return render_template('home_page.html')


@app.route('/cart_bill', methods=['POST'])
def cart_bill():
    menu = {0: [50, 'Tomatoes'], 1: [10, 'Coriander'], 2: [20, 'Potatoes']}

    isChecked = request.form.getlist('is-checked')
    j = 0
    for i in isChecked:
        i = int(i)
        isChecked[j] = i
        j += 1

    tomato_qty = int(request.form['tomato-qty'])
    coriander_qty = int(request.form['coriander-qty'])
    potato_qty = int(request.form['potato-qty'])
    menu[0].append(tomato_qty)
    menu[1].append(coriander_qty)
    menu[2].append(potato_qty)

    menu[0].append(menu[0][0] * menu[0][2])
    menu[1].append(menu[1][0] * menu[1][2])
    menu[2].append(menu[2][0] * menu[2][2])

    total = menu[0][3] + menu[1][3] + menu[2][3]

    return render_template('cart_bill.html', final_menu = menu, total = total, isChecked = isChecked)



if __name__ == '__main__':
    app.run(debug = True)