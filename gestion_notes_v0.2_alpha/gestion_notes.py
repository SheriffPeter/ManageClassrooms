from datetime import date, timedelta
from random import randint
from statistics import StatisticsError
from gestion_notes_classes import Promotion, Eleve, Examen


def main():
    promo = Promotion('Gaëlle', 2022, 'initiation')
    ex1 = Examen('exam POO', 'python', date.today(), promo)
    ex2 = Examen('Zen of Python', 'python', date(2022, 9, 1), promo)
    
    for ex in (ex1, ex2):
        promo.ajouter_examen(ex)

    alice = Eleve('Test', 'Alice', date(1970, 1, 1))
    bob = Eleve('Démo', 'Bob', date(1728, 4, 1))
    charlie = Eleve('Truc', 'Charlie', date.today() + timedelta(days=1))

    for e in (alice, bob, charlie):
        promo.ajouter_eleve(e)

        for ex in promo.examens:
            if randint(1, 4) < 3:  # est-ce qu’on ajoute une note ?
                note = randint(0, 100) / 5
                e.ajouter_note(ex, note)
                print(f'Ajout de la note {note} sur {ex} pour {e}')
            else:
                print(f'Pas de note pour {e} sur {ex}')
    promo.sauvegarder('promo.data')

    try:
        print(f'{promo} (moyenne : {promo.calculer_moyenne()}/20)')
        for position, eleve, moyenne in promo.calculer_classement():
            print(f'  - {position}) {eleve} (moyenne : {moyenne}/20)')
    except StatisticsError:
        print(f'{promo} : aucune note')
    for e in promo.eleves_non_classes():
        print(f'  - {e} (aucune note)')

    print('Examens :')
    for ex in promo.examens:
        try:
            print(f'  - {ex} (moyenne : {ex.calculer_moyenne()}/20)')
        except StatisticsError:
            print(f'  - {ex} (aucune note)')

    print(promo.to_dict())
    


if __name__ == '__main__':
    main()
