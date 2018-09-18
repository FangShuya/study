#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
from scipy.stats import binom


def person(s):
	j = 0
	#阈值,伯努利二项分布
	for i in range(len(s)):
		if s[i] != 0:
			j += 1
		
	print('num person: %d',j)
	Threshold = binom.ppf(0.95,j,0.85)
	print("threshold %f"%Threshold)
	
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
	print('large person:')
	print(backitems[0])
	#出现次数超过阈值的输出人名
	
	
	if backitems[0][1] == 0:
		if backitems[0][0] == len(s) :
			return 0
		else:
			large_person = backitems[1]
		
	else:
		large_person = backitems[0]
		
	if large_person[0] >= Threshold:
			return large_person[1]
	else:
		return "others"
		
		
	
def position(name_pos):
	x_rang = 70 #位置偏移阈值
	y_rang = 70 #位置偏移阈值
	name = []
	
	pos_temp = []
	print("frame %d"%len(name_pos))
	#大循环，i：帧数
	for i in range(len(name_pos)):
		name_temp = [0, 0, 0, 0, 0, 0, 0, 0]
		#第一帧，直接保存人名（name_temp）和位置（pos_temp）
		#print("frame %d"%i)
		if i == 0:  
			for j in range(len(name_pos[0])):  #j：第一帧中人脸的个数
				name_temp.insert(j,name_pos[0][j][2])
				pos_temp.append((name_pos[0][j][0],name_pos[0][j][1])) 
				#print(name_temp)
				#print(pos_temp)
			
			
		
		#其他帧，每个人脸的位置都与pos_temp中人脸的位置进行比较。位置偏移不超过阈值的认为是同一个人脸		
		else:
			for j in range(len(name_pos[i])): #j：第i帧中人脸的个数
				for k in range(len(pos_temp)): #与pos_temp中人脸的位置进行比较					
					if (abs(name_pos[i][j][0]- pos_temp[k][0]) <= x_rang) & (abs(name_pos[i][j][1]- pos_temp[k][1]) <= y_rang):
						#name_temp.insert(k,(name_pos[i][j][2]))
						#pos_temp.insert(pos_temp.index((pos_temp[k][0],pos_temp[k][1])),(name_pos[i][j][0],name_pos[i][j][1]))
						name_temp.pop(pos_temp.index((pos_temp[k][0],pos_temp[k][1])))
						name_temp.insert(pos_temp.index((pos_temp[k][0],pos_temp[k][1])),(name_pos[i][j][2]))
						#print("	face%d -- position%d"%(j,k))
			
						break
						
					else:
						if k == len(pos_temp)-1:
							#print("	add new person")
							
							pos_temp.append((name_pos[i][j][0],name_pos[i][j][1]))
							name_temp.insert(pos_temp.index((name_pos[i][j][0],name_pos[i][j][1])),(name_pos[i][j][2]))
							
						else:
							#print("	face%d -X- position%d"%(j,k))
							continue
			print(name_temp)
			#print(pos_temp)
				
		name.append(name_temp)

	return name

def person_list(name_pos):
	name_list = []  #输出人名列表
	name = position(name_pos)
	print("name_positon ok!")

	name_trans = list(map(list,zip(*name)))
	for i in range(len(name_trans)):
		name_list.append(person(name_trans[i]))
	#print(name_list)
	print("person list ok!")
	return name_list

if __name__ == '__main__':
	name_list = []  #输出人名列表
	
	#传给我的名字矩阵 50*n: name_list
	#name_matrix = [["FGN","HQH","ZQ"],["FGN","HQH","ZQ"],["FGN","HQH","ZL"],["FGN","HQH","ZQ"],["FGN","HQH","ZQ"]]
	#name_pos =  [[(203.5, 474.0, 'lf')], [(1138.0, 197.5, 'zq'), (205.5, 473.0, 'lf')], [(1135.5, 196.0, 'zq'), (456.5, 675.0, 'HQH')], [(1127.0, 202.0, 'zq')], [(216.5, 466.5, 'lf')], [(1122.0, 202.5, 'zq')], [(1119.5, 202.5, 'zq'), (223.5, 460.0, 'lf')], [(226.5, 456.5, 'lf')], [(235.5, 451.5, 'lf')], [(241.0, 448.5, 'lf')], [(245.5, 445.5, 'lf'), (1119.0, 203.5, 'zq')], [(245.0, 443.5, 'lf'), (1119.0, 205.5, 'zq')], [(248.0, 441.5, 'lf'), (1120.5, 205.5, 'xyt')], [(249.5, 441.5, 'lf')], [(261.0, 438.5, 'lf')], [(262.0, 435.0, 'lf')], [(266.5, 434.0, 'lf')], [(270.0, 432.5, 'lf')], [(274.5, 430.5, 'lf')], [(278.5, 427.5, 'lf')], [(296.0, 418.5, 'xyt')], [(307.0, 413.0, 'lf')], [(321.0, 407.0, 'lf')], [(326.5, 406.0, 'lf')], [(333.5, 404.5, 'lf')], [(337.0, 403.5, 'lf')], [(339.0, 405.0, 'lf')], [(341.0, 406.5, 'lf')], [(339.0, 409.0, 'lf')], [(338.5, 411.0, 'lf')], [(334.5, 413.5, 'lf')], [(335.0, 415.5, 'lf')], [(333.5, 415.5, 'lf')], [(326.5, 417.0, 'lf')]]
	name_pos = [[(1141.5, 196.0, 'zq'), (203.5, 474.0, 'lf')], [(1138.0, 197.5, 'zq'), (205.5, 473.0, 'lf')], [(1135.5, 196.0, 'zq')], [(1127.0, 202.0, 'zq')], [], [(216.5, 466.5, 'lf')], [(1122.0, 202.5, 'zq')], [(1119.5, 202.5, 'zq'), (223.5, 460.0, 'lf')], [(226.5, 456.5, 'lf')], [(235.5, 451.5, 'lf')], [(241.0, 448.5, 'lf')], [(245.5, 445.5, 'lf'), (1119.0, 203.5, 'zq')], [(245.0, 443.5, 'lf'), (1119.0, 205.5, 'zq')], [(248.0, 441.5, 'lf'), (1120.5, 205.5, 'xyt')], [(249.5, 441.5, 'lf')], [], [(261.0, 438.5, 'lf')], [(262.0, 435.0, 'lf')], [(266.5, 434.0, 'lf')], [(270.0, 432.5, 'lf')], [(274.5, 430.5, 'lf')], [(278.5, 427.5, 'lf')], [], [(296.0, 418.5, 'xyt')], [(307.0, 413.0, 'lf')], [(321.0, 407.0, 'lf')], [(326.5, 406.0, 'lf')], [(333.5, 404.5, 'lf')], [(337.0, 403.5, 'lf')], [(339.0, 405.0, 'lf')], [(341.0, 406.5, 'lf')], [(339.0, 409.0, 'lf')], [(338.5, 411.0, 'lf')], [(334.5, 413.5, 'lf')], [(335.0, 415.5, 'lf')], [(333.5, 415.5, 'lf')], [(326.5, 417.0, 'lf')], [], [], [], [], [], [], [(233.0, 496.5, 'zy')], [], [], [], [], [(271.0, 423.5, 'lf')], [(262.0, 425.5, 'lf')], [], [], [(220.0, 434.0, 'lf')], [(210.0, 435.0, 'lf')], [], [(707.0, 484.0, 'fsy')], [(718.5, 479.5, 'rjh')], [(737.0, 474.5, 'fsy')], [(225.5, 413.5, 'others'), (752.0, 470.0, 'fsy')], [(235.5, 409.0, 'others'), (771.0, 463.0, 'zl')]]

	#name_pos =  [[(203.5, 474.0, 'lf')], [(1138.0, 197.5, 'zq'), (205.5, 473.0, 'lf')], [(1135.5, 196.0, 'zq'), (205.5, 473.0, 'lf'), (456.5, 675.0, 'HQH')], [(1127.0, 202.0, 'zq')]]
	print(person_list(name_pos))
	
