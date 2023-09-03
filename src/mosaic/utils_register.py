from skimage.registration import phase_cross_correlation
from scipy import ndimage
from scipy.fft import fft2
import numpy as np
import itertools

def register(im1, im2, sigma = 3, upsample_factor = 10):
	im1_LoG = ndimage.gaussian_laplace(im1, sigma)
	im2_LoG = ndimage.gaussian_laplace(im2, sigma)
	
	im1_fft = fft2(im1_LoG)
	im2_fft = fft2(im2_LoG)
	
	#Returns displacement that will best align im2 wrt im1.
	#1st entry in shift is the y offset with positive values meaning im2 should be shifted down.
	#2nd entry in shift is the x offset with positive values meaning im2 should be shifted right.
	shift, error, diffphase = phase_cross_correlation(im1_fft, im2_fft, \
					upsample_factor = upsample_factor, space = 'fourier')
	
	return([shift, error, diffphase])



