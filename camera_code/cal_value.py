import time
import math


def PT_control(x,y):
	f = 3.4	#最远的焦距3.4mm
	Rw = 1280  #水平分辨率1280像素
	Rh = 720   #垂直分辨率720像素
	tanP = 3.385/f  #水平角度
	tanT = 2.54/f   #垂直角度
	a = math.atan(2*abs(Rw/2-x)/Rw*tanP)*57.3  #水平需要调整的角度
	if (Rw/2-x) >= 0:
		P_dir = -1
	else:
		P_dir = 1
	
	b = math.atan(2*abs(Rh/2-y)/Rh*tanT)*57.3-22  #垂直需要调整的角度
	if b >= 0:
		T_dir = 1
	else:
		T_dir = -1
	#cam.absolute_position(24,24,(a*57.3/90*16),(b*57.3/25*16),P_dir,T_dir)
	print('a=%d b=%d \n',(a,b))
	print('absolute_position: %d %d %d %d\n',((a*16),(abs(b)*16),P_dir,T_dir))
	return (True)
	
def Zoom_control(pre_pixel):	
	target_pixel = 200*200
	zoom_value = math.sqrt(target_pixel/pre_pixel)
	
	if zoom_value >= 30:
		zoom_time = 12
	else:
		zoom_time = zoom_value *1.4
	#print('zoom_value :%d  zoom_time:%f',(zoom_value,zoom_time))
	print('zoom_time:%f',(zoom_time))
	return (True)
	
def PTZ_control(lu_x, lu_y, rd_x, rd_y):
	wide = rd_x - lu_x
	heigh = rd_y - lu_y
	center_x = lu_x + wide/2
	center_y = lu_y + heigh/2
	pre_pixel = wide*heigh
	
	PT_control(center_x,center_y)
	Zoom_control(pre_pixel)
	#print('center: %d %d\n pre_pixel: %d\n',(center_x,center_y,pre_pixel))
	return (True)
	
if __name__ == '__main__':
	PTZ_control(111,380,153,427)
	PTZ_control(516,347,563,407)
	PTZ_control(484,265,515,303)
	PTZ_control(202,110,225,137)
	