import sklearn
from flask import Flask, render_template, request
from model import load, prediksi

app = Flask(__name__)

# load model dan scaler
load()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/homebase')
def homebase():
   return render_template('home.html')

@app.route('/informasi')
def informasi():
   return render_template('informasi.html')

@app.route('/aplikasi')
def aplikasi():
   return render_template('index.html')

@app.route('/anggotakel')
def anggotakel():
   return render_template('anggota.html')

@app.route('/informasipenanaman')
def informasipenanaman():
   return render_template('informasi-penanaman.html')

@app.route('/informasibibit')
def informasibibit():
   return render_template('informasi-bibit.html')

@app.route('/informasidata')
def informasidata():
   return render_template('informasi-data.html')

@app.route("/predict", methods=["POST"])
def predict():
    # menangkap data yang diinput user melalui form
    Luas_Panen = int(request.form['Luas_Panen'])
    Provinsi = int(0)
    Tahun = int(request.form['Tahun'])
    Suhu_rata_rata = int(request.form['Suhu_rata_rata'])
    Curah_hujan = int(request.form['Curah_hujan'])
    Kelembapan = int(request.form['Kelembapan'])

    # melakukan prediksi menggunakan model yang telah dibuat
    data = [[Luas_Panen, Provinsi, Tahun, Suhu_rata_rata, Curah_hujan, Kelembapan]]
    prediction_result, confidence = prediksi(data)
    return render_template('index.html', hasil_prediksi=prediction_result, nilai_kepercayaan=confidence)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)