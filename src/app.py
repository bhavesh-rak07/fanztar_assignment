from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# Component data
components_data = {
    'A': {'name': 'LED Screen', 'price': 10.28},
    'B': {'name': 'OLED Screen', 'price': 24.07},
    'C': {'name': 'AMOLED Screen', 'price': 33.30},
    'D': {'name': 'Wide-Angle Camera', 'price': 25.94},
    'E': {'name': 'Ultra-Wide-Angle Camera', 'price': 32.39},
    'F': {'name': 'USB-C Port', 'price': 18.77},
    'G': {'name': 'Micro-USB Port', 'price': 15.13},
    'H': {'name': 'Lightning Port', 'price': 20.00},
    'I': {'name': 'Android OS', 'price': 42.31},
    'J': {'name': 'iOS OS', 'price': 45.00},
    'K': {'name': 'Metallic Body', 'price': 45.00},
    'L': {'name': 'Plastic Body', 'price': 30.00},
}

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    components = data.get('components', [])

    # Validate the components
    if len(components) != 5:
        return jsonify({'error': 'Invalid request. Please provide exactly 5 components.'}), 400

    # Calculate the total price and parts
    total = 0
    parts = []
    for code in components:
        component = components_data.get(code)
        if component is None:
            return jsonify({'error': f'Invalid component code: {code}'}), 400
        total += component['price']
        parts.append(component['name'])

    # Generate a unique order ID
    order_id = str(uuid4())

    # Return the response
    return jsonify({
        'order_id': order_id,
        'total': total,
        'parts': parts
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
