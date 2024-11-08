from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample menu data
menu = [
    {'id': 1, 'name': 'Dosa', 'price': 80},
    {'id': 2, 'name': 'Panner cury', 'price': 150},
    {'id': 3, 'name': 'tea', 'price': 10},
    {'id': 4, 'name': 'coffe', 'price': 20},
]

cart = []

@app.route('/')
def index():
    return render_template('index.html', menu=menu, cart=cart)

@app.route('/add_to_cart/<int:menu_id>')
def add_to_cart(menu_id):
    for item in menu:
        if item['id'] == menu_id:
            cart.append(item)
            break
    return redirect(url_for('index'))

@app.route('/checkout')
def checkout():
    total = sum(item['price'] for item in cart)
    return render_template('checkout.html', cart=cart, total=total)

if __name__ == '__main__':
    app.run(debug=True)
