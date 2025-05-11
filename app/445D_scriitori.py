# app/445D_scriitori.py
from flask import Flask, render_template_string
# Import the actual names and alias them to the names used in the routes
from app.lib.biblioteca_scriitori import descriere_scurta_autor as descriere_scurta, carti_autor as opere_autor

# Rest of your Flask code remains the same,
# as it calls descriere_scurta() and opere_autor()
app = Flask(__name__)

@app.route('/scriitori')
def pagina_index_scriitori():
    html = """
    <h1>Dostoievski</h1>
    <ul>
      <li><a href="/descriere_scurta_dostoievski">Descriere scurta a lui Dostoievski</a></li>
      <li><a href="/opere_dostoievski">Opere ale lui Dostoievski</a></li>
    </ul>
    """
    return render_template_string(html)

@app.route('/descriere_scurta_dostoievski')
def ruta_descriere_scurta():
    # Calls the imported function aliased as descriere_scurta
    return f"<p>{descriere_scurta()}</p><p><a href='/scriitori'>&larr; Înapoi</a></p>"

@app.route('/opere_dostoievski')
def ruta_opere_autor():
    # Calls the imported function aliased as opere_autor
    return f"<p>{opere_autor()}</p><p><a href='/scriitori'>&larr; Înapoi</a></p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True) # Using port 5011 and debug
