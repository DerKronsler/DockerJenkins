import unittest
from RPGGame import Charakter, Gegner
from unittest.mock import patch
import random

class TestCharakter(unittest.TestCase):

    def setUp(self):
        self.charakter = Charakter("Held", 30, 8, 5)
        self.gegner = Gegner("Zombie", 20, 6, 3)

    def test_schadenNehmen(self):
        self.charakter.schadenNehmen(5)
        self.assertEqual(self.charakter.hp, 25)

    def test_istAmLeben(self):
        self.assertTrue(self.charakter.istAmLeben())
        self.charakter.schadenNehmen(30)
        self.assertFalse(self.charakter.istAmLeben())

    def test_levelAufstieg(self):
        self.charakter.levelAufstieg()
        self.assertEqual(self.charakter.level, 2)
        self.assertEqual(self.charakter.angriff, 10)
        self.assertEqual(self.charakter.verteidigung, 6)
        self.assertEqual(self.charakter.hp, 40)

    def test_erfahrungSammeln(self):
        self.charakter.erfahrungSammeln(10)
        self.assertEqual(self.charakter.erfahrung, 0)
        self.assertEqual(self.charakter.level, 2)

    def test_gegnerAngreifen(self):
        self.charakter.gegnerAngreifen(self.gegner)
        self.assertEqual(self.gegner.hp, 15)

class TestKampf(unittest.TestCase):

    def setUp(self):
        self.spieler = Charakter("Held", 30, 8, 5)
        self.gegner = Gegner("Zombie", 20, 6, 3)

    def test_kampf_sieg(self):
        self.spieler.gegnerAngreifen(self.gegner)
        self.gegner.gegnerAngreifen(self.spieler)
        self.spieler.gegnerAngreifen(self.gegner)
        self.assertTrue(self.spieler.istAmLeben())
        self.assertFalse(self.gegner.istAmLeben())
        self.spieler.erfahrungSammeln(5)
        self.assertEqual(self.spieler.erfahrung, 5)

    def test_kampf_niederlage(self):
        self.spieler.hp = 1
        self.gegner.angriff = 10
        self.gegner.gegnerAngreifen(self.spieler)
        self.assertFalse(self.spieler.istAmLeben())

if __name__ == '__main__':
    unittest.main()
