from statistics import StatisticsError, mean
from typing import TYPE_CHECKING, Iterable

from . import Base, exceptions

if TYPE_CHECKING:
    from . import Eleve, Examen


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
