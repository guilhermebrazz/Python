"""Escreva um programa que leia três valores com ponto flutuante: A, B e C. Em seguida, calcule e mostre: 

a) a área do triângulo retângulo que tem A por base e C por altura. 

b) a área do círculo de raio C. (pi = 3.14159) 

c) a área do trapézio que tem A e B por bases e c por altura. 

d) a área do quadrado que tem lado B. 

e) a área do retângulo que tem lados A e B."""

entrada = input()
valores = entrada.split()
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])
print(f'TRIANGULO: {(a*c/2):.3f}')
print(f'CIRCULO: {(3.14159*c**2):.3f}')
print(f'TRAPEZIO: {((a+b)*c/2):.3f}')
print(f'QUADRADO: {(b**2):.3f}')
print(f'RETANGULO: {(a*b):.3f}')