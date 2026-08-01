#!/bin/bash

if [ ! -d "venv" ]; then
    echo "Création de l'environnement virtuel..."
    python -m venv venv
else
    echo "Environnement virtuel déjà présent."
fi

echo "Activation..."

source venv/bin/activate

echo "Mise à jour de pip..."
python -m pip install --upgrade pip

echo "Installation des dépendances..."
pip install -r requirements.txt

echo "Installation de TaskFlow..."
pip install .

echo "Installation terminée."
