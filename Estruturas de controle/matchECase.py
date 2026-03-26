valor = int(input("Valor do produto: ")); 
forma = input("Escolha a forma de pagamento (dinheiro, a vista em cartão, duas vezes no cartão ou quatro vezes no cartão). "); 

vistaDinheiro = valor * 0.10; 
vistaDinheiro2 = valor - vistaDinheiro; 

vistaCartao = valor * 0.5; 
vistaCartao2 = valor - vistaCartao; 

duasVezes = valor

quatroVezes = valor * 0.7; 
quatroVezes2 = valor + quatroVezes; 

match forma: 
    case "dinheiro": 
        print("Você escolheu pagar a vista em dinheiro ou cheque!")
        print("O valor final é: ", vistaDinheiro2); 
    case "a vista em cartão": 
        print("Você escolheu pagar a vista no cartão!"); 
        print("O valor final é: ", vistaCartao); 
    case "duas vezes no cartão":
        print("Você escolheu pagar em duas vezes no cartão!"); 
        print("O valor final é: ", duasVezes); 
    case "quatro vezes no cartão": 
        print("Você escolheu pagar em quatro vezes no cartão!"); 
        print("O valor final é: ", quatroVezes2);  
