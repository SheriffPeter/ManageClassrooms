"""
Our main fichier pour les tests
"""

from datetime import date

# from promotion import Promotion
from eleve import Eleve
# from examen import Examen


if __name__ == "__main__":
    el1 = Eleve(date_naissance=date.today(),nom="coucou", prenom="hello")