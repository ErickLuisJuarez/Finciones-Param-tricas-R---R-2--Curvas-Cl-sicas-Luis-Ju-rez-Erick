from sympy import symbols, cos, sin, pi, plot_parametric #Se importan funciones para sympy
t = symbols('t') #Se define el parámetro t
r = 2 #Se define el radio del circulo
#Circulo
x_circulo = r * cos(t) #Se define la componente x del circulo
y_circulo = r * sin(t) #Se define la componente y del circulo
# Involuta del Circulo
x_circulo_involuta = r * (cos(t) + t * sin(t)) #Se define la componente x de la involuta del circulo
y_circulo_involuta = r * (sin(t) - t * cos(t)) #Se define la componente y de la involuta del circulo
# Grafica el círculo y su involuta y se imprime el titulo de la gráfica y la leyenda
p = plot_parametric((x_circulo, y_circulo, (t, 0, 2 * pi)), show=False, line_color='green', label='Circulo') #Grafica el circulo
p.extend(plot_parametric((x_circulo_involuta, y_circulo_involuta, (t, 0, 2 * pi)), show=False, line_color='purple', line_style='--', label='Involuta')) #Añade la involuta a la gráfica
p.title = "Circulo y su Involuta" #Imprime el titulo de la gráfica
p.legend = True #Muestra la leyenda de la grafica
p.show() #Muestra la grafica final