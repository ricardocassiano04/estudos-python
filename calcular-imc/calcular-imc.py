#!/bin/python3
'''

Autor: Ricardo Cassiano


Script para calcular o IMC (índice de massa coporal).


Basta informar sua altura e seu peso que será mostrado
seu índice, dirá se está acima do peso ou abaixo e o
quanto precisa perder ou ganhar para ficar no peso ideal.


'''

repetir = 's'

while (repetir == 's'):
    print('Ola. Este e o calculador de IMC!')
    print('A seguir, preencha seu peso e sua altura.')

    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    imc = peso / pow(altura, 2)
    peso_ideal = 23 * pow(altura,2)
    
    if imc < 17:        
        print("Você está muito abaixo do peso.")
    elif imc >= 17 and imc <= 18.49:        
        print("Você está abaixo do peso.")
    elif imc >= 18.5 and imc <= 24.99:        
        print("Você está no peso normal.")
    elif imc >= 25 and imc <= 29.99:        
        print("Você está acima do peso.")
    elif imc >= 30 and imc <= 34.99:        
        print("Você está no nível Obesidade I")
    elif imc >= 35 and imc <= 39.99:        
        print("Você está no nível Obesidade II (severa)")
    else:        
        print("Você está no nível Obesidade III (mórbida)")
        
    print("Seu IMC é: ", round(imc,2))
    print("Se deseja ter um IMC igual a 23, seu peso deve ser:  ", peso_ideal)
    if peso > peso_ideal:
        print("Você deve perder ", str(round(peso - peso_ideal,2)), " kg")
    elif peso < peso_ideal:
        print("Você deve ganhar ", str(round(peso_ideal - peso,2)), " kg")
    else:
        print("Você já está no peso ideal.\nParabéns!!")
    repetir = input("Deseja continuar? (s/n): ")
print("\nImc finalizado\nAté mais!")
