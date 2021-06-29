import unittest 
from getCoordinate import getCoordinate


class TestMeasureDistance(unittest.TestCase):
	"""docstring for TestMeasureDistance"""
	def test_type(self):
		self.assertRaises(TypeError, getCoordinate, 10)
		self.assertRaises(TypeError, getCoordinate, True)
		self.assertRaises(TypeError, getCoordinate, "TestFileName")
		