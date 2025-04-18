from flask import Flask, jsonify, request
from datetime import datetime
import pytz

app = Flask(__name__)

API_TOKEN = "supersecrettoken123"

capital_timezones = {
    "Washington": "America/New_York",
    "London": "Europe/London",
    "Tokyo": "Asia/Tokyo",
    "Paris": "Europe/Paris",
    "Beijing": "Asia/Shanghai",
    "Ottawa": "America/Toronto",
    "Canberra": "Australia/Sydney"
    # Add more if needed
}

def token_required(f):
    def decorator(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            if token == API_TOKEN:
                return f(*args, **kwargs)
        return jsonify({"error": "Unauthorized – provide a valid token"}), 401
    decorator.__name__ = f.__name__
    return decorator

@app.route('/')
def home():
    return 'Try: /api/time?city=Tokyo with a Bearer token in the header.'

@app.route('/api/time', methods=['GET'])
@token_required
def get_time():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "Missing 'city' parameter"}), 400

    timezone_name = capital_timezones.get(city)
    if not timezone_name:
        return jsonify({"error": f"City '{city}' not found in database"}), 404

    timezone = pytz.timezone(timezone_name)
    now = datetime.now(timezone)
    utc_offset = now.strftime('%z')
    formatted_offset = f"UTC{utc_offset[:3]}:{utc_offset[3:]}"  # UTC+09:00

    return jsonify({
        "city": city,
        "local_time": now.strftime("%Y-%m-%d %H:%M:%S"),
        "utc_offset": formatted_offset
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
