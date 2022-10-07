class GestionNotesException(Exception):
    pass


class EleveExistant(GestionNotesException):
    pass


class EleveInexistant(GestionNotesException):
    pass


class ExamenAffecte(GestionNotesException):
    pass


class ExamExistant(GestionNotesException):
    pass


class ExamInexistant(GestionNotesException):
    pass


class NoteIncorrecte(GestionNotesException, ValueError):
    pass


class EleveSansPromotion(GestionNotesException):
    pass


class ExamenIncorrect(GestionNotesException):
    pass
