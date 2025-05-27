
from flask import Flask, jsonify
from datetime import datetime
import jdatetime

app = Flask(__name__)

@app.route("/api/time", methods=["GET"])
def get_time():
    now = datetime.utcnow()
    tehran_now = datetime.now()
    jalali = jdatetime.datetime.fromgregorian(datetime=tehran_now)

    return jsonify({
        "gregorian": {
            "year": tehran_now.year,
            "month": tehran_now.month,
            "day": tehran_now.day,
            "hour": tehran_now.hour,
            "minute": tehran_now.minute,
            "second": tehran_now.second
        },
        "jalali": {
            "year": jalali.year,
            "month": jalali.month,
            "day": jalali.day,
            "hour": jalali.hour,
            "minute": jalali.minute,
            "second": jalali.second
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
