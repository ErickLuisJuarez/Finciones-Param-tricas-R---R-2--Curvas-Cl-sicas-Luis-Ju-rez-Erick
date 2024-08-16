from sympy import symbols, cos, sin, pi, plot_parametric #Se importan funciones para sympy
t = symbols('t') #Se define el parametro t
#Nefroide
x_nefroide = (3 * cos(t) - cos(3 * t)) / 2 #Se define la componente x de la nefroide
y_nefroide = (3 * sin(t) - sin(3 * t)) / 2 #Se define la componente y de la nefroide
# Involuta de la Nefroide
x_nefroide_involuta = 4 * cos(t)**3 #Se define la componente x de la involuta de la nefroide
y_nefroide_involuta = 3 * sin(t) + sin(3 * t) #Se define la componente y de la involuta de la nefroide
# Grafica la nefroide y su involuta e imprime el titulo de la gráfica y su leyenda
p = plot_parametric((x_nefroide, y_nefroide, (t, 0, 2 * pi)), show=False, line_color='orange', label='Nefroide') #Grafica la nefroide
p.extend(plot_parametric((x_nefroide_involuta, y_nefroide_involuta, (t, 0, 2 * pi)), show=False, line_color='pink', line_style='--', label='Involuta')) #Añade la involuta a la gráfica
p.title = "Nefroide y su Involuta" #Imprime el titulo de la gráfica
p.legend = True #Muestra la leyenda de la grafica
p.show() #Muestra la grafica final