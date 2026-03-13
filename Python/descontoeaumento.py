produto = int(input("Preço do produto:")); 
desconto = int(input("Percentual de desconto:")); 

descontomenor = produto * desconto / 100
descontomaior = produto * desconto / 100 + produto

print("Preço do desconto:", descontomenor, "Preço com aumento:", descontomaior); 