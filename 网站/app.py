from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.secret_key = 'your-secret-key'
orders = []

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/sync-cart', methods=['POST'])
def sync_cart():
    data = request.get_json()
    seat = data.get('seat', '')
    cart = data.get('cart', [])
    total = data.get('total', 0)
    if seat and cart:
        orders.append({
            'seat': seat,
            'cart': cart,
            'total': total
        })
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error', 'message': '缺少座位号或订单数据'}), 400

@app.route('/admin')
def admin():
    return render_template('admin.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)
