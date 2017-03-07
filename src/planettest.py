#!/usr/bin/env python3

import unittest
from Planet import Direction, Planet


class PlanetTestCase(unittest.TestCase):
	def setUp(self):
		self.planet = Planet()


class FirstPlanet(PlanetTestCase):
	# +--+
	# |  |
	# +-0,3------+
	#    |       |
	#   0,2-----2,2 (target)
	#    |      /
	# +-0,1    /
	# |  |    /
	# +-0,0-1,0
	#    |
	# (start)

	def test_empty_planet(self):
		self.assertEqual(self.planet.shortest_path((0,0),(1,2)), None)

	def test_target_not_reachable(self):
		self.planet.add_path((0,0,Direction.North), (0,1,Direction.South))
		self.assertEqual(self.planet.shortest_path((0,0),(1,2)), None)

	def test_target_not_reachable_with_loop(self):
		self.planet.add_path((0, 1, Direction.West), (0, 0, Direction.West))
		self.assertIsNone(self.planet.shortest_path((0, 0), (1, 2)))

	def test_shortest_path(self):
		self.planet.add_path((0, 0, Direction.East), (1, 0, Direction.West))
		self.planet.add_path((0, 1, Direction.North), (0, 2, Direction.South))
		self.planet.add_path((0, 2, Direction.North), (0, 3, Direction.South))
		self.planet.add_path((0, 2, Direction.East), (2, 2, Direction.West))
		self.planet.add_path((0, 3, Direction.North), (0, 3, Direction.West))
		self.planet.add_path((0, 3, Direction.East), (2, 2, Direction.North))
		self.planet.add_path((1, 0, Direction.North), (2, 2, Direction.South))
		self.assertEqual(self.planet.shortest_path((0, 0), (2, 2)), [(0,0,Direction.East), (1,0,Direction.North), (2,2,Direction.South)])


if __name__ == "__main__":
	unittest.main()
