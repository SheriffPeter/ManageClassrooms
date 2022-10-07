"""
Promotion
"""
from statistics import mean
import typing
from eleve import Eleve

if typing.TYPE_CHECKING:
    from examen import Examen

class Promotion:
    """
    ma promotion
    """

    def __init__(self, prof: str, annee: int, niveau: str) -> None:
        self.prof:str = prof
        self.annee:int = annee
        self.niveau:str = niveau

        self.eleves: list[Eleve] = []
        self.examens: list['Examen'] = []

    def __str__(self) -> str:
        return f'Promotion {self.niveau}.{self.annee} de {self.prof}'

    def __repr__(self) -> str:
        return f'<{type(self).__name__} object: {self.niveau}.{self.annee}{self.prof}>'

    def ajouter_eleve(self, el: 'Eleve') -> None:
        """
        Ajouter un élève à une promotion
        """
        self.eleves.append(el)
        el.promotion = self

    def ajouter_examen(self, exam: 'Examen') -> None:
        """
        ajouter un examen à une promotion
        """
        self.examens.append(exam)
        exam.promotion = self

    def calculer_moyenne(self) ->  float:
        """
        Calcul la moyenne d'une promo
        """
        # sum_notes: float = 0.0
        # for e in self.eleves:
        #     sum_notes += e.calculer_moyenne()

        # return sum_notes / len(self.eleves)
        return mean([e.calculer_moyenne() for e in self.eleves if e.notes])
        # return statistics.mean(map(Eleve.calculer_moyenne, self.eleves))

    def retirer_eleve(self, elev: 'Eleve') -> None:
        """
            On doit pouvoir retirer un élève d'une promotion
        """
        elev.promotion = None
        self.eleves.remove(elev)

    def retirer_examen(self, exam: 'Examen') -> None:
        """
        Une promo peut se séparer d'un examen
        """
        for elev in self.eleves:
            for note in elev.notes.keys():
                if exam is note:
                    return # throw exception

        self.examens.remove(exam)

    def retirer_notes(self, exam: 'Examen') -> None:
        """
        Si l'on veut supprimer les notes de tous les élèves d'une promo correspondant à un examen
        """
        for elev in self.eleves:
            for note in elev.notes.keys():
                if exam is note:
                    del elev.notes[note]

    def calculer_classement(self) -> list[tuple[int,'Eleve', float]]:
        classement: list[tuple['Eleve', float]] = []
        for e in self.eleves:
            classement.append((e, e.calculer_moyenne()))
        classement = sorted(classement, key= lambda e: e[1],reverse= True)

        # We get the tuple eleve + note and we add the position 
        # we now just need to unpack the tuple of eleve,note
        # ret: list[tuple[int,'Eleve', float]] = []
        # for pos,(e,n) in list(enumerate(classement, start=1)):
        #     ret.append((pos,e,n))
        ret = [(p, c[0], c[1]) for p,c in enumerate(classement, start=1)]

        return ret


if __name__ == "__main__":
    pass