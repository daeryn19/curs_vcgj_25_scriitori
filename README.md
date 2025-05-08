# curs_vcgj_25_scriitori
# Scriitori Flask App

## Cuprins

1. [Descriere aplicație](#descriere-aplicație)
2. [Descriere versiune](#descriere-versiune)
   1. [Buguri cunoscute](#buguri-cunoscute)
3. [Configurare](#configurare)
4. [Exemple aplicație](#exemple-aplicație)
5. [Testare cu pytest](#testare-cu-pytest)
6. [Verificare statică cu pylint](#verificare-statică-cu-pylint)
7. [Utilizare Docker și containerizare aplicație](#utilizare-docker-și-containerizare-aplicație)
8. [DevOps](#devops)
   1. [Pipeline Jenkins](#exemplu-executie-pipeline-jenkins)
   2. [Workflow GitHub Actions](#exemplu-executie-workflow-github-actions)
9. [Bibliografie](#bibliografie)

## Descriere aplicație

Aplicația `scriitori` este o aplicație Flask care servește informații despre viața și operele scriitorilor celebri, cum ar fi Victor Hugo. Aplicația include un API și o interfață web care permite utilizatorilor să interacționeze cu informațiile despre scriitori.

Aplicația poate fi rulată pe orice sistem Linux și a fost testată pe Ubuntu 22.04. 

### Funcționalități:
- Permite utilizatorilor să acceseze date despre Victor Hugo.
- Utilizează Flask pentru a expune API-ul și interfața web.
- Include testare cu `pytest` și verificări statice cu `pylint`.

## Descriere versiune

### v1.0 - Versiunea inițială
- Ruta principală: `/` - URL: `http://127.0.0.1:5011`
- API pentru Victor Hugo:
  - `/victor-hugo` - URL: `http://127.0.0.1:5011/victor-hugo`
  
### Probleme cunoscute:
1. La accesarea mai multor rute simultan, aplicația poate prezenta un comportament neregulat din cauza unei conflicte de rute.

## Configurare

### Clonare repository

1. Creează un spațiu de lucru și clonează aplicația `scriitori`:
   ```bash
   mkdir laborator_scrieri
   cd laborator_scrieri
   git clone https://github.com/tunetomc/scriitori.git

