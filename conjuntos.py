#Henrique Anderle Schulz
arquivo_entrada = open("operações1.txt", "r")
linhas = arquivo_entrada.readlines()

def separar_linhas(linha):
    x = linha.split('\n')
    y = x[0].split(',')
    return y

def ler(x):
    operacao = (separar_linhas(linhas[x]))
    conjunto1 = (separar_linhas(linhas[x+1]))
    conjunto2 = (separar_linhas(linhas[x+2]))
    resultado = []
    if "U" in operacao:
        for c in range (len(conjunto1)):
            resultado.append(conjunto1[c])
        for i in range (len(conjunto2)):
            if conjunto2[i] not in conjunto1:
                resultado.append(conjunto2[i])
        print('União: conjunto 1 {',  ','.join(conjunto1), '}, conjunto2 {', ','.join(conjunto2), '}.Resultado: {', ','.join(resultado),'}')
    if "I" in operacao:
        for i in range (len(conjunto1)):
            if conjunto1[i] in conjunto2:
                resultado.append(conjunto1[i])
        print('Interseção: conjunto 1 {',  ','.join(conjunto1), '}, conjunto2 {', ','.join(conjunto2), '}.Resultado: {', ','.join(resultado),'}')
    if "D" in operacao:
        for i in range (len(conjunto1)):
            if conjunto1[i] not in conjunto2:
                resultado.append(conjunto1[i])
        print('Diferença: conjunto 1 {',  ','.join(conjunto1), '}, conjunto2 {', ','.join(conjunto2), '}.Resultado: {', ','.join(resultado),'}')
    if "C" in  operacao:
        res_form = []
        for i in range (len(conjunto1)):
            for c in range (len(conjunto2)):
                resultado.append([conjunto1[i], conjunto2[c]])
        for l in range (len(resultado)):
            res_form.append('(')
            for c in range (len(resultado[0])):
                res_form.append(resultado[l][c])
                if c == 0 :
                    res_form.append(',')
                if c == (len(resultado[0]) - 1 ):
                    res_form.append(')')
        print('Cartesiano: conjunto 1 {',  ','.join(conjunto1), '}, conjunto2 {', ','.join(conjunto2), '}.Resultado: {', ''.join(res_form),'}')

num_operacoes = separar_linhas(linhas[0])
num_operacoes = int(num_operacoes[0])

x = 1
for i in range(1, num_operacoes + 1):
    (ler(x))
    x = x + 3
