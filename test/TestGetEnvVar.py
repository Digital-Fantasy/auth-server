import unittest
import utils

class TestGetEnvVar(unittest.TestCase):
    """This test suite tests the functions that give access to the config file"""

    def test_existed_var(self):
        """This function tests if the config file for the translation server exists"""
        self.assertIsInstance(utils.get_env_var("FLASKKEY"), str, "get_env_var() could not find a flask Key")

    def test_nonexisted_var(self):
        """This function tests if the get_conf function returns a dictionary with the config file"""
        self.assertIsInstance(utils.get_env_var("EnvVarThatDoesNotExist"), type(None), "Did not return None when asking for env var that did not exist")