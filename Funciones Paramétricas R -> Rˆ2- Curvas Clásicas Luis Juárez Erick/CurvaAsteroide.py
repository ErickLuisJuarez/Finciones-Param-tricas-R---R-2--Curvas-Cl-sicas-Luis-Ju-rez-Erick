from sympy import symbols, cos, sin, pi, plot_parametric #Se importan funciones para sympy
t = symbols('t') #Se define el parámetro t
#Curva Asteroide
x_asteroide = cos(t)**3 #Se define la componente x de la curva asteroide
y_asteroide = sin(t)**3 #Se define la componente y de la curva asteroide
# Involuta de la Curva Asteroide
x_asteroide_involuta = (3 * cos(t) - cos(3 * t)) / 8 #Se define la componente x de la involuta de la curva asteroide
y_asteroide_involuta = (3 * sin(t) + sin(3 * t)) / 8 #Se define la componente y de la involuta de la curva asteroide
# Grafica la curva asteroide y su involuta y se imprime el titulo de la gráfica y su leyenda
p = plot_parametric((x_asteroide, y_asteroide, (t, 0, 2 * pi)), show=False, line_color='blue', label='Curva Asteroide') #Grafica la curva asteroide
p.extend(plot_parametric((x_asteroide_involuta, y_asteroide_involuta, (t, 0, 2 * pi)), show=False, line_color='red', line_style='--', label='Involuta')) #Añade la involuta a la gráfica
p.title = "Curva Asteroide y su Involuta" #Imprime el titulo de la gráfica
p.legend = True #Muestra la leyenda de la grafica
p.show() #Muestra la grafica final