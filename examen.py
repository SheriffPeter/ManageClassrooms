from datetime import date
import typing

if typing.TYPE_CHECKING:
    from promotion import Promotion
    from eleve import Eleve

class Examen:

    def __init__(self, nom: str, matiere: str, date_exam: date, promotion: 'Promotion') -> None:
        self.nom:str = nom
        self.matiere:str = matiere
        self.date_exam: date = date_exam
        self.promotion: 'Promotion' = promotion

    def __str__(self) -> str:
        return f'Examen {self.nom} de {self.matiere} du {self.date_exam}, promo {self.promotion}'

    def __repr__(self) -> str:
        return f'<{type(self).__name__} object: {self.nom}{self.matiere}{self.date_exam}{self.promotion}>'

    def calculer_moyenne(self) -> float:
        """
        compute the average of all notes if this specific exam
        """
        #we need to get all the notes from all the students of the given promo that passed that specific exam
        # get all the notes of that exam.
        nb: int = 0
        sum_notes: float = 0.0
        for e in self.promotion.eleves:
            if self in e.notes.keys():
                nb += 1
                sum_notes += e.notes[self]
        
        if nb > 0:
            return sum_notes / nb
        else : 
            return -1.0 # make exception


    def min(self) -> float:
        exam_notes = self.recuperer_notes()

        return min(exam_notes.values())

    def max(self) -> float:
        exam_notes: dict['Eleve', float] = self.recuperer_notes()

        return max(exam_notes.values())

    def recuperer_notes(self) -> dict['Eleve', float]:
        exam_notes: dict['Eleve', float] = {}
        for e in self.promotion.eleves:
            if self in e.notes.keys():
                exam_notes[e] = e.notes[self]
        return exam_notes

if __name__ == "__main__":
    pass