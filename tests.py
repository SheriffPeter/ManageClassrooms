"""
Our integration test case file
"""
import unittest
from datetime import date
from promotion import Promotion
from eleve import Eleve

def division(n1: int, n2: int) -> float:
    """
    Une simple division
    """
    # n2 += 1 if n2%2==0 else n2
    return  n1 / n2

class BasicTestCase(unittest.TestCase):
    """
    .
    """
    def test_truc(self):
        """
        .
        """
        self.assertEqual('a','b',msg = "Les a ne sont pas identiques entre eux")

    def test_division(self):
        res = division(10,5)
        self.assertEqual(res, 2)

    def test_division_par_zero(self):
        # res = False
        # try:
        #     division(1,0)
        # except ZeroDivisionError:
        #     res = True
        # self.assertTrue(res, msg="La divisio par zéro a bien planté")
        with self.assertRaises(ZeroDivisionError):
            division(1,0)

    def test_divsion_10_3(self):
        """
        tester division pour résultat infini
        """
        self.assertEqual(round(division(10,3),5), 3.33333)
        self.assertEqual(division(10,3),10/3)

    def test_division_float(self):
        """
        Test avec result en float < 0
        
        """
        self.assertEqual(division(5,10), 0.5)


class GestionNoteTestCase(unittest.TestCase):
    
    def setUp(self) -> None:
        """
        On va créer un contexte de promotion utilisable pour du test
        """
        eleve1 = Eleve(nom="marchal", prenom="pierre", date_naissance=date.today())
        eleve1.notes = {"e":12.0, "x": 10.0, "y": 8.0}
        eleve2 = Eleve(nom="coucou", prenom="hello", date_naissance=date.today())
        eleve2.notes = {"e":3.5, "x": 9.4, "y": 13.2}
        eleve3 = Eleve(nom="pzeioufh   ", prenom="ded", date_naissance=date.today())
        eleve3.notes = {"e": 12.4, "x": 7.9}
        self.eleves = [eleve1,eleve2, eleve3]

    def tearDown(self) -> None:
        del self.eleves

    def test_calculer_moyenne_eleve(self):
        self.assertEqual(self.eleves[0].calculer_moyenne(), 10.0)
        self.assertEqual(round(self.eleves[1].calculer_moyenne(),2), 8.7)
        self.assertEqual(self.eleves[2].calculer_moyenne(), 10.15)

    def test_retrait_eleve(self):
        """
        On test le retrait d'un eleve
        Il nous faut un dejà un eleve dans une promo. ON vérifie que
        l'élève est bien dans la promo.
        on retire l'élève
        on chekc élève pas dans la promo ET on check eleve.promo is None
        """
        promo = Promotion("prof", 2022, "EI")
        promo.eleves.append(self.eleves[0])
        promo.eleves.append(self.eleves[1])
        promo.eleves.append(self.eleves[2])

        self.assertEqual(len(promo.eleves),3)

        promo.retirer_eleve(self.eleves[0])
        self.assertNotIn(self.eleves[0], promo.eleves)
        self.assertEqual(len(promo.eleves),2)


    def test_ajout_eleve_et_moyenne_promo(self):
        pass