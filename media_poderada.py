


# dados sensores
sensor_A_data = [20.1, 20.3, 20.0, 20.2, 20.1, 20.3, 20.0, 20.2, 20.1, 20.3]
sensor_B_data = [20.5, 20.0, 21.0, 20.2, 20.8, 20.1, 20.6, 20.3, 20.9, 20.4]
sensor_C_data = [21.5, 19.8, 22.0, 20.0, 19.5]

all_data = sensor_A_data + sensor_B_data + sensor_C_data

# Peso das respostas de cada sensor
peso_A = [3] * len(sensor_A_data)
peso_B = [2] * len(sensor_B_data)
peso_C = [1] * len(sensor_C_data)

all_pesos = peso_A + peso_B + peso_C

print(all_data)
print(all_data)

soma_valores = 0
soma_peso = 0

for i in range(len(all_data)):
    valor = all_data[i]
    peso = all_pesos[i]

    soma_valores += (valor * peso)
    soma_peso += peso

    media_poderada = soma_valores / soma_peso


print(f">>> Exemplo 01: Dados dos Sensores <<<")
print(f"Soma dos valores ponderados: {soma_valores:.2f}")
print(f"Soma dos pesos: {soma_peso:.2f}")
print(f"Média Ponderada das Temperaturas:{media_poderada:.2f}")
    
