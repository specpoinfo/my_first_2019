from graph import *

#Инициализация объектов через функции
#Все обекты отрисовываются от их центра
def my_sun(center_x, center_y):
    brushColor("yellow")
    penColor('yellow')
    circle(center_x, center_y, 37)


def my_boat(center_x, center_y):
    pass

def my_cloud(center_x, center_y):
    penColor('#94BABE')
    brushColor("white")
    x = center_x - 15
    y = center_y + 6.5
    for i in range(2):
        for k in range(2):
            circle(x - k*10, y + k*10, 13)
        x += 20
        y += 2
    x = center_x + 10
    y = center_y + 18
    for i in range(3):
        circle(x, y, 13)
        x += 8
        if i == 1:
            y += 12
        else:
            y -= 12
    

def my_background(my_width, my_height):    #Отрисовка фона
    #облака
    penColor("#637ACB")
    brushColor("#A1F5FF")
    rectangle(0, 0, my_width, my_height*0.46)
    #море
    penColor('#4532C8')
    brushColor("#4423DF")
    rectangle(0, my_height * 0.46, my_width, my_height*0.695)
    #песок
    penColor('#A7A43C')
    brushColor("#EEF60C")
    rectangle(0, my_height * 0.695, my_width, my_height)
    #палка от зонта
    penColor('#E38219')
    brushColor("#E38219")   
    rectangle(95, my_height - 20, 100, my_height-139)
    #основание верхушки зонтака
    penColor('#D84A67')
    brushColor("#F45151")   
    rectangle(95, my_height - 139, 100, my_height-170)
    #левая часть зонта
    polygon([(25, my_height - 139),(95, my_height - 139),(95, my_height-170)])
    #правая часть зонта
    polygon([(170, my_height - 139),(100, my_height - 139),(100, my_height-170)])
    #штриховка левой и правой части зонта
    penColor('#C14040')
    for x in range(1, 4):
        line(95, my_height-170,25 + 70*x/4, my_height - 139)
    for x in range(1,4):
        line(100, my_height-170, 100 + 70*x/4 , my_height - 139)


windowSize(600,402)
canvasSize(600,402)
width , height = canvasSize()

#месторасположение солнца
my_sun_x = 530
my_sun_y = 55

#месторасположение облаков
my_cloud_x = 150
my_cloud_y = 50


my_background(width,height)
my_sun(my_sun_x, my_sun_y)
my_cloud(my_cloud_x, my_cloud_y)





run()