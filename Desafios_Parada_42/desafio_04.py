# Faça um programa que converte Grau Celsius em Grau Fahrenheit.

print(' = '*11 + 'CONVERSOR DE TEMPERATURA' + ' = '*11)
temp_C = float(input('Insira a temperatura em °C: '))

temp_K = (temp_C + 273)
temp_F = (temp_C *1.8)+32
print(' ')
print(' ')
print(f'A temperatura {temp_C}°C é equivalente a {temp_K}K na escola Kelvin ou {temp_F}°F na escala Fahrenheit')
print(' = '*30)
