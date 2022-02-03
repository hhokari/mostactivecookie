import unittest
import subprocess

class TestActiveCookie(unittest.TestCase):

     def test_recent_cookie_1(self):
         self.assertEqual(subprocess.check_output("python func.py 'most_active_cookie cookie_log.csv' -d 2018-12-09", shell=True, universal_newlines=True), 'AtY0laUfhglK3lC7\n')

     def test_recent_cookie_2(self):
         self.assertEqual(subprocess.check_output("python func.py 'most_active_cookie cookie_log.csv' -d 2018-12-08", shell=True, universal_newlines=True), 'SAZuXPGUrfbcn5UA\n4sMM2LxV07bPJzwf\nfbcn5UAVanZf6UtG\n')

     def test_recent_cookie_3(self):
         self.assertEqual(subprocess.check_output("python func.py 'most_active_cookie cookie_log.csv' -d 2018-12-07", shell=True, universal_newlines=True), '4sMM2LxV07bPJzwf\n')

if __name__ == '__main__':
    unittest.main()
