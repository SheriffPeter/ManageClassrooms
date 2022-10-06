from datetime import date
import typing

if typing.TYPE_CHECKING:
    from promotion import Promotion
    from examen import Examen


class Eleve:

    def __init__(self, nom: str, prenom: str, date_naissance: date) -> None:
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        
        self.promotion: typing.Optional['Promotion'] = None
        self.notes: dict['Examen', float] = {}

    def __str__(self) -> str:
        ret: str =  f"L'eleve {self.prenom} {self.nom.upper()} est né en {self.date_naissance}."
        if self.promotion is None:
            ret += f"\nIl n'a pas encore été inscrit dans une classe."
        else:
            ret += f"\nIl est dans la promotion {self.promotion.niveau}.{self.promotion.annee}"
        
        if len(self.notes):
            ret += f"\nIl a {len(self.notes)}"

        ret += "\n"
        return ret

    def __repr__(self) -> str: 
        return f'<{type(self).__name__} object: {self.prenom.lower()}{self.nom.lower()}>'

    def __gt__(self, other: 'Eleve') -> bool:
        return self.calculer_moyenne() > other.calculer_moyenne()

    def __lt__(self, other: 'Eleve') -> bool:
        return self.calculer_moyenne() < other.calculer_moyenne()

    def __ge__(self, other: 'Eleve') -> bool:
        return self.calculer_moyenne() >= other.calculer_moyenne()

    def __le__(self, other: 'Eleve') -> bool:
        return self.calculer_moyenne() <= other.calculer_moyenne()

    def __eq__(self, other: typing.Any) -> bool:
        if not other.calculer_moyenne:
            return False
        return self.calculer_moyenne() == other.calculer_moyenne()

    def __ne__(self, other: typing.Any) -> bool:
        if not other.calculer_moyenne:
            return True
        return self.calculer_moyenne() != other.calculer_moyenne()

    def __hash__(self) -> int:
        return hash(('eleve.Eleve', self.nom))

    def calculer_moyenne(self) -> float:
        if not len(self.notes):
            pass # throw exception
        sum: float = 0.0
        for _, n in self.notes.items():
            sum += n
        return sum / len(self.notes)

    def ajouter_note(self,exam: 'Examen', note: float) -> None:
        if not (0.0 < note < 20.0):
            pass # throw exception
        elif not self.promotion or exam not in self.promotion.examens:
            pass # throw exception

        if exam in self.notes.keys():
            return # throw already existing exception

        self.notes[exam] = note


    def modifier_note(self,exam: 'Examen', note: float) -> None:
        if not (0.0 < note < 20.0):
            pass # throw exception
        
        self.notes[exam] = note


if __name__ == "__main__":
    pass