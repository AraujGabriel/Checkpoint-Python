#30. Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha da condição de pagamento.
# Utilize os códigos da tabela a seguir para ler qual a condição de pagamento escolhida, efetuar o cálculo adequado e exibir o valor a ser pago no final.
# Código Condição de pagamento
# 1 *   À vista em dinheiro ou cheque, recebe 10% de desconto
# 2 *   À vista no cartão de crédito, recebe 15% de desconto
# 3 *	Em duas vezes, preço normal de etiqueta sem juros
# 4 *	Em quatro vezes, preço normal de etiqueta mais juros de 10%

a = float(input("Insira o valor da etiqueta do produto:   "))
print(f"O produto escolhido custa:",a)
b = int(input("Escolha uma condicao de pagamento:\n1 *   À vista em dinheiro ou cheque, recebe 10% de desconto\n 2 *   À vista no cartão de crédito, recebe 15% de desconto\n3 *	Em duas vezes, preço normal de etiqueta sem juros\n 4 *	Em quatro vezes, preço normal de etiqueta mais juros de 10%\nDigite o numero da condicao de pagamento"))

if b==1:
    p = a*0.9
    print("O valor a ser pago:",p)
elif b==2:
    p = a*0.85
    print("O valor a ser pago: ",p)
elif b==3:
    print("O valor a ser pago:",a)
elif b ==4:
    p=a*1.1
    print("O valor a ser pago:",p)
else: print("Opcao invalida")