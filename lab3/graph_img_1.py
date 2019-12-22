from graph import * #если что так лучше не делать


# evil_smile 
center_x = 250
center_y = 300

brushColor('yellow')
circle(center_x, center_y, 200)
brushColor("red")
circle(center_x - 100, center_y - 50 , 50)
circle(center_x + 100, center_y - 50, 40)
brushColor("black")
circle(center_x - 100, center_y - 50 , 14)
circle(center_x + 100, center_y - 50, 14)

rectangle(center_x - 100, center_y + 100, center_x + 100, center_y + 130)
polygon([(50,100), (70, 80), (245, 220), (225, 230)])
polygon([(450,100), (440, 80), (265, 220), (285, 230)])


run()
