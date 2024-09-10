from flask import request, jsonify
from database import create_app, init_db, get_db_session
from models import User, Order

app = create_app()

with app.app_context():
    init_db()

@app.route('/create_order', methods=['POST'])
def create_order():
    data = request.json
    user = User.query.filter_by(id=data['user_id']).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    order = Order(user_id=data['user_id'], dish_name=data['dish_name'], status='Created')
    db_session = get_db_session()
    db_session.add(order)
    db_session.commit()
    return jsonify({"message": "Order created successfully"})

@app.route('/orders/<int:user_id>', methods=['GET'])
def get_orders(user_id):
    orders = Order.query.filter_by(user_id=user_id).all()
    return jsonify([order.to_dict() for order in orders])

@app.route('/update_order/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.json
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    # Update the order status
    if 'status' in data:
        order.status = data['status']

    db_session = get_db_session()
    db_session.commit()

    return jsonify({"message": "Order updated successfully"})


if __name__ == '__main__':
    app.run(debug=True)
