import pickle
from statistics import StatisticsError

from gestion_notes_classes import Promotion

def main():
    with open('promo.data', mode='rb') as fd:
        promo = pickle.load(fd)
    if not isinstance(promo, Promotion):
        raise ValueError('Données corrompues')

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

if __name__ == '__main__':
    main()
