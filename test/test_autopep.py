import unittest
import autopep8
import subprocess
class Testing(unittest.TestCase):
    def test_pepexample(self):
        #Converting code into pep8 style
        subprocess.check_output('autopep8 --in-place --aggressive --aggressive autopep_test.py')
        try:
            #checking the code against pep8
            subprocess.check_output('pep8 --first autopep_test.py')
            status = 0
        except:
            status = 1
        self.assertEqual(status,0)
unittest.main()

