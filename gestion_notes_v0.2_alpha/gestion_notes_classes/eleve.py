from datetime import date
from statistics import mean
from typing import TYPE_CHECKING, Optional, TypedDict
from . import Base, exceptions


if TYPE_CHECKING:
    from . import Examen, Promotion


class EleveDict(TypedDict):
    nom: str
    prenom: str
    date_naissance: str
    notes: list[tuple[int, float]]


class Eleve(Base):
    
    nom: str
    prenom: str
    date_naissance: date
    promotion: Optional['Promotion'] = None
    notes: dict['Examen', float]

    def __init__(self, nom: str, prenom: str, date_naissance: date):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.notes = {}

    def __str__(self) -> str:
        return f'{self.prenom} {self.nom.upper()}'

    def __ge__(self, other: 'Eleve') -> bool:
        return self.calculer_moyenne() >= other.calculer_moyenne()

    def __gt__(self, other: 'Eleve') -> bool:
        return self.calculer_moyenne() > other.calculer_moyenne()

    def __le__(self, other: 'Eleve') -> bool:
        return self.calculer_moyenne() <= other.calculer_moyenne()

    def __lt__(self, other: 'Eleve') -> bool:
        return self.calculer_moyenne() < other.calculer_moyenne()

    def ajouter_note(self, exam: 'Examen', note: float) -> None:
        if not (0 <= note <= 20):
            raise exceptions.NoteIncorrecte(note)
        if self.promotion is None:
            raise exceptions.EleveSansPromotion(self)
        if exam not in self.promotion.examens:
            raise exceptions.ExamenIncorrect(f'La promotion {self.promotion} ne contient pas l\'examen {exam}')
        if exam in self.notes:
            raise exceptions.ExamenIncorrect(f'{self} a déjà une note pour {exam}')
        self.notes[exam] = note

    def modifier_note(self, exam: 'Examen', note: float) -> None:
        if not (0 <= note <= 20):
            raise exceptions.NoteIncorrecte(note)
        if exam not in self.notes:
            raise exceptions.ExamenIncorrect(f'{self} n\'a pas de note pour {exam}')
        self.notes[exam] = note


    def calculer_moyenne(self) -> float:
        return mean(self.notes.values())

    def to_dict(self) -> EleveDict:
        return {
            'nom': self.nom,
            'prenom': self.prenom,
            'date_naissance': date.isoformat(self.date_naissance),
            'notes': [(hash(e),n) for e,n in self.notes.items()],
        }