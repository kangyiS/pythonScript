import tkinter as tk
from  tkinter  import ttk
from tkinter import *
import serial
#import serial.tools.list_ports
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import time
from math import *
from tkinter import messagebox as tkMessageBox
from tkinter import filedialog as tkFiledialog
import os
import datetime

receive_data = {'linear_acceleration':{'x':0,'y':0,'z':0}, 'angular_velocity':{'x':0,'y':0,'z':0}, 'magnetic_field':{'x':0,'y':0,'z':0}}
velocity = {'x':0, 'y':0, 'z':0}
position = {'x':0, 'y':0, 'z':0}
finish = 0#表示是否读完imu_data文件，0没有读到文件，1正在读文件，2读完文件
draw_info = ""
fn = ""
figure = ""
data_timeInterval = 0.1#0.1s 接收一次数据，小车的imu数据发送时间间隔是0.1s
acc_z_zero = 10.9#加速度计z轴零点，单位是m/s2
#f = open("F:\\2018浙大\\夏令营\\keil\\imu_data.txt")

plt.ion() #让画的图像具有交互功能-动态显示
fig = plt.figure() 
ax = fig.gca(projection='3d') 

#小车位置的初始坐标为(0,0,0)
px = [0]
py = [0]
pz = [0]
# set figure information
ax.set_title("Trace")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.xlim((-20,20))
plt.ylim((-8,8))
ax.set_zlim((-3,3))#xyz量程

def search_file():#函数的定义
    global fn
    fn = tkFiledialog.askopenfilename()
    print(fn)
    myList.insert(tk.END, fn)
def draw_trace():#函数定义---画图
    global fn #声明几个全局变量
    global finish
    global figure
    f = open(fn)
    while finish != 2:
        lineStr = f.readline()
        if lineStr == 'linear_acceleration: \n':
            receive_data['linear_acceleration']['x'] = float(f.readline().split()[1])#有空格就分割，可以得到数据，字符串转成浮点型
            receive_data['linear_acceleration']['y'] = float(f.readline().split()[1])#在字典中查的关键字，通过key找到value
            receive_data['linear_acceleration']['z'] = float(f.readline().split()[1])
            finish = 1
            #draw_info = "drawing..."
            #infoList.insert(tk.END, draw_info)
            #print(receive_data)
        elif lineStr == 'angular_velocity: \n':
            receive_data['angular_velocity']['x'] = float(f.readline().split()[1])
            receive_data['angular_velocity']['y'] = float(f.readline().split()[1])
            receive_data['angular_velocity']['z'] = float(f.readline().split()[1])
            finish = 1
            #draw_info = "drawing..."
            #infoList.insert(tk.END, draw_info)
            #print(receive_data)
        elif lineStr == 'magnetic_field: \n':
            receive_data['magnetic_field']['x'] = float(f.readline().split()[1])
            receive_data['magnetic_field']['y'] = float(f.readline().split()[1])
            receive_data['magnetic_field']['z'] = float(f.readline().split()[1])
            finish = 1
            #draw_info = "drawing..."
            #infoList.insert(tk.END, draw_info)
            #print(receive_data)
        elif lineStr == '---\n':
            velocity['x'] += receive_data['linear_acceleration']['x']*data_timeInterval
            velocity['y'] += receive_data['linear_acceleration']['y']*data_timeInterval
            velocity['z'] += (receive_data['linear_acceleration']['z']-acc_z_zero)*data_timeInterval
            position['x'] += velocity['x']*data_timeInterval
            position['y'] += velocity['y']*data_timeInterval
            position['z'] += velocity['z']*data_timeInterval
            px.append(position['x'])
            py.append(position['y'])
            pz.append(position['z'])
            figure = ax.plot(px, py, pz, color='r', marker='o')#红色
            plt.draw()
            plt.pause(data_timeInterval)
            finish = 1
            draw_info = str(datetime.datetime.now()) +"  drawing..."
            infoList.insert(tk.END, draw_info)
        elif lineStr == '':
            if finish == 1:
                draw_info = str(datetime.datetime.now()) + "  Finished!"
                infoList.insert(tk.END, draw_info)
            else:
                draw_info = str(datetime.datetime.now()) + "  Error!"
                infoList.insert(tk.END, draw_info)
            finish = 2
        else:
            pass
    f.close()
    #*****************建界面

window = tk.Tk()#建窗口 GOI的库
window.title('Dialog Box')
window.geometry('480x440')

#建立列表框，用来显示文件路径
myList=tk.Listbox(window) 
myList.place(x=40, y=20, width=400, height=20)

#建立search file按钮
button_search = tk.Button(window,text="search file",width=15,height=2,command=search_file)
button_search.place(x=40, y=50, width=150, height=30)

#建立draw按钮
button_draw = tk.Button(window,text="draw",width=15,height=2,command=draw_trace)
button_draw.place(x=290, y=50, width=150, height=30)

#建立列表框和滚动条，用来显示信息
scr1 = Scrollbar(window)
infoList=tk.Listbox(window, yscrollcommand=scr1.set) 
infoList.place(x=40, y=100, width=380, heigh=300)

scr1.config(command=infoList.yview)
scr1.place(x=420, y=100, width=20, height=300)

window.mainloop()

'''

receive_data = {'linear_acceleration':{'x':0,'y':0,'z':0}, 'angular_velocity':{'x':0,'y':0,'z':0}, 'magnetic_field':{'x':0,'y':0,'z':0}}
velocity = {'x':0, 'y':0, 'z':0}
position = {'x':0, 'y':0, 'z':0}
finish = 0

f = open("F:\\2018浙大\\夏令营\\keil\\imu_data.txt")

plt.ion() #让画的图像具有交互功能-动态显示
fig = plt.figure() #声明建图片
ax = fig.gca(projection='3d') #声明建3d图片

px = [0]#从a1 a2 a3取数据
py = [0]
pz = [0]
# set figure information
ax.set_title("3D_Curve")#设置图片的标题
ax.set_xlabel("x")#xyz轴的标签
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.xlim((-20,20))#设置三轴的范围
plt.ylim((-8,8))
ax.set_zlim((-3,3))

while not finish:
    lineStr = f.readline()
    if lineStr == 'linear_acceleration: \n':
        receive_data['linear_acceleration']['x'] = float(f.readline().split()[1])
        receive_data['linear_acceleration']['y'] = float(f.readline().split()[1])
        receive_data['linear_acceleration']['z'] = float(f.readline().split()[1])
        #print(receive_data)
    elif lineStr == 'angular_velocity: \n':
        receive_data['angular_velocity']['x'] = float(f.readline().split()[1])
        receive_data['angular_velocity']['y'] = float(f.readline().split()[1])
        receive_data['angular_velocity']['z'] = float(f.readline().split()[1])
        #print(receive_data)
    elif lineStr == 'magnetic_field: \n':
        receive_data['magnetic_field']['x'] = float(f.readline().split()[1])
        receive_data['magnetic_field']['y'] = float(f.readline().split()[1])
        receive_data['magnetic_field']['z'] = float(f.readline().split()[1])
        #print(receive_data)
    elif lineStr == '---\n':
        velocity['x'] += receive_data['linear_acceleration']['x']*0.1
        velocity['y'] += receive_data['linear_acceleration']['y']*0.1
        velocity['z'] += (receive_data['linear_acceleration']['z']-10.9)*0.1
        position['x'] += velocity['x']*0.1
        position['y'] += velocity['y']*0.1
        position['z'] += velocity['z']*0.1
        px.append(position['x'])#往b1中添加数
        py.append(position['y'])
        pz.append(position['z'])
        figure = ax.plot(px, py, pz, color='r', marker='o')#红色
        plt.draw()
        plt.pause(0.1)
    elif lineStr == '':
        finish = 1
    else:
        pass
f.close()
'''