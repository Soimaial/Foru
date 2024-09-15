# Forum API

## Description

API REST pour la gestion d'un forum développé avec Django et Django REST Framework. Cette API permet de gérer des forums, des sujets et des messages.

## Technologies Utilisées

- Python 3.12
- Django 5.x ou superieur
- Django REST Framework
- PostgreSQL
- Postman (pour la documentation de l'API)

## Installation

### Prérequis

- Python 3.12
- PostgreSQL

### Étapes

1. **Cloner le Repository**

   ```bash
   git clone https://github.com/Soimaial/projet_forum.git
   cd forum_api

2.Créer et activer un environnement virtuel
    python -m venv env
#      Activation de l'environnement virtuel
    source env/bin/activate (Linux ou MacOS)
    env\Scripts\activate (Windows )

3.Installer les dépendances
    pip install -r requirements.txt

4. Créer et Configurer la base de données PostgreSQL

5. Créer un superutilisateur
# Créez un superutilisateur pour pouvoir accéder à l'interface d'administration de Django.
    python manage.py createsuperuser

6. python manage.py runserver
# Accédez à l'interface d'administration à l'adresse suivante : http://127.0.0.1:8000/admin/