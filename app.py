#=============================================================
#=== ZADANIE 3 - Kod aplikacji Flask ===
#=============================================================

# Tu wklej kod do swojego zadania 
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def strona_glowna():
    return render_template('index.html')
