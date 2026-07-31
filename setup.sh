#!/bin/bash

echo "Création de l'environnement virtuel..."
python -m venv venv

echo "Activation..."
source venv/bin/activate

echo "Installation des dépendances..."
pip install -r requirements.txt

echo "Installation de TaskFlow..."
pip install .

echo "Installation terminée."