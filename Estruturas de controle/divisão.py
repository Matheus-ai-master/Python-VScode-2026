print("Use números inteiros para melhor resposta."); 
primeiro = int(input("Primeiro número (dividendo): ")); 
segundo = int(input("Segundo número (divisor): ")); 

if primeiro == 0 or segundo == 0: 
    print("Não é possível dividir nada por zero, o resultado sempre será 0."); 

conta = primeiro / segundo; 

if conta >= 0.1:
   print("Resultado: ", conta); 