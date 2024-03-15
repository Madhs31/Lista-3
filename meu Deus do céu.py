a=int(input('Digite o primeiro número:'))
b=int(input('DIgite o segundo número:'))

while a % b != 0:
    a, b = b, a%b
    
print (f'mdc = {b}')