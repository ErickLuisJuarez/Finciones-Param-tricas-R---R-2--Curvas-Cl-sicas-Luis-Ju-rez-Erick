from sympy import symbols, cosh, sinh, plot_parametric #Se importan funciones para sympy
t = symbols('t')#Se dedine el parámetro t
# Catenaria
x_catenaria = t #Se define la componente x de la catenaria
y_catenaria = cosh(t) #Se define la componente y de la catenaria
# Involuta de la Catenaria
x_catenaria_involuta = t - sinh(t) / cosh(t) #Se define la componente x de la involuta de la catenaria
y_catenaria_involuta = 1 / cosh(t) #Se define la componente y de la involuta de la catenaria
# Grafica la catenaria y su involuta e imprime el titulo d ela grafica y su leyenda
p = plot_parametric((x_catenaria, y_catenaria, (t, -2, 2)), show=False, line_color='red', label='Catenaria') #Grafica la catenaria
p.extend(plot_parametric((x_catenaria_involuta, y_catenaria_involuta, (t, -2, 2)), show=False, line_color='cyan', line_style='--', label='Involuta')) #Añade la involuta a la gráfica
p.title = "Catenaria y su Involuta" #Imprime el titulo de la gráfica
p.legend = True #Muestra la leyenda de la grafica
p.show() #Muestra la grafica final