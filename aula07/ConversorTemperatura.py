#Programa que converte de Celsius para Fahrenheit e Kelvin
#print("Celsius para Fahrenheit = ( C * 9/5) + 32 = F")
#print("Celsius para Kelvin = C + 273,15 = K ")

celsi = float(input("Digite o valor em Celsius: "))
conv1 = (celsi * 9/5) + 32
conv2 =  celsi + 273.15
celsiFahren = print("{}C para Fahrenheit é igual a: {}".format(celsi, conv1))
celsiKelvin = print("{}C para Kelvin é igual a: {}".format(celsi, conv2))



#print("Fahrenheit para Celsius = (F - 32) * 5/9 = C")
#print("Fahrenheit para Kelvin = (F - 32) * 5/9 + 273.15 = K ")
fahren = float(input("Digite o valor em Fahrenheit: "))
conv3 = (fahren - 32) * 5/9
conv4 = (fahren - 32) * 5/9 + 273.15
fahrenCelsi = print("{}F para celsius é igual a: {}".format(fahren, conv3))
fahrenKelvin = print("{}F para Kelvin é igual a: {}".format(fahren, conv4))

#print("Kelvin para Celsius = K - 273,15 = C ")
#print("Kelvin para Fahrenheit = (K - 273,15) * 9/5 + 32 = F")
kelvin = float(input("Digite o valor em kelvin: "))
conv5 = kelvin - 273.15
conv6 =  (kelvin - 273.15) * 9/5 + 32
kelvinCelsi = print("{}K para celsius é igual a: {}".format(kelvin, conv5))
kelvinFahren =("{}K para fahrenheit é igual a: {}".format(kelvin, conv6))



