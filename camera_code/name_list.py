#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
from scipy.stats import binom


def person(s):
	#阈值,伯努利二项分布
	Threshold = binom.ppf(0.95,5,0.85)
	
	
	#统计每个字符串出现的次数，存在字典 dic中
	dic={}
	for i in range(len(s)):
		if  s[i] in dic:
			dic[s[i]]+=1
		else:
			dic[s[i]]=1
			
	#对字典中出现次数进行降序排序		
	items=dic.items()
	backitems=[[v[1],v[0]] for v in items]
	backitems.sort(reverse=True)
	
	#出现次数超过阈值的输出人名
	if backitems[0][0] >= Threshold:
		return backitems[0][1]
	else:
		return "others"
	
def position(name_pos)
	x_rang = 100
	y_rang = 100
	
	for i in range(len(name_pos))
		
		
		
if __name__ == '__main__':
	name_list = []  #输出人名列表
	
	#传给我的名字矩阵 50*n: name_list
	#name_matrix = [["FGN","HQH","ZQ"],["FGN","HQH","ZQ"],["FGN","HQH","ZL"],["FGN","HQH","ZQ"],["FGN","HQH","ZQ"]]
	name_pos =  [[(1141.5, 196.0, 'zq'), (203.5, 474.0, 'lf')], [(1138.0, 197.5, 'zq'), (205.5, 473.0, 'lf')], [(1135.5, 196.0, 'zq')], [(1127.0, 202.0, 'zq')], [(216.5, 466.5, 'lf')], [(1122.0, 202.5, 'zq')], [(1119.5, 202.5, 'zq'), (223.5, 460.0, 'lf')], [(226.5, 456.5, 'lf')], [(235.5, 451.5, 'lf')], [(241.0, 448.5, 'lf')], [(245.5, 445.5, 'lf'), (1119.0, 203.5, 'zq')], [(245.0, 443.5, 'lf'), (1119.0, 205.5, 'zq')], [(248.0, 441.5, 'lf'), (1120.5, 205.5, 'xyt')], [(249.5, 441.5, 'lf')], [(261.0, 438.5, 'lf')], [(262.0, 435.0, 'lf')], [(266.5, 434.0, 'lf')], [(270.0, 432.5, 'lf')], [(274.5, 430.5, 'lf')], [(278.5, 427.5, 'lf')], [(296.0, 418.5, 'xyt')], [(307.0, 413.0, 'lf')], [(321.0, 407.0, 'lf')], [(326.5, 406.0, 'lf')], [(333.5, 404.5, 'lf')], [(337.0, 403.5, 'lf')], [(339.0, 405.0, 'lf')], [(341.0, 406.5, 'lf')], [(339.0, 409.0, 'lf')], [(338.5, 411.0, 'lf')], [(334.5, 413.5, 'lf')], [(335.0, 415.5, 'lf')], [(333.5, 415.5, 'lf')], [(326.5, 417.0, 'lf')]]

	name_trans = list(map(list,zip(*name_matrix)))
	for i in range(len(name_trans)):
		name_list.append(person(name_trans[i]))
	print(name_list)
