# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 20:39:34 2015

@author: Ilia
"""

import pythagorean_tuning
reload(pythagorean_tuning)
from pythagorean_tuning import *

my_root = 40
pyts = IntervalScale(7,12,my_root)
scale2 = IntervalScale(7,7,my_root)
scale3 = IntervalScale(1,12,my_root)
scale4 = MinorScale(my_root)
scale5 = MajorPentatonicScale(my_root)
scale6 = MajorScale(my_root)
#use_scale = pyts
#use_scale = PythagoreanScale(my_root)
use_scale = scale5
#use_scale = pythagorean_tuning.MinorScale(my_root)

from midiutil.MidiFile3 import MIDIFile
mf1 = MIDIFile(1)

from my_midi_utils import GetTicksPerBeat
ticks_per_beat = GetTicksPerBeat(mf1)

duration = 0.25
velocity=100

#fname = 'A000010 - euler_phi.txt'
#pathname = 'source_txt/'
##fname = '3x plus 1 - A006577.txt'
##fname = 'Karl Aage Rasmussen - build up - ascending - A056239.txt'
##fname = 'fractal - A025480 - other_version.txt'
#import numpy as np
#seq = np.loadtxt(pathname+fname,dtype=np.int)
#
##seq_notes = [use_scale[x] for x in seq_A108618]
#seq_notes = [use_scale[x[1]] for x in seq]
#print seq_notes

#theta=2**(1./3)/2
#theta = np.pi/4
#theta = 3**0.5/2
#theta = 2**0.5/2
#theta = 6**0.5/3
#theta = np.e/6 #e seems to always be somewhat monotonic
#theta = 11**0.5/4
#theta = 2**0.25*3/4
#theta = 0.7
#theta = 3**0.5-1
theta = 3./4

from generate_irrational_signature import MakeIrrationalSignature
signature = MakeIrrationalSignature(theta,0,40,0,40)
#seq_notes = [use_scale[x[1]] for x in seq]
seq_notes = [use_scale[x] for x in signature]

fname_base = 'signature_irrational_%.4f' % theta

for i in xrange(len(seq_notes)):
    if seq_notes[i]>=0 and seq_notes[i]<=127:
        mf1.addNote(0,0,seq_notes[i],i*duration,duration*2,velocity)
    
#import re

out_fname = fname_base + '_' + str(use_scale) + '.midi'
with open(out_fname,'wb') as f:
    mf1.writeFile(f)

