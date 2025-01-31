from flask import Flask, render_template, request

app = Flask(__name__)

# Fungsi untuk menghitung harga berdasarkan durasi dan tingkat kesulitan
def hitung_harga(duration, difficulty):
    base_price = 10000  # Harga dasar per jam
    multiplier = {"mudah": 1, "sedang": 1.5, "sulit": 2}
    return duration * base_price * multiplier.get(difficulty, 1)

@app.route("/")
def home():
    return render_template("home.html")  # Mengakses home.html

@app.route("/repair", methods=["GET", "POST"])
def repair():
    price = None  # Default nilai harga
    if request.method == "POST":
        duration = float(request.form["duration"])
        difficulty = request.form["difficulty"]
        price = hitung_harga(duration, difficulty)

    return render_template("repair.html", price=price)

if __name__ == "__main__":
    app.run(debug=True)
