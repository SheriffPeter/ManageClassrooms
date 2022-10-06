import typing

if typing.TYPE_CHECKING:
    from eleve import Eleve
    from examen import Examen

class Promotion:

    def __init__(self, prof: str, annee: int, niveau: str) -> None:
        self.prof:str = prof
        self.annee:int = annee
        self.niveau:str = niveau

        self.eleves: list['Eleve'] = []
        self.examens: list['Examen'] = []

    def __str__(self) -> str:
        return f'Promotion {self.niveau}.{self.annee} de {self.prof}'

    def __repr__(self) -> str:
         return f'<{type(self).__name__} object: {self.niveau}.{self.annee}{self.prof}>'

    def ajouter_eleve(self, el: 'Eleve') -> None:
        self.eleves.append(el)
        el.promotion = self

    def ajouter_examen(self, exam: 'Examen') -> None:
        self.examens.append(exam)
        exam.promotion = self

    def calculer_moyenne(self) ->  float:
        sum: float = 0.0
        for e in self.eleves:
            sum += e.calculer_moyenne()

        return sum / len(self.eleves)

    def retirer_eleve(self, el: 'Eleve') -> None:
        el.promotion = None
        self.eleves.remove(el)

    def retirer_examen(self, exam: 'Examen') -> None:
        for e in self.eleves:
            for n in e.notes.keys():
                if exam is n:
                    return # throw exception

        self.examens.remove(exam)

    def retirer_notes(self, exam: 'Examen') -> None:
        for e in self.eleves:
            for n in e.notes.keys():
                if exam is n:
                    del e.notes[n]

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