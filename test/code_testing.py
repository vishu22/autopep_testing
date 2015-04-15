import unittest
import autopep8
import subprocess
import os

class Testing(unittest.TestCase):
    def test_pepexample(self):
        #Converting code into pep8 style
        print os.getcwd()
        path = os.getcwd() + '/test/test_file.py'
        print os.path.exists(path)
        print path
        # os.system('autopep8 --in-place --aggressive --aggressive ' + path)
        try:
            #checking the code against pep8
            print 'rnu'
            os.system('pep8 --first ' + path)
            status = 0
        except:
            status = 1
            print "test case cleared"
        self.assertEqual(status,0)

#unittest.main()
