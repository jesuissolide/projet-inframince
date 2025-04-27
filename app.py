from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # ➔ capturer l'IP du visiteur
    visiteur_ip = request.remote_addr
    print(f"Un visiteur est arrivé depuis l'IP : {visiteur_ip}")
    
    return render_template('index.html')

@app.route('/projection', methods=['POST'])
def projection():
    data = request.json
    entité = data.get('entité')
    flux = data.get('flux')
    sceau = data.get('sceau')

    print(f"Transmission captée : {entité} a scellé {flux} avec {sceau}")
    return f"Encapsulation réussie pour l'entité {entité}. Le flux est en attente de fixation définitive."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
