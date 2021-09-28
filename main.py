# 1- imports  - bibliotecas
import pytest

# 2- class - classes (conjuntos de funções/métodos)



# 3- definitons - definições = métodos e funções


def print_hi(name):
    print(f'Oi, {name}')


def somar (numero1, numero2):
    return numero1 + numero2

def subtrair(numero1, numero2):
    return numero1 - numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

#esse é um exemplo de demonstração
def dividir(numero1, numero2):
    if numero2 != 0:
        return numero1 / numero2
    else:
        return 'Não dividiras por zero'

def dividir_try_except(numero1,numero2):
    try:
        return numero1 / numero2
    except TypeError:
        # return 'Não dividirás por zero'
        if TypeError == ZeroDivisionError:
            return 'Não dividirás por zero'
        elif TypeError == ArithmeticError:
            return 'Erro no cálculo'
        elif TypeError == ValueError:
            return 'Erro no valor'
        else:
            return 'Erro desconhecido'
        pass




    # Testes Unitários / Teste de Unidades

    # teste da função de somar - metódo não retorna valor, função retorna valor


def test_somar_didatico():
        # 1- Configura / Prepara
        numero1 = 8 #input
        numero2 = 5 #input
        resultado_esperado = 13 #output


        # 2- Executa
        resultado_atual = somar(numero1, numero2)

        # 3- Check / Valida
        assert resultado_atual == resultado_esperado
@pytest.mark.parametrize('numero1,numero2,resultado',[
    #valores
    (5, 4, 9), # teste 1
    (3, 2, 5), # teste 2
    (10,6, 16), # teste 3
])
def test_somar(numero1,numero2, resultado):
    try:
        assert somar(numero1,numero2) == resultado
    except AssertionError:
        print(f'Entrou no Except: {AssertionError}')


def test_subtrair():
    assert subtrair(4,5) == -1

def test_multiplicar():
    assert multiplicar(3,8) == 24

def test_dividir():
    assert dividir(9,3) == 3

def test_dividir_zero():
    assert dividir(9,0) == 'Não dividiras por zero'

@pytest.mark.parametrize('numero1, numero2, resultado',[
    (8,2,4),
    (20,4,5),
    (10,0,'Não dividiras por zero')
])
def test_dividr_try_except(numero1,numero2,resultado):
    assert dividir_try_except(numero1,numero2)== resultado

if __name__ == '__main__':
    print_hi('Tatiane')


    resultado = somar(5, 4)
    print(f'O resultado da soma é: {resultado}')

    resultado = subtrair(5, 3)
    print(f'O resultado da subtraçao é: {resultado}')


    resultado = multiplicar(2, 4)
    print(f'O resultado da multiplicaçao é: {resultado}')

    resultado = dividir(9, 3)
    print(f'O resultado da divisao é: {resultado}')









