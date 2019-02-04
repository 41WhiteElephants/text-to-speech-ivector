import matplotlib
import sklearn.manifold.TSNE
from kaldi_to_numpy import ark2dict 

def main():
	ivec_path = "/macierz/home/s174520/ivector-xvector/ivector/data/feat/ivectors_enroll_mfcc/ivector.1.ark"
	ivec_dict = ark2dict(ivec_path)
	print len(ivec_dict)
	# do_tsne()
	# plot()
	
		


if __name__ == "__main__":
	main()
