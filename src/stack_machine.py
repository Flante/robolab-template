#!/usr/bin/env python3

from enum import IntEnum
from typing import Callable, Tuple
# IMPORTANT NOTE: DO NOT IMPORT THE ev3dev.ev3 MODULE IN THIS FILE

class SMState(IntEnum):
	""" Return codes for the stack machine """
	RUNNING = 1
	STOPPED = 2
	ERROR   = 3

class StackMachine:
	"""Implements the stack machine according to the specification """

	def __init__(self, callback: Callable[[bool], None]) -> None:
		""" Initialises the stack machine by setting its overflow flag and its callback function for the CHK instruction.

		:param callback: function
		"""
		self.callback = callback
		self.overflow = False

	def do(self, codeWord: Tuple[int,int,int,int,int]) -> SMState:
		"""
		Processes the entered code word by either executing the instruction or pushing the operand on the stack.

		:param codeWord: 5-tuple
		:returns: SMState
		"""
		# implementation
		pass

	def top(self) -> Tuple[int,int,int,int,int,int,int,int]:
		"""
		Returns the top element of the stack.

		:returns: 8-tuple or None
		"""
		# implementation
		pass
