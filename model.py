import pickle

# global variable
global model, scaler

def load():
    global model, scaler
    model = pickle.load(open('model/model_rf.pkl', 'rb'))
    scaler = pickle.load(open('model/scaler.pkl', 'rb'))

def prediksi(data):
    # Standardisasi data
    data = scaler.transform(data)

    # Prediksi hasil Status
    prediksi = int(model.predict(data))

    # Mapping hasil prediksi ke label yang sesuai
    if prediksi == 0:
        hasil_prediksi = "Dropout"
    elif prediksi == 1:
        hasil_prediksi = "Layak Panen"
    else:
        hasil_prediksi = "Sangat Layak Panen"

    return hasil_prediksi, prediksi