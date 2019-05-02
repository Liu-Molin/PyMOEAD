# !/usr/bin/env python
# --------------------------------------------------------------
# File:          utilis.py
# Project:       PyMoead
# Created:       Wednesday, 1st May 2019 10:08:10 pm
# @Author:       molin@live.cn
# Last Modified: Wednesday, 1st May 2019 10:08:14 pm
# Copyright  © Rockface 2018 - 2019
# --------------------------------------------------------------

import sys, os
import fileinput
import moead



def file_loader(dataPath):
	num_line = 0
	problem = moead.Constraint()
	AssetList = []
	for line in fileinput.input(dataPath):
		if num_line==0:
			line = line.split()
			problem.num_assets = int(line[0])
			problem.num_port = int(line[1])
		else:
			if num_line<=problem.num_assets :
				asset_cache = moead.Asset(line)
				AssetList.append(asset_cache)
			else:
				if num_line<=(2*problem.num_assets):
					tran = num_line-problem.num_assets-1
					line = line.split()
					AssetList[tran].mean_income = line[0]
					AssetList[tran].diviation_risk = line[1]
		num_line+=1
	fund = 0
	for i in range(len(AssetList)):
		AssetList[i].id = i
		fund+=AssetList[i].holding*AssetList[i].current_price
		problem.fund = fund
		AssetList[i].standarize()
		##print(AssetList[i])
	return problem, AssetList
	