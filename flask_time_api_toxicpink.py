
from flask import Flask, jsonify
from flask_cors import CORS
import datetime
import jdatetime

app = Flask(__name__)
CORS(app)  # پشتیبانی از CORS برای اجازه دسترسی WebApp ها

@app.route("/api/time")
def get_time():
    now_gregorian = datetime.datetime.utcnow() + datetime.timedelta(hours=3, minutes=30)
    now_jalali = jdatetime.datetime.fromgregorian(datetime=now_gregorian)

    return jsonify({
        "gregorian": {
            "year": now_gregorian.year,
            "month": now_gregorian.month,
            "day": now_gregorian.day,
            "hour": now_gregorian.hour,
            "minute": now_gregorian.minute,
            "second": now_gregorian.second
        },
        "jalali": {
            "year": now_jalali.year,
            "month": now_jalali.month,
            "day": now_jalali.day,
            "hour": now_jalali.hour,
            "minute": now_jalali.minute,
            "second": now_jalali.second
        }
    })

if __name__ == "__main__":
    app.run(debug=True)
