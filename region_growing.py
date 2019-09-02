# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
Created on Thu Aug 22 09:08:04 2019
@author: gag 
"""

import math 

from PIL import Image
from pylab import *
import matplotlib.cm as cm
import scipy as sp
import random
import functions


def find_region(img, seed, delta):
	"""function that applies region growing method

    Parameters:
    -----------
    img: original image

    seed: pixel in which the region's growth will begin

	delta: from the initial pixel value a delta will be used

    Returns:
    --------
    img_rg: result image, binary image with the region found

    """

	x = int(seed[0][1])
	y = int(seed[0][0])

	val = img[x,y]
	print("Value of pixel" +str(val))
	lv = val - delta #(lowValue)
	print("Low:" + str(lv))
	hv = val + delta #(highValue)
	print("High:" + str(hv))

	seed_pixel = []
	seed_pixel.append(x)
	seed_pixel.append(y)


	img_rg = np.zeros((rows+1,columns+1))
	img_rg[seed_pixel[0]][seed_pixel[1]] = 255.0
	img_display = np.zeros((rows,columns))

	region_points = []
	region_points.append([x,y])

	print('\nloop runs till region growing is complete')
	#print 'starting points',i,j
	count = 0
	x = [-1, 0, 1, -1, 1, -1, 0, 1]
	y = [-1, -1, -1, 0, 0, 1, 1, 1]
	
	while( len(region_points)>0):
		
		if count == 0:
			point = region_points.pop(0)
			i = point[0]
			j = point[1]
		# print('\nloop runs till length become zero:')
		# print('len',len(region_points))
		# print('count',count)

		for k in range(8):	
			#print '\ncomparison val:',val, 'ht',ht,'lt',lt
			if img_rg[i+x[k]][j+y[k]] !=1:
				try:
					value = img[i+x[k]][j+y[k]]
					if  value > lv and value < hv:
						#print '\nbelongs to region',arr[i+x[k]][j+y[k]]
						# print(value)
						img_rg[i+x[k]][j+y[k]]=1
						p = [0,0]
						p[0] = i+x[k]
						p[1] = j+y[k]
						if p not in region_points: 
							if 0< p[0] < rows and 0< p[1] < columns:
								''' adding points to the region '''
								region_points.append([i+x[k],j+y[k]])
					else:
						#print 'not part of region'
						img_rg[i+x[k]][j+y[k]]=0
				except IndexError:     
                			continue

		#print '\npoints list',region_points
		point = region_points.pop(0)
		i = point[0]
		j = point[1]
		count = count +1
		#find_region(point[0], point[1])			 

	return img_rg




if __name__== "__main__":


	file = "/home/gag/MyProjects/Image-Segmentation-using-Region-Growing/mapaSantaFe.tif"
	### se lee la imagen
	src_ds, band, GeoT, Project = functions.openFileHDF(file, 1)
	###sub-window
	sub_win = band[1220:3740, 1190:3850]


	# rows,columns = np.shape(sub_win)
	# print('\nrows', rows, 'columns', columns)

	fig, ax = plt.subplots()
	im=ax.imshow(sub_win)

	seed = plt.ginput(1)

	print('you clicked:',seed)

	#closing figure
	plt.close()


	# th = threshold(sub_win, -23, 3)

	# fig, ax = plt.subplots()
	# im=ax.imshow(th)

	# plt.show()



	delta = 10
	img_out = find_region(sub_win, seed, delta)

	fig, ax = plt.subplots()
	### , cmap="Greys_r"

	im=ax.imshow(img_out)
	plt.show()


