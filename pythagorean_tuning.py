# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 19:01:26 2015

@author: Ilia
"""

def circle_of_fifths(root_note):
    notes = [root_note + i*7 for i in range(0,12)]
    return(notes)

def pythagorean_scale(root_note):
    notes = [root_note + x for x in [i*7 % 12 for i in range(0,12)]]
    return notes

pythagorean_12_notes = pythagorean_scale(0)
circle_of_fifths_single = circle_of_fifths(0)


class PythagoreanScale(object):
    def __init__(self,root):
        self.root = root    
    def __getitem__(self,num):
        return self.root + pythagorean_12_notes[num%12] + num/12 * 12
    def __str__(self):
        return 'PythagoreanScale_{root}' \
                    .format(**self.__dict__)

if __name__ == '__main__':
    root = 40
    notes_cof = circle_of_fifths(root)
    notes_pyt = pythagorean_scale(root)
    print(notes_pyt)

class IntervalScale(object):
    def __init__(self,interval,number_of_notes,root):
        self.interval = interval
        self.basic_scale = range(0,number_of_notes*interval,interval)
        self.normalized_scale = [x % 12 for x in self.basic_scale]
        self.root = root
        self.number_of_notes = number_of_notes
    def __getitem__(self,num):
        return self.root + \
        self.normalized_scale[num % self.number_of_notes] + \
        num/self.number_of_notes * 12
    def __str__(self):
        return 'IntervalScale_{interval}_{number_of_notes}_{root}' \
                    .format(**self.__dict__)

class OrderedScale(object):
    def __init__(self,root,normalized_scale):
        self.root = root
        self.number_of_notes = len(normalized_scale)
        self.normalized_scale = normalized_scale
    def __getitem__(self,num):
        return self.root + \
        self.normalized_scale[num % self.number_of_notes] + \
        num/self.number_of_notes * 12
    def __str__(self):
        return type(self).__name__ + '_' + str(self.root)

class MajorScale(OrderedScale):
    def __init__(self,root):
        super(MajorScale,self).__init__(root,[0,2,4,5,7,9,11])
#    def __str__(self):
#        return 'MajorScale_{root}' \
#                    .format(**self.__dict__)

class MinorScale(OrderedScale):
    def __init__(self,root):
        super(MinorScale,self).__init__(root,[0,2,3,5,7,8,10])
#    def __str__(self):
#        return 'MinorScale_{root}' \
#                    .format(**self.__dict__)

class MajorPentatonicScale(OrderedScale):
    def __init__(self,root):
        super(MajorPentatonicScale,self).__init__(root,[0,2,4,7,9])
#    def __str__(self):
#        return 'MajorPentatonicScale_{root}'.format(self.root)

class MinorPentatonicScale(OrderedScale):
    def __init__(self,root):
        super(MinorPentatonicScale,self).__init__(root,[0,3,5,7,10])
#    def __str__(self):
#        return 'MinorPentatonicScale_{root}'.format(self.root)


