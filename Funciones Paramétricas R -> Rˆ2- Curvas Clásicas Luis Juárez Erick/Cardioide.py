from sympy import symbols, cos, sin, pi, plot_parametric #Se importan funciones para sympy
t = symbols('t') #Se define el parámetro t
a = 3 #Constante
# Cardioide
x_cardioid = (1 + cos(t)) * cos(t) #Se define la componente x de la cardioide
y_cardioid = (1 + cos(t)) * sin(t) #Se define la componente y de la cardioide
# Involuta de la Cardioide
x_cardioid_involute = 2 * a + 3 * a * cos(t) * (1 - cos(t)) #Se define la componente x de la involuta de la cardioide
y_cardioid_involute = 3 * a * sin(t) * (1 - cos(t)) #Se define la componente x de la involuta de la cardioide
# Grafica la cardioide y su involuta e imprime el titulo de la gráfica y su leyenda
p = plot_parametric((x_cardioid, y_cardioid, (t, 0, 2 * pi)), show=False, line_color='red', label='Cardioide') #Grafica la cardioide
p.extend(plot_parametric((x_cardioid_involute, y_cardioid_involute, (t, 0, 2 * pi)), show=False, line_color='yellow', line_style='--', label='Involuta')) #Añade la involuta a la gráfica
p.title = "Cardioide y su Involuta" #Imprime el titulo de la gráfica
p.legend = True #Muestra la leyenda de la grafica
p.show() #Muestra la grafica final