parcelas = int(input("Valor das parcelas:")); 
quantidade = int(input("Quantidade de parcelas: ")); 

valordasparcelasjuntas = parcelas * quantidade; 

vista = int(input("Valor á vista:")); 

desconto = ((valordasparcelasjuntas - vista) / valordasparcelasjuntas) * 100
prcentual = valordasparcelasjuntas - vista; 


print("Aqui está o percentual de desconto se o pagamento for á vista:", desconto); 
