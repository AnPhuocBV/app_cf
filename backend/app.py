from flask import Flask
from flask_cors import CORS
from routes.categories import category_bp
from routes.orders import order_bp

app = Flask(__name__)
CORS(app)

# Đăng ký routes
app.register_blueprint(category_bp)
app.register_blueprint(order_bp)

@app.route('/')
def home():
    return "✅ Backend Flask đang chạy!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
