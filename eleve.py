"""
un eleve file
"""

import typing
from datetime import date

#On met ça pour éviter les import circulaires
if typing.TYPE_CHECKING:
    from promotion import Promotion
    from examen import Examen

class Eleve:
    """
    Our Eleve class
    """

    def __init__(self, nom: str, prenom: str, date_naissance: date) -> None:
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.promotion: typing.Optional['Promotion'] = None
        self.notes: dict['Examen', float] = {}

    def __str__(self) -> str:
        """ Comment voulons nous afficher un eleve en string """
        ret: str =  f"L'eleve {self.prenom} {self.nom.upper()} est né en {self.date_naissance}."
        if self.promotion is None:
            ret += "\nIl n'a pas encore été inscrit dans une classe."
        else:
            ret += f"\nIl est dans la promotion {self.promotion.niveau}.{self.promotion.annee}"
        if len(self.notes):
            ret += f"\nIl a {len(self.notes)}"
        ret += "\n"
        return ret


    def __repr__(self) -> str: 
        """ Representation interne d'un objet """
        return f'<{type(self).__name__} object: {self.prenom.lower()}{self.nom.lower()}>'

    def __gt__(self, other: 'Eleve') -> bool:
        return self.calculer_moyenne() > other.calculer_moyenne()

    def __lt__(self, other: 'Eleve') -> bool:
        return self.calculer_moyenne() < other.calculer_moyenne()

    def __ge__(self, other: 'Eleve') -> bool:
        return self.calculer_moyenne() >= other.calculer_moyenne()

    def __le__(self, other: 'Eleve') -> bool:
        return self.calculer_moyenne() <= other.calculer_moyenne()


#################################################################
    # What is the need to redefine eq and ne?????"""

    #redéfinir un __eq__ nécessite toujours de redéfinir la fonction __hash__
    # def __eq__(self, other: typing.Any) -> bool:
    #     if not other.calculer_moyenne:
    #         return False
    #     return self.calculer_moyenne() == other.calculer_moyenne()

    # def __ne__(self, other: typing.Any) -> bool:
    #     if not other.calculer_moyenne:
    #         return True
    #     return self.calculer_moyenne() != other.calculer_moyenne()
###################################################################
    def __hash__(self) -> int:
        """ Eleve n'était plus iterable car ça dépend de ses atrributs interne
            S'il y a des attributes non hashsables la fonction hash qui utilise le hash des attributs
            et ainsi de suite récursivement ne fonctionne plus.
            Il faut la redéfinir nous mêmes pour éviter ce pb. Le mieux est de créer un tuple comme suit.
            """
        return hash(('eleve.Eleve', self.nom))

    def calculer_moyenne(self) -> float:
        """
        calculer_moyenne
        """
        breakpoint()
        if len(self.notes) == 0:
            pass # throw exception
        sum_notes: float = 0.0
        for n in self.notes.values():
            sum_notes += n
        # sum_notes = sum(self.notes.values())
        return sum_notes / len(self.notes)
        # return mean(self.notes.values())

    def ajouter_note(self,exam: 'Examen', note: float) -> None:
        if not (0.0 < note < 20.0):
            pass # throw exception
        elif not self.promotion or exam not in self.promotion.examens:
            pass # throw exception

        if exam in self.notes.keys():
            return # throw already existing exception

        self.notes[exam] = note


    def modifier_note(self,exam: 'Examen', note: float) -> None:
        """
        update notes
        """
        if not (0.0 < note < 20.0):
            pass # throw exception
        
        self.notes[exam] = note


if __name__ == "__main__":
    pass