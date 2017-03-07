from enum import Enum, unique
from typing import List, Optional, Tuple


@unique
class Direction(Enum):
	North = 0
	East  = 1
	South = 2
	West  = 3


class Planet:
	def __init__(self):
		pass

	# example: add_path((0, 3, Direction.North), (0, 3, Direction.West))
	def add_path(self, start: Tuple[int,int,Direction], target: Tuple[int,int,Direction]):
		"""add a path to the map"""
		pass

	# example: shortest_path((0,0), (2,2)) returns: [(0, 0, Direction.East), (1, 0, Direction.North), (2, 2, Direction.South)]
	# example: shortest_path((0,0), (1,2)) returns: None
	def shortest_path(self, start: Tuple[int,int], target: Tuple[int,int]) -> Optional[List[Tuple[int,int,Direction]]]:
		"""return a shortest path between two crossings"""
		pass
