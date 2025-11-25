# ---- 1. Image de base ----
FROM python:3.11-slim

# ---- 2. Variables d'environnement pour la prod ----
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# ---- 3. Définir le dossier de travail ----
WORKDIR /app

# ---- 4. Installer les dépendances ----
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- 5. Copier le code du projet ----
COPY . .

# ---- 6. Collecte des fichiers statiques ----
RUN python manage.py collectstatic --noinput

# ---- 7. Exposer le port ----
EXPOSE 8000

# ---- 8. Lancer le serveur Django avec Gunicorn ----
CMD ["sh", "-c", "gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT"]
