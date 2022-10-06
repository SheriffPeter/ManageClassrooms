
"""
Fichier des tests unitaires et d'intégration
"""

from datetime import date
from textwrap import dedent
from eleve import Eleve
from promotion import Promotion
from examen import Examen

#### Fonction générique ####


##### Test Eleve ####
def test_el_tu():
    """
    On essaie de tester untairement notre class Eleve
    C'et compliqué car toutes les classes doivent se connaitre
    """
    el = Eleve(nom = "marchal", prenom="Pierre", date_naissance=date(year=1990, month=2, day=23))
    assert el.nom == 'marchal'
    assert el.prenom == 'Pierre'
    assert el.promotion == None
    assert el.notes == None


def test_Eleve_str_no_promo(): 
    el = Eleve(nom = "marchal", prenom="Pierre", date_naissance=date(year=1990, month=2, day=23))
    assert dedent(str(el)).strip() == dedent("""L'eleve Pierre MARCHAL est né en 1990-02-23.\nIl n'a pas encore été inscrit dans une classe.""").strip()
                        
def test_Eleve_str_promo():
    el = Eleve(nom = "marchal", prenom="Pierre", date_naissance=date(year=1990, month=2, day=23))
    promo = Promotion(prof= "Teacher", annee= 2022, niveau= "Master")
    el.promotion = promo
    assert dedent(str(el)).strip() == dedent("""L'eleve Pierre MARCHAL est né en 1990-02-23.\nIl est dans la promotion Master.2022""").strip()


def test_moyenne():
    el = Eleve(nom = "marchal", prenom="Pierre", date_naissance=date(year=1990, month=2, day=23))
    promo = Promotion("Teacher", 2022, "Master")
    promo.ajouter_eleve(el)
    exam = Examen(nom= "partiel", \
                    matiere= "french", \
                    date_exam = date(year=1990, month=2, day=23),\
                    promotion= promo    )
    exam2 = Examen(nom= "partiel", \
                    matiere= "french", \
                    date_exam = date(year=1990, month=2, day=23),\
                    promotion= promo    )
    exam3 = Examen(nom= "partiel", \
                    matiere= "french", \
                    date_exam = date(year=1990, month=2, day=23),\
                    promotion= promo    )
    exam4 = Examen(nom= "partiel", \
                    matiere= "french", \
                    date_exam = date(year=1990, month=2, day=23),\
                    promotion= promo    )
    el.ajouter_note(exam, 10.0)
    el.ajouter_note(exam2, 12.0)
    el.ajouter_note(exam3, 8.0)
    assert el.calculer_moyenne() == 10.0
    el.ajouter_note(exam4, 5.3)
    assert el.calculer_moyenne() == 8.825

#### Test Examen ####
def test_TU_contruction():
    exam = Examen(nom="name", matiere="français", date_exam=date.today(), promotion=Promotion('prof',2022, "niveau"))
    assert exam.nom == "name"
    assert exam.matiere == "français"
    assert exam.date_exam == date.today()
    assert exam.promotion == Promotion('prof',2022, "niveau")


def test_calculer_exam_moyenne():
    el = Eleve(nom = "marchal", prenom="Pierre", date_naissance=date(year=1990, month=2, day=23))
    el2 = Eleve(nom = "coucou", prenom="coucou", date_naissance=date(year=1990, month=2, day=23))
    el3 = Eleve(nom = "bye", prenom="bye", date_naissance=date(year=1990, month=2, day=23))
    promo = Promotion("Teacher", 2022, "Master")
    promo.ajouter_eleve(el)
    promo.ajouter_eleve(el2)
    promo.ajouter_eleve(el3)
    exam = Examen(nom= "partiel", \
                    matiere= "french", \
                    date_exam = date(year=1990, month=2, day=23),\
                    promotion= promo    )
    promo.ajouter_examen(exam)
    el.ajouter_note(exam, 12.0)
    el2.ajouter_note(exam, 20.0)
    el3.ajouter_note(exam, 15.0)

    assert round(exam.calculer_moyenne(), 2) == 15.67

def test_recupérer_notes():
    el = Eleve(nom = "marchal", prenom="Pierre", date_naissance=date(year=1990, month=2, day=23))
    el2 = Eleve(nom = "coucou", prenom="coucou", date_naissance=date(year=1990, month=2, day=23))
    el3 = Eleve(nom = "bye", prenom="bye", date_naissance=date(year=1990, month=2, day=23))
    promo = Promotion("Teacher", 2022, "Master")
    promo.ajouter_eleve(el)
    promo.ajouter_eleve(el2)
    promo.ajouter_eleve(el3)
    exam = Examen(nom= "partiel", \
                    matiere= "french", \
                    date_exam = date(year=1990, month=2, day=23),\
                    promotion= promo    )
    promo.ajouter_examen(exam)
    el.ajouter_note(exam, 12.0)
    el2.ajouter_note(exam, 20.0)
    el3.ajouter_note(exam, 15.0)
    ret = exam.recuperer_notes()

    print(f"ret::{ret}")
    assert sorted(ret), sorted({el: 12.0, el2: 20.0, el3: 15.0})

def test_minimum():
    el = Eleve(nom = "marchal", prenom="Pierre", date_naissance=date(year=1990, month=2, day=23))
    el2 = Eleve(nom = "coucou", prenom="coucou", date_naissance=date(year=1990, month=2, day=23))
    el3 = Eleve(nom = "bye", prenom="bye", date_naissance=date(year=1990, month=2, day=23))
    promo = Promotion("Teacher", 2022, "Master")
    promo.ajouter_eleve(el)
    promo.ajouter_eleve(el2)
    promo.ajouter_eleve(el3)
    exam = Examen(nom= "partiel", \
                    matiere= "french", \
                    date_exam = date(year=1990, month=2, day=23),\
                    promotion= promo    )
    promo.ajouter_examen(exam)
    el.ajouter_note(exam, 12.0)
    el2.ajouter_note(exam, 20.0)
    el3.ajouter_note(exam, 15.0)

    assert exam.min() == 12.0
    

def test_maximum():
    el = Eleve(nom = "marchal", prenom="Pierre", date_naissance=date(year=1990, month=2, day=23))
    el2 = Eleve(nom = "coucou", prenom="coucou", date_naissance=date(year=1990, month=2, day=23))
    el3 = Eleve(nom = "bye", prenom="bye", date_naissance=date(year=1990, month=2, day=23))
    promo = Promotion("Teacher", 2022, "Master")
    promo.ajouter_eleve(el)
    promo.ajouter_eleve(el2)
    promo.ajouter_eleve(el3)
    exam = Examen(nom= "partiel", \
                    matiere= "french", \
                    date_exam = date(year=1990, month=2, day=23),\
                    promotion= promo    )
    promo.ajouter_examen(exam)
    el.ajouter_note(exam, 12.0)
    el2.ajouter_note(exam, 20.0)
    el3.ajouter_note(exam, 15.0)

    assert exam.max() == 20.0

#### Test Promotion ####

def test_calcul_classement():
    el = Eleve(nom = "marchal", prenom="Pierre", date_naissance=date(year=1990, month=2, day=23))
    el2 = Eleve(nom = "coucou", prenom="coucou", date_naissance=date(year=1990, month=2, day=23))
    el3 = Eleve(nom = "bye", prenom="bye", date_naissance=date(year=1990, month=2, day=23))
    promo = Promotion("Teacher", 2022, "Master")
    promo.ajouter_eleve(el)
    promo.ajouter_eleve(el2)
    promo.ajouter_eleve(el3)
    exam = Examen(nom= "partiel", \
                    matiere= "french", \
                    date_exam = date(year=1990, month=2, day=23),\
                    promotion= promo    )
    promo.ajouter_examen(exam)
    el.ajouter_note(exam, 12.0)
    el2.ajouter_note(exam, 20.0)
    el3.ajouter_note(exam, 15.0)

    ret = promo.calculer_classement()
    print(ret)
    assert ret == [(1,el2, 20.0),(2,el3, 15.0), (3, el, 12.0)]
