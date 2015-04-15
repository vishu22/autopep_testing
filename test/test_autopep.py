import unittest
import autopep8
import subprocess
import os

class Testing(unittest.TestCase):
    def test_pepexample(self):
        #Converting code into pep8 style
        path = os.getcwd() + '\\autopep_test.py'
        subprocess.check_output('autopep8 --in-place --aggressive --aggressive ' + path)
        try:
            #checking the code against pep8
            subprocess.check_output('pep8 --first autopep_test.py')
            status = 0
        except:
            status = 1
        self.assertEqual(status,0)

#unittest.main()