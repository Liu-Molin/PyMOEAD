# !/usr/bin/env python
# --------------------------------------------------------------
# File:          moead.py
# Project:       PyMoead
# Created:       Wednesday, 1st May 2019 10:13:59 pm
# @Author:       molin@live.cn
# Last Modified: Wednesday, 1st May 2019 11:06:38 pm
# Copyright  © Rockface 2018 - 2019
# --------------------------------------------------------------

import sys, os
import numpy as np
from decimal import *
import utilis


DATA_DIR='/Users/meow/Desktop/DP/PyMoead/DataSet'
DATA_PATH = os.path.join(DATA_DIR, 'portreb1.txt')

class Constraint():
	def __init__(self):
		pass
class Asset():
	
	def __init__(self, line):
		line = line.split()
		self.id = 0
		self.current_price = 0
		self.holding = 0
		self.cost_sell = 0
		self.cost_buy = 0
		self.vcost_sell = 0.0
		self.vcost_buy = 0.0
		self.min_sell = 0
		self.min_buy = 0
		self.max_sell = 0
		self.max_buy = 0
		self.mean_income = 0.0
		self.diviation_risk = 0.0
		self.__set_data(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9])

	def __str__(self):
		info = '\nID:\t' + str(self.id) + '\nCurrent price:\t' + str(self.current_price) + '\nHolding:\t' + str(self.holding) + '\nMean income:\t' + str(self.mean_income) +'\nDiviation risk:\t' + str(self.diviation_risk)
		return info
	def __set_data(self, current_price, holding, cost_buy, cost_sell, vcost_buy, vcost_sell, min_buy, min_sell, max_buy, max_sell):
		self.current_price = int(current_price)
		self.holding = int(holding)
		self.cost_sell = cost_sell
		self.cost_buy = cost_buy
		self.vcost_sell = vcost_sell
		self.vcost_buy = vcost_buy
		self.min_sell = int(min_sell)
		self.min_buy = int(min_buy)
		self.max_sell = max_sell
		self.max_buy = max_buy
	
	def standarize(self):
		self.holding += int(self.max_buy)

class Lamb():
	
	
	def __init__(self, lambid):
		self.lambid = lambid
		self.lamb = []
		self.neighbor = []
		pass
	def __str__(self):
		return str(self.lambid) + '\t' + str(self.lamb)

class PyMOEAD():

	def __init__(self, dataPath):
		self.num_solution = 100
		self.num_epoch = 100
		self.num_neighbor = 5

		self.dataPath = dataPath
		pass

	def __initLamb(self, num_lamb, num_neighbor):
		lambList = []
		for i in range(num_lamb):
			tempLamb = Lamb(i)
			
			weight1 = float(i)/float(num_lamb)
			weight2 = 1-weight1
			tempLamb.lamb.append(weight1)
			tempLamb.lamb.append(weight2)
			lambList.append(tempLamb)
		return lambList
	def __param(self, num_solution, num_epoch, num_neighbor):
		self.num_solution = num_solution
		self.num_epoch = num_epoch
		self.num_neighbor = num_neighbor

	def __initPopulation(self, num_solution):
		pass
	def go(self, num_solution = 100,  num_epoch = 100, num_neighbor = 5):
		self.__param(num_solution, num_epoch, num_neighbor)
		self.problem, self.AssetList = utilis.file_loader(self.dataPath)
		self.__initLamb(self.num_solution, self.num_neighbor)

if __name__ == "__main__":
	mop = PyMOEAD(DATA_PATH)
	mop.go()
