from datetime import date
from statistics import mean
import typing

from . import Base, Promotion, Eleve

class ExamenDict(typing.TypedDict):
    matiere: str
    date_exam: str
    nom: str
    hash: int


class Examen(Base):
    
    matiere: str
    date_exam: date
    promotion: Promotion
    nom: str

    def __init__(self, nom: str, matiere: str, date_exam: date, promotion: Promotion) -> None:
        self.nom = nom
        self.matiere = matiere
        self.date_exam = date_exam
        self.promotion = promotion

    def __str__(self) -> str:
        return f'{self.nom} ({self.matiere})'

    def __hash__(self):
        return hash(('Examen', self.nom,self.matiere, self.date_exam))

    def __eq__(self,other: object) -> bool:
        return hash(self) == hash(other)

    def recuperer_notes(self) -> dict[Eleve, float]:
        # return {e: e.notes[self] for e in self.promotion.eleves if self in e.notes}
        notes: dict[Eleve, float] = {}
        for e in self.promotion.eleves:
            if self in e.notes:
                notes[e] = e.notes[self]
        return notes

    def min(self) -> float:
        return min(self.recuperer_notes().values())

    def max(self) -> float:
        return max(self.recuperer_notes().values())

    def calculer_moyenne(self) -> float:
        return mean(self.recuperer_notes().values())

    def to_dict(self) -> ExamenDict:
        return { 
                'nom': self.nom,
                'matiere': self.matiere,
                'date_exam': date.isoformat(self.date_exam),
                'hash': hash(self),
        }

    def from_dict(my_dict: ExamenDict, promo: 'Promotion') -> 'Examen':
        exam = Examen(nom="", matiere="", date_exam=date.today(), promotion=promo)

        return exam