# !/usr/bin/env python
# --------------------------------------------------------------
# File:          moead.py
# Project:       PyMoead
# Created:       Wednesday, 1st May 2019 10:13:59 pm
# @Author:       molin@live.cn
# Last Modified: Wednesday, 1st May 2019 11:06:38 pm
# Copyright  © Rockface 2018 - 2019
# --------------------------------------------------------------

import sys

class asset():
	def __init__(self, id, current_price, holding, cost_buy, cost_sell, vcost_buy, vcost_sell, min_buy, min_sell, max_buy, max_sell, mean_income, diviation_risk):
		self.id = id
		self.current_price = current_price
		self.holding = holding
		self.cost_sell = cost_sell
		self.cost_buy = cost_buy
		self.vcost_sell = vcost_sell
		self.vcost_buy = vcost_buy
		self.min_sell = min_sell
		self.min_buy = min_buy
		self.max_sell = max_sell
		self.max_buy = max_buy
		self.mean_income = mean_income
		self.diviation_risk = diviation_risk

	
