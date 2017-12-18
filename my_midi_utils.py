# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 20:56:00 2015

@author: Ilia
"""

import struct
def GetTicksPerBeat(midi_file):
    ticks_per_beat = struct.unpack('>H',midi_file.header.ticksPerBeat)
    return ticks_per_beat[0]
