import unittest
import mobilenumbers

class TestMobileNumberClean(unittest.TestCase):

    def test_clean_09space258_639258(self):
        self.assertEqual(mobilenumbers.clean('0(925)8032895'), '+639258032895')

    def test_clean_09space258_639258(self):
        self.assertEqual(mobilenumbers.clean('0 (925)8032895'), '+639258032895')

    def test_clean_639258space_639258(self):
        self.assertEqual(mobilenumbers.clean('63(925)8 032895'), '+639258032895')

    def test_clean_09258_639258(self):
        self.assertEqual(mobilenumbers.clean('0(925)8032895'), '+639258032895')

    def test_clean_09174_639174(self):
        self.assertEqual(mobilenumbers.clean('0(917)4998353'), '+639174998353')

    def test_clean_639174_639174(self):
        self.assertEqual(mobilenumbers.clean('63(917)4998353'), '+639174998353')

    def test_clean_5432then11digits_5432then11digits(self):
        self.assertEqual(mobilenumbers.clean('54(325)0123456789'), '+543250123456789')

    def test_clean_5432_5432(self):
        self.assertEqual(mobilenumbers.clean('54(325)432'), '+54325432')

    def test_clean_000925_63925(self):
        self.assertEqual(mobilenumbers.clean('000(925)8032895'), '+639258032895')

    def test_clean_630925_63925(self):
        self.assertEqual(mobilenumbers.clean('+63(0)09173010005'), '+639173010005')

    def test_clean_parentheses_without_parentheses(self):
        self.assertEqual(mobilenumbers.clean('0(925)8032895'), '+639258032895')

    def test_clean_63000925_63925(self):
        self.assertEqual(mobilenumbers.clean('63(000)9258032895'), '+639258032895')

    def test_clean_63000000925_63925(self):
        self.assertEqual(mobilenumbers.clean('63(000)0009258032895'), '+639258032895')

    def test_clean_empty_none(self):
        self.assertEqual(mobilenumbers.clean(''), None)

if __name__ == '__main__':
    unittest.main()

