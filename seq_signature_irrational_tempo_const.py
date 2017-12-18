# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 20:39:34 2015

@author: Ilia
"""

import pythagorean_tuning
reload(pythagorean_tuning)
from pythagorean_tuning import *

my_root = 30
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
theta = 2**0.5/2

from generate_irrational_signature import *
max_c = 90
max_d = 90
signature,dn = GetClippedSignature(theta,max_c,max_d,ret_d=True)
#seq_notes = [use_scale[x[1]] for x in seq]

root_notes = np.where(signature==0)[0]
root_notes = np.concatenate((root_notes,np.array([len(signature)])))
time_between_roots = np.array(np.diff(root_notes),dtype=np.float)

fname_base = 'signature_irrational_tempo_norm_%.4f' % theta

root_duration = 8.0 #two bars

root_interval_ind = -1
time_since_root = 0
this_time = 0.0
note_durations = []
note_times = []
elongation_factor = 1.5
for i in xrange(len(signature)):
    if signature[i] == 0:
        root_interval_ind += 1
        time_since_root = 0
        this_time = root_interval_ind * root_duration
        note_durations.append(root_duration/elongation_factor)
        note_times.append(this_time)
        this_root_interval = time_between_roots[root_interval_ind]
    else:
        this_duration = root_duration/this_root_interval
        time_since_root+=1
        this_time += this_duration
        note_durations.append(this_duration)
        note_times.append(this_time)

seq_notes = [use_scale[x] for x in signature]
for i in xrange(len(seq_notes)):
    if seq_notes[i]>=0 and seq_notes[i]<=127:
#        mf1.addNote(0,0,seq_notes[i],i*duration,duration*2,velocity)
#        mf1.addNote(0,0,seq_notes[i],note_times[i],note_durations[i]*elongation_factor,velocity)
        mf1.addNote(0,0,seq_notes[i],note_times[i],0.25,velocity)

out_fname = fname_base + '_' + str(use_scale) + '.midi'
with open(out_fname,'wb') as f:
    mf1.writeFile(f)

