# Étape 1 : partir d'une image officielle Python
FROM python:3.11-slim
# Étape 2 : installer dépendances système (SQLite déjà inclus)
RUN apt-get update && apt-get install -y \
    build-essential \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*
# Étape 3 : définir le dossier de travail
WORKDIR /app
# Étape 4 : copier requirements et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Étape 5 : copier tout le projet
COPY . .
# Étape 6 : exposer le port de Django
EXPOSE 8000
# Étape 7 : lancer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
