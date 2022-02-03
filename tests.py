import unittest
import subprocess
import os

class TestActiveCookie(unittest.TestCase):

     def test_recent_cookie_1(self):
         self.assertEqual(subprocess.check_output("python func.py 'most_active_cookie cookie_log.csv' -d 2018-12-09", shell=True, universal_newlines=True), 'AtY0laUfhglK3lC7\n')

     def test_recent_cookie_2(self):
         self.assertEqual(subprocess.check_output("python func.py 'most_active_cookie cookie_log.csv' -d 2018-12-08", shell=True, universal_newlines=True), 'SAZuXPGUrfbcn5UA\n4sMM2LxV07bPJzwf\nfbcn5UAVanZf6UtG\n')

     def test_recent_cookie_3(self):
         self.assertEqual(subprocess.check_output("python func.py 'most_active_cookie cookie_log.csv' -d 2018-12-07", shell=True, universal_newlines=True), '4sMM2LxV07bPJzwf\n')

     def test_not_enough_arguments_1(self):
         try:
            subprocess.check_output("python func.py", shell=True, universal_newlines=True)
         except subprocess.CalledProcessError as e:
            self.assertEqual(e.returncode, 1)

     def test_not_enough_arguments_2(self):
         try:
            subprocess.check_output("python func.py 'most_active_cookie cookie_log.csv'", shell=True, universal_newlines=True)
         except subprocess.CalledProcessError as e:
            self.assertEqual(e.returncode, 1)       

     def test_not_enough_arguments_3(self):
         try:
            subprocess.check_output("python func.py 'most_active_cookie cookie_log.csv' -d", shell=True, universal_newlines=True)
         except subprocess.CalledProcessError as e:
            self.assertEqual(e.returncode, 1)

     def test_invalid_file(self):
         try:
            subprocess.check_output("python func.py 'non_existent_file.csv' -d", shell=True, universal_newlines=True)
         except subprocess.CalledProcessError as e:
            self.assertEqual(e.returncode, 1)

     def test_wrong_flag_option(self):
         try:
            subprocess.check_output("python func.py 'most_active_cookie cookie_log.csv' -f 2018-12-07", shell=True, universal_newlines=True)
         except subprocess.CalledProcessError as e:
            self.assertEqual(e.returncode, 1)

if __name__ == '__main__':
    unittest.main()
