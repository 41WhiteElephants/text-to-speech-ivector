"""numpy-kaldi i/o interface
"""
import numpy as np


def ark2dict(arkfile):  
    	"""Kaldi archive (ark) to dictionnary of numpy arrays (~npz)
    	"""
	spk_ivec = {}
	with open(arkfile) as fin:
            	lines= fin.readlines()
		for line in lines:	
			#delete brackets
			line = line.replace("[", "").replace("]", "").split()
			spk_name = line[0]
			print spk_name
			num_data = map(float,line[1:])
			print(num_data)
            
	    		ivec = np.array(num_data)
            		spk_ivec[spk_name] = ivec
	return spk_ivec
