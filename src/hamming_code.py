#!/usr/bin/env python3

from enum import IntEnum
from typing import Tuple
# IMPORTANT NOTE: DO NOT IMPORT THE ev3dev.ev3 MODULE IN THIS FILE

class HCResult(IntEnum):
	""" Return codes for the Hamming Code interface """
	VALID         = 1
	CORRECTED     = 2 # whenever ANY bit has been corrected
	UNCORRECTABLE = 3

class HammingCode:
	""" Provides decoding capabilities for the specified Hamming Code """

	def decode(self, encodedWord: Tuple[int,int,int,int,int,int,int,int,int,int]) -> Tuple[Tuple[int,int,int,int,int], HCResult]:
		"""
		Checks the channel alphabet word for errors and attempts to decode it.

		:returns: (5-tuple, HCResult) or (None, HCResult)
		"""
		# implementation
		pass
