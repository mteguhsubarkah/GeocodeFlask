import unittest 
from measureDistance import measureDistance

MOSCOW_RING_ROAD_Latitude = 55.766557
MOSCOW_RING_ROAD_Longitude = 37.623429

class TestMeasureDistance(unittest.TestCase):
	"""docstring for TestMeasureDistance"""
	def test_distance(self):
		self.assertAlmostEqual(measureDistance(MOSCOW_RING_ROAD_Latitude,MOSCOW_RING_ROAD_Longitude), 0)

	def test_type(self):
		self.assertRaises(TypeError, measureDistance, (3 + 5j,3 + 5j))
		self.assertRaises(TypeError, measureDistance, (True,True))
		self.assertRaises(TypeError, measureDistance, "TEST")
		