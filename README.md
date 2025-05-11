# curs_vcgj_25_scriitori

`Scriitori`
=====================================

# Cuprins

1. [Descriere aplicatie](#descriere-aplicatie)  
2. [Descriere versiune](#descriere-versiune)  
3. [Configurare](#configurare)  
4. [Testare cu pytest](#testare-cu-pytest)  


# Descriere aplicatie
[cuprins](#cuprins)

Aplicatia `scriitori` prezinta informatii despre scriitorul ales de studentul Mihaila Adelin-Gabriel, **Dmitry Glukhovsky**.  
Poate fi executata doar pe Linux. A fost testata pe Ubuntu 22.04.02.  
Componenta WEB a aplicatiei se bazeaza pe framework-ul `Flask`.  
Aplicatia este simpla, afiseaza informatii despre autor - disponibile la butonul "Dmitry Glukhovsky".

Pentru o navigare mai usoara in browser, pagina principala contine link-uri catre celelalte pagini.  
Fiecare pagina specifica (cea care afiseaza informatii despre scriitor sau atributele sale) contine un link catre pagina principala.

Aplicatia contine suport pentru containerizare in fisierul `Dockerfile` din directorul principal al aplicatiei.

Din punct de vedere al testarii, este inclus unit testing cu pytest, pentru functiile din biblioteca aplicatiei, aflate in directorul `app/libs`.

Pipeline-ul pentru Jenkins este definit in fisierul `Jenkinsfile`. Acesta cloneaza codul, creeaza mediul de lucru virtual (venv), il activeaza si ruleaza testele (unit test - cu pytest, verificari statice cu pylint).

# Descriere versiune
[cuprins](#cuprins)

## v01 - afisare 'raw' fara formatare. Adaugare link-uri intre pagini.

- ruta standard `'/'` - URL: http://127.0.0.1:5011  
- rute in aplicatia WEB pentru:  
  - scriitor: `/scriitor` - URL: http://127.0.0.1:5011/scriitor  
  - cea mai buna opera: `/scriitor/opera` - URL: http://127.0.0.1:5011/scriitor/opera  
  - genul literar: `/scriitor/gen` - URL: http://127.0.0.1:5011/scriitor/gen  

# Configurare
[cuprins](#cuprins)

Configurare `.venv` si instalare pachete

In directorul `app` rulati comenzile:

1. `activeaza_venv`: Incearca sa activeze venv-ul. Daca nu poate, configureaza venv-ul in directorul `.venv` si apoi instaleaza `flask` si `flask-bootstrap`. La urmatoarea rulare, va activa doar venv-ul.  
2. `ruleaza_aplicatia`: De rulat dupa activarea venv-ului. Va porni serverul pe IP: 127.0.0.1 si port 5011. Acces server din browser: http://127.0.0.1:5011

## EXEMPLU activare venv si rulare

```text
guest@Ubuntu24:~/SCC/curs_vcgj_25_scriitori$ source activeaza_venv
SUCCESS: venv was activated.
(.venv) guest@Ubuntu24:~/SCC/curs_vcgj_25_scriitori$ source ruleaza_aplicatia
Scriitori
 * Serving Flask app 'scriitori'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5011
Press CTRL+C to quit
 * Restarting with stat
Scriitori
```


Functiile din biblioteca de functii a aplicatiei:
- directorul `libs`, fisierul:
  - `biblioteca_scriitori.py`
    
au teste de tip *unit test* asociate. Acestea compara rezultatul obtinut de la functii cu valoarea asteptata, returnand **PASS** daca sunt egale si **FAIL** in caz contrar.

Pentru testare s-a folosit pachetul `pytest`. Se afla in `quickrequirements.txt`. Executia testelor:

```bash
pytest
python -m pytest
flask --app scriitori test
```

Ultima comanda functioneaza datorita definirii unei comenzi CLI `test` in aplicatie, care apeleaza `pytest.main(["."])`.
