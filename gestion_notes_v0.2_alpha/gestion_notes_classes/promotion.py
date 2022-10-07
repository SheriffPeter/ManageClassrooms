import typing
import json
from statistics import StatisticsError, mean
from typing import TYPE_CHECKING, Iterable


from . import Base, exceptions

if TYPE_CHECKING:
    from . import Eleve, Examen
    from .eleve import EleveDict
    from .examen import ExamenDict


class PromotionDict(typing.TypedDict):
    prof: str
    annee: int
    niveau: str
    eleves: list['EleveDict']
    examens: list['ExamenDict']

class Promotion(Base):
    
    prof: str
    annee: int
    niveau: str
    eleves: list['Eleve']
    examens: list['Examen']

    def __init__(self, prof: str, annee: int, niveau: str):
        self.prof = prof
        self.annee = annee
        self.niveau = niveau
        self.eleves = []
        self.examens = []

    def __str__(self) -> str:
        return f'Promotion {self.niveau} {self.annee}'

    def ajouter_eleve(self, eleve: 'Eleve') -> None:
        if eleve in self.eleves:
            raise exceptions.EleveExistant(eleve)
        self.eleves.append(eleve)
        eleve.promotion = self

    def retirer_eleve(self, eleve: 'Eleve') -> None:
        try:
            self.eleves.remove(eleve)
            eleve.promotion = None
        except ValueError as e:
            raise exceptions.EleveInexistant(eleve) from e

    def ajouter_examen(self, exam: 'Examen') -> None:
        if exam.promotion is not self:
            raise exceptions.ExamenAffecte(f'{exam} est affecté à {exam.promotion}')
        if exam in self.examens:
            raise exceptions.ExamExistant(exam)
        self.examens.append(exam)

    def retirer_examen(self, exam: 'Examen') -> None:
        if exam not in self.examens:
            raise exceptions.ExamInexistant(exam)
        self.examens.remove(exam)

    def calculer_moyenne(self) -> float:
        # return mean(map(filter(lambda e: e.notes, 'Eleve'.calculer_moyenne), self.eleves))
        # return mean([e.calculer_moyenne() for e in self.eleves if e.notes])
        notes: list[float] = []
        for e in self.eleves:
            try:
                notes.append(e.calculer_moyenne())
            except StatisticsError:
                pass
        return mean(notes)

    def calculer_classement(self) -> list[tuple[int, 'Eleve', float]]:
        eleves_notes = filter(lambda e: e.notes, self.eleves)
        eleves_tries = sorted(eleves_notes, reverse=True)
        return [(i, e, e.calculer_moyenne()) for i, e in enumerate(eleves_tries, start=1)]

    def eleves_non_classes(self) -> Iterable['Eleve']:
        return filter(lambda e: not e.notes, self.eleves)

    def sauvegarder(self, fichier: str):
        with open(fichier, 'w') as fd:
            json.dump(self.to_dict(), fd, indent=3)

    @classmethod
    def charger(cls, ) # TODO

    def to_dict(self) -> PromotionDict:
        """
        Sérialisation de l'objet Promotion

        On parcours l'objet en sérialisant par récursion.
        Dès que l'on arrive sur un objet non sérialisable de notre implem (Eleve et Examen)
        On appelle leurs propres fonctions de sérialisation.
        On va créer un dictionnaire qui sera stringué ensuite
        """
        seri_dict: PromotionDict = {'prof': self.prof, 'annee': self.annee, 'niveau': self.niveau,
                  'eleves': [el.to_dict() for el in self.eleves], 
                  'examens': [ex.to_dict() for ex in self.examens],
                  }
        
        return seri_dict
        # ensuite on ajoute les serialisations de eleves et examens en les appelants diretement
            
    @classmethod
    def from_dict(cls,my_dict: PromotionDict) -> 'Promotion':  # type: ignore
        """
        Il faut commencer par récupérer les informations de bases, les faciles.

        Ensuite on commence par récupérer les examens qui ne peuvent exister sans une promo
        Et à la fin les élèves qui ont besoin d'un examen. It all makes sens \o/
        """
        promo = Promotion(prof="", annee=0, niveau="")
        # On commence par récupérer les valeurs de bases
        try:
            promo.prof = str(my_dict['prof'])
            promo.annee = int(my_dict['annee'])
            promo.niveau = str(my_dict['niveau'])
        except KeyError as ke:
            print(f'Your dictionnary is missing an essential information {ke}')
        except ValueError as ve:
            print(f"One of the key value is not of the good type {ve}")

        # On commence par récupérer les examens
        try: 
            promo.examens = [Examen.from_dict(ex, promo) for ex in my_dict['examens']]
        except KeyError as ke:
            print(f'Your dictionnary is missing examens, WTF DUDE ?! {ke}')

        
        # On commence par récupérer les examens
        try: 
            promo.eleves = [Eleve.from_dict(el, promo) for el in my_dict['eleves']]
        except KeyError as ve:
            print(f'Your dictionnary is missing eleves, WTF DUDE ?! {ve}')

        return promo
