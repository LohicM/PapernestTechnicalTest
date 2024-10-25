
# PapernestTechnicalTest


Ce Projet est un test technique donné par Papernest dont le but est de développer une API et d'y inclure une méthode GET pour obtenir la couverture 2G, 3G et 4G d'une adresse.

Pour ce projet, j'ai décider d'utiliser Python avec FastAPI et uvicorn pour l'API, ainsi que Requests, Pandas et Pyproj pour la récupération et gestion de datas.

Je vous remercie sincèrement pour le temps que vous accorderez à l'évaluation de ce projet ainsi que pour l'intérêt que vous portez à mon profil.

Loïc Marlard


## Prérequis

- Python 3.10.12
- Postman, Insomnia ou un navigateur web

## Lancement

Pour lancer le projet :

```bash
  uvicorn main:app --reload
```


## API Reference

#### Get la couverture d'une adresse

```http
  GET http://127.0.0.1:8000/?q=Adresse
```
Par exemple:

```http
GET http://127.0.0.1:8000/?q=2+allée+rembrandt+94800+Paris
```
Response:

```json
{
  "orange": {
    "2G": true,
    "3G": true,
    "4G": true
  },
  "SFR": {
    "2G": true,
    "3G": true,
    "4G": true
  },
  "Free": {
    "2G": false,
    "3G": true,
    "4G": true
  },
  "Bouygues": {
    "2G": false,
    "3G": true,
    "4G": false
  }
}
```
