salario = int(input("Digite o salário de João aqui: "))
aumento = float(input("Digite a porcentagem, sem o símbolo de porcentagem do aumento\nPor exemplo, um aumento de 5% será 5, um aumento de 100% será 100"))
periodototal = int(input("Digite os meses consecutivos em que João recebeu um aumento: "))

periodo = 1 # outra variável foi usada para fazer uma contagem progressiva do salário ao longo dos meses, dado pela condição do loop while abaixo:

print("") # pula uma linha, totalmente cosmético
print(salario)
while periodo != periodototal: # esta condição
    salario =  salario * (aumento / 100 + 1) # determina a variável como o valor anterior vezes a fórmula de 
    print(round(salario, 2)) # arrendondamento dos dígitos decimais
    periodo += 1

print("\nFeito por Rogerio D. Júnior \nrogerdjr@usp.br")