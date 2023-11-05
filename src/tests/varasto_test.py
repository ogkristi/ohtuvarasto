import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def test_konstruktori_negatiivinen_tilavuus(self):
        varasto = Varasto(-1)
        
        self.assertAlmostEqual(varasto.tilavuus, 0)
        
    def test_konstruktori_negatiivinen_saldo(self):
        varasto = Varasto(10,-1)
        
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_konstruktori_ylivuoto(self):
        varasto = Varasto(10,11)

        self.assertAlmostEqual(varasto.saldo, 10)
    
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_negatiivinen(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertEqual(self.varasto.saldo, 0)
    
    def test_lisays_ylivuoto(self):
        self.varasto.lisaa_varastoon(11)

        self.assertEqual(self.varasto.saldo, 10)
        
    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_negatiivinen(self):
        saatu_maara = self.varasto.ota_varastosta(-5)

        self.assertEqual(saatu_maara, 0)

    def test_ottaminen_kaikki(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(100)

        self.assertEqual(saatu_maara, 8)
        self.assertEqual(self.varasto.saldo, 0)
    
    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_str(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
