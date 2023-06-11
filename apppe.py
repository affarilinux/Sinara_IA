entrada = [1,2,3,2.5]

peso1 = [0.2,0.8,-0.5,1]
peso2 = [0.5,-0.91,0.26,-0.5]
peso3 = [-0.26,-0.27,0.17,0.87]

bias1 = 2
bias2 = 3
bias3 = 0.5

saida = [
        #neuronio1
        entrada[0] * peso1[0] + entrada[1] * peso1[1] + 
        entrada[2] * peso1[2] + entrada[3] * peso1[3] + bias1,

        #neuronio2
        entrada[0] * peso2[0] + entrada[1] * peso2[1] + 
        entrada[2] * peso2[2] + entrada[3] * peso2[3] + bias2,

        #neuronio3
        entrada[0] * peso3[0] + entrada[1] * peso3[1] + 
        entrada[2] * peso3[2] + entrada[3] * peso3[3] + bias3

        
        ]

print(saida)

