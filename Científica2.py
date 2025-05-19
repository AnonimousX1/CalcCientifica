"""
Nome do Arquivo: calcCientifica.py
Autor: Henrxque e Pedro Heinz
Email: anonimosx1@gmail.com
Data de Criação: 24/04/2024

Descrição: Calculadora ciêntifica utilizando métodos numéricos implementada sem uso de bibliotecas python
Licença: MIT
"""

#Calculadora GUI

import tkinter as tk

def fatorial(n: int):
    if (n < 0):
        return "Error!"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def pi():
    pi: float = 0
    denominador: float
    for i in range(0,1000000):
        denominador = ((4*i)+1)*((4*i)+3)
        pi = pi + (2/denominador)
    return round(pi*4,6)

#--------------- EXP (X)  -----------------

def pexp(x): # n = 700 boa, precisão ate x = 500.
    if(type(x == float)):
        return exp(x, n = 100)
    else:
        return exp(x, 700)

def exp(x, n):
    result: float = 0
    for i in range(n):
        result = result + (x**i)/fatorial(i)
    return round(result,8)

#--------------- Sin (X)  -----------------

def psin(x): # n= 50, boa precisão
  return sin(x, n= 50)

def sin(x, n):
    result: float = 0
    picostant: float = pi()
    for i in range(n):
        teta = x*(picostant/180)
        result += ((-1) ** i) * (teta ** (2 * i + 1)) / fatorial(2 * i + 1) #Estoura para loops grandes demais
    return round(result,8)

#--------------- Cos (X)  -----------------

def pcos(x): #n= 50, boa precisão
  return cos(x, n = 50)

def cos(x, n):
    result: float = 0
    picostant = pi()
    for i in range(n):
        teta = x*(picostant/180)
        result += ((-1)**i) * (teta**(2*i)) / fatorial(2*i) #Estoura para loops grandes demais
    return round(result,8)

#--------------- Tan (X)  -----------------

def tan(x): #MESMO n DAS OUTRAS
    result = sin(x, 80) / cos(x, 80)
    return round(result,4)

#--------------- Raiz (X)  -----------------

def praizquad(x):
  return raizquad(x, n = 100) # n= 100, boa precisão

def raizquad(x, n): # uso de uma identidade e ^ (( ln a ) / 2)
    result = exp((pln(x)/2), n)
    return round(result,8)

#--------------- ln (X)  -----------------

def pln(x): #n= 370 , boa precisão
  return ln(x, n = 370)

def ln(x, n):
    if (x == 0):
        return "Error!"
    scientific_notation = "{:.12e}".format(x)
    scientific_notation = scientific_notation.replace('+','')
    a, b = map(float, scientific_notation.split('e'))
    output = 0
    for i in range(1,n):
        output += (((a/10)-1)**i)*((-1)**(i+1))/i
        output -= (b+1)*((-0.9)**i)*((-1)**(i+1))/i
    return round(output,10)

#--------------- log10 (X)  -----------------

#MESMO n DAS ln

def log10(x):
    LN10: float = pln(10)  # Calcula ln(10) usando a série de logn
    if(x==0):
        return "Error!"

    result = pln(x) / LN10
    return round(result,8)


#--------------Interface gráfica -----------
root = tk.Tk()
root.title("Calculadora Científica")

entry = tk.Entry(root, width=35, borderwidth=10)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def insert_value(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# Botões para números e operações aritméticas
for i in range(1, 10):
    tk.Button(root, text=str(i), command=lambda i=i: insert_value(i), padx=20, pady=20).grid(row=(1 + (i-1)//3), column=(i-1)%3)
tk.Button(root, text="0", command=lambda: insert_value(0), padx=20, pady=20).grid(row=4, column=0)

operations = ['+', '-', '*', '/']
for index, operator in enumerate(operations):
    tk.Button(root, text=operator, command=lambda operator=operator: insert_value(operator), padx=20, pady=20).grid(row=index+1, column=3)

# Funções científicas e suas representações
functions = ['psin', 'pcos', 'tan', 'praizquad', 'pi', 'pexp', 'fatorial', 'pln', 'log10']
representacao = ['sin', 'cos', 'tan', '√', 'π', 'e^x', 'n!', 'ln', 'log']

for index, (func, rep) in enumerate(zip(functions, representacao)):
    button = tk.Button(root, text=rep, command=lambda f=func: insert_value(f + '('), padx=20, pady=20)
    button.grid(row=5 + index // 4, column=index % 4, sticky='nsew')


# Botões para parênteses
tk.Button(root, text="(", command=lambda: insert_value('('), padx=20, pady=20).grid(row=4, column=1, columnspan=1)
tk.Button(root, text=")", command=lambda: insert_value(')'), padx=20, pady=20).grid(row=4, column=2, columnspan=1)


# Botão para avaliar a expressão
tk.Button(root, text="=", command=calculate, padx=20, pady=20).grid(row=7, column=3, sticky='nsew')
tk.Button(root, text="Clear", command=clear, padx=20, pady=20).grid(row=7, column=1, columnspan=2, sticky='nsew')

root.mainloop()
