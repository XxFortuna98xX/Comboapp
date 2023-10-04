from flask import Flask
from flask import url_for, render_template
import os

app = Flask(__name__)
picFolder = os.path.join('static', 'pics')
app.config['UPLOAD_FOLDER'] = picFolder

@app.route('/')
def index():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'Simo.ico')
    return render_template('index.html', user_image= pic1)

if __name__ == '__main__':
    app.run(debug=True, port=8000)

Combo = ["Jeb", "Cross", "Montante", "Gancio Destro", "Gancio Sinistro", "Gangio Destro americana", "Gancio Sinistro americana", "Teschio", "Full", "Mataleao"]
#0 Carezza (combo 1-10)
#1 Saluto (combo 1-15)
#2 Normale (combo 1-20)
#3 Sparing (combo 1-25)
#4 Brutal (combo 1-30)
#5 Distruzione (combo 1-50)
#6 Quindi (combo 233-330)
