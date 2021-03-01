import turtle

t=turtle.Pen()

colors = ['red', 'black', 'green']
print(colors)
print(colors[0])

t.speed(0.5)
for x in range(0, 100):
	t.pencolor(colors[x%3])
	t.left(68)
	i = 100
	t.forward(x)

t.forward(100)


turtle.done()
