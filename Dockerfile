FROM python:3.11-slim

# Définir le dossier de travail
WORKDIR /app

# Copier et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code du projet Django
COPY . .

# Exposer le port du serveur Django
EXPOSE 8000

# Lancer Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
