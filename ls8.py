#!/usr/bin/env python3

"""Main."""

import sys
from cpu2 import *

cpu = CPU()

cpu.load('hinter.ls8')
cpu.run()