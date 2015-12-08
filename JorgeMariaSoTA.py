"""
entrada
• Quantidade	de	processos	para	simular
• Tamanho	do	Burst	do processo	(manual	ou	simulado)
• Tempo	de	chegada,	quando	necessário
• Prioridade,	quando	necessário
• Quantum	de	tempo,	quando	necessário

resultado
• Lista	dos	processos	com	os	seus	burst,	prioridades	e	tempo	de	chegada
• Exibir	o	Waiting	Time	e	Turnaround	Time	de	cada	processo	no	algoritmo
• Exibir	o	Waiting	Time	médio
• Exibir	o	Turnaround	Time	médio

"""



print("""Entre com 1 para FCFS
\nEntre com 2 para SJF
\nEntre com 3 para SRTF
\nEntre com 4 para Round	Robin
\nEntre com 5 para Multinível""")

entre = int(input("\nDigite o valor da entrada: "))
nDeProcessos = 0
dicProcesso ={}


print(entre)

if entre == 1:
	print("Você selecionou FCFS:")
	nDeProcessos = int(input("Ente com o numero de processos:"))
	for processo in range(nDeProcessos):
		burst = int(input("entre com a burst do processo %d :" %(processo+1)))
		tDeChegada = int(input("entre com o tempo de chegada do processo %d: " %(processo+1)))
		dicProcesso[processo+1] = [burst, tDeChegada]
	listProcessos = []
	ordem = []
	for i in dicProcesso.keys():
		listProcessos.append(i)

	while len(listProcessos):
		primeiroAChegar = listProcessos[0]
		for i in listProcessos:
			if dicProcesso[primeiroAChegar][1] > dicProcesso[i][1]:
				primeiroAChegar = i
		ordem.append(primeiroAChegar)
		listProcessos.remove(primeiroAChegar)

	for i, processo in enumerate(ordem):
		if(i == 0):
			temp = dicProcesso[processo]
			temp.append(dicProcesso[processo][1])
			temp.append(dicProcesso[processo][0] + dicProcesso[processo][1])
			temp.append(dicProcesso[processo][1])
			temp.append(dicProcesso[processo][3] - dicProcesso[processo][1])
			dicProcesso[processo] = temp
		else:
			temp = dicProcesso[processo]
			t = i-1
			temp.append(dicProcesso[ordem[t]][3])
			temp.append(dicProcesso[processo][0] + dicProcesso[ordem[t]][3])
			temp.append(dicProcesso[processo][2] - dicProcesso[processo][1])
			temp.append(dicProcesso[processo][3] - dicProcesso[processo][1])
			dicProcesso[processo] = temp

	tempoDeEspera = 0
	turnAround = 0
	for i in dicProcesso.keys():
		tempoDeEspera = tempoDeEspera + dicProcesso[i][4]
		turnAround = turnAround + dicProcesso[i][5]
	print("\n\n\n")
	for i in dicProcesso.keys():
		print("\nProcesso %d: Burst =  %d -- Tempo de chegada = %d --Tempo de espera = %d -- Turnaround = %d" %(i, dicProcesso[i][0], dicProcesso[i][1], dicProcesso[i][4], dicProcesso[i][5]))
	print("\n\nTempo medio de espera = %f -- Tempo medio de turnaround = %f" %(tempoDeEspera/len(dicProcesso), turnAround/len(dicProcesso)))


elif entre == 2:
	print("Você selecionou SJF:")
	nDeProcessos = int(input("Ente com o numero de processos"))
	for processo in range(nDeProcessos):
		burst = int(input("entre com a burst do processo %d :" %(processo+1)))
		tDeChegada = int(input("entre com o tempo de chegada do processo %d: " %(processo+1)))
		dicProcesso[processo+1] = [burst, tDeChegada]
	listProcessos = []
	ordem = []
	for i in dicProcesso.keys():
		listProcessos.append(i)

	while len(listProcessos):
		primeiroAChegar = listProcessos[0]
		for i in listProcessos:
			if dicProcesso[primeiroAChegar][1] > dicProcesso[i][1]:
				primeiroAChegar = i
		ordem.append(primeiroAChegar)
		listProcessos.remove(primeiroAChegar)

	primeiroAEntrar = ordem[0]
	for i in ordem:
		if dicProcesso[primeiroAEntrar][0] > dicProcesso[i][0]:
			if dicProcesso[primeiroAEntrar][1] == dicProcesso[i][1]:
				primeiroAEntrar = i
	ordem.remove(primeiroAEntrar)
	primeiroAEntrarL = [primeiroAEntrar]

	while len(ordem):
		menorJob = ordem[0]
		for i in ordem:
			if dicProcesso[menorJob][0] > dicProcesso[i][0]:
				menorJob = i
		listProcessos.append(menorJob)
		ordem.remove(menorJob)

	ordem = primeiroAEntrarL + listProcessos

	for i, processo in enumerate(ordem):
		if(i == 0):
			temp = dicProcesso[processo]
			temp.append(dicProcesso[processo][1])
			temp.append(dicProcesso[processo][0] + dicProcesso[processo][1])
			temp.append(dicProcesso[processo][1])
			temp.append(dicProcesso[processo][3] - dicProcesso[processo][1])
			dicProcesso[processo] = temp
		else:
			temp = dicProcesso[processo]
			t = i-1
			temp.append(dicProcesso[ordem[t]][3])
			temp.append(dicProcesso[processo][0] + dicProcesso[ordem[t]][3])
			temp.append(dicProcesso[processo][2] - dicProcesso[processo][1])
			temp.append(dicProcesso[processo][3] - dicProcesso[processo][1])
			dicProcesso[processo] = temp
	tempoDeEspera = 0
	turnAround = 0
	for i in dicProcesso.keys():
		tempoDeEspera = tempoDeEspera + dicProcesso[i][4]
		turnAround = turnAround + dicProcesso[i][5]
	print("\n\n\n")
	for i in dicProcesso.keys():
		print("\nProcesso %d: Burst =  %d -- Tempo de chegada = %d --Tempo de espera = %d -- Turnaround = %d" %(i, dicProcesso[i][0], dicProcesso[i][1], dicProcesso[i][4], dicProcesso[i][5]))
	print("\n\nTempo medio de espera = %f -- Tempo medio de turnaround = %f" %(tempoDeEspera/len(dicProcesso), turnAround/len(dicProcesso)))


elif entre == 3:
	print("Você selecionou SRTF:")
	nDeProcessos = int(input("Ente com o numero de processos"))
	tempoParaFinalizar = 0
	for processo in range(nDeProcessos):
		burst = int(input("entre com a burst do processo %d :" %(processo+1)))
		tempoParaFinalizar = tempoParaFinalizar + burst
		tDeChegada = int(input("entre com o tempo de chegada do processo %d: " %(processo+1)))
		dicProcesso[processo+1] = [burst, tDeChegada]
	listProcessos = []
	ordem = []
	for i in dicProcesso.keys():
		listProcessos.append(i)

	while len(listProcessos):
		primeiroAChegar = listProcessos[0]
		for i in listProcessos:
			if dicProcesso[primeiroAChegar][1] > dicProcesso[i][1]:
				primeiroAChegar = i
		ordem.append(primeiroAChegar)
		listProcessos.remove(primeiroAChegar)

	primeiroAEntrar = ordem[0]
	for i in ordem:
		if dicProcesso[primeiroAEntrar][0] > dicProcesso[i][0]:
			if dicProcesso[primeiroAEntrar][1] == dicProcesso[i][1]:
				primeiroAEntrar = i
	ordem.remove(primeiroAEntrar)
	primeiroAEntrarL = [primeiroAEntrar]

	while len(ordem):
		menorJob = ordem[0]
		for i in ordem:
			if dicProcesso[menorJob][0] > dicProcesso[i][0]:
				menorJob = i
		listProcessos.append(menorJob)
		ordem.remove(menorJob)

	ordem = primeiroAEntrarL + listProcessos
	dicTempoRestante = {}
	dicTempoQueFalta = {}
	for i in dicProcesso.keys():
		dicTempoQueFalta[i] = dicProcesso[i][0]
	
	processoEmExe = ordem[0]
	burstEmExe = dicProcesso[ordem[0]][0]
	listProcessos = []
	for exe in range(tempoParaFinalizar):
		for processo in ordem:
			if exe >= dicProcesso[processo][1]:
				if burstEmExe > dicProcesso[processo][0]:
					processoEmExe = processo
					burstEmExe = dicProcesso[processo][0]
		listProcessos.append(processoEmExe)
		burstEmExe = burstEmExe-1
		dicTempoQueFalta[processoEmExe] = burstEmExe
		if burstEmExe == 0:
			ordem.remove(processoEmExe)
			if len(ordem) > 0:
				processoEmExe = ordem[0]
			burstEmExe = dicTempoQueFalta[processoEmExe]

	for i, processo in enumerate(listProcessos):
		if i == 0:
			dicTempoRestante[processo] = [i]
			if listProcessos[i+1] != processo:
				temp = dicTempoRestante[processo]
				temp.append(i+1)
				dicTempoRestante[processo] = temp 
		elif i == len(listProcessos)-1:
			temp = dicTempoRestante[processo]
			temp.append(i)
			dicTempoRestante[processo] = temp 
		elif listProcessos[i-1] != processo or processo != listProcessos[i+1]:
			if processo in dicTempoRestante:
				temp = dicTempoRestante[processo]
				temp.append(i)
				dicTempoRestante[processo] = temp 
			else:
				dicTempoRestante[processo] = [i]	

	for i in dicProcesso.keys():
		finalDoprocesso = dicTempoRestante[i]
		fdp = finalDoprocesso[len(finalDoprocesso)-1]
		tempoDeEspera =  fdp - dicProcesso[i][1] - dicProcesso[i][0] + 1
		turnAround = fdp + 1 - dicProcesso[i][1]
		temp = dicProcesso[i]
		temp.append(tempoDeEspera)
		temp.append(turnAround)
		dicProcesso[i] = temp 

	tempoDeEspera = 0
	turnAround = 0
	for i in dicProcesso.keys():
		tempoDeEspera = tempoDeEspera + dicProcesso[i][2]
		turnAround = turnAround + dicProcesso[i][3]
	for i in dicProcesso.keys():
		print("\nProcesso %d: Burst =  %d -- Tempo de chegada = %d --Tempo de espera = %d -- Turnaround = %d" %(i, dicProcesso[i][0], dicProcesso[i][1], dicProcesso[i][2], dicProcesso[i][3]))
	print("\n\nTempo medio de espera = %f -- Tempo medio de turnaround = %f" %(tempoDeEspera/len(dicProcesso), turnAround/len(dicProcesso)))


elif entre == 4:
	print("Você selecionou Round Robin:")
	quantum = int(input("\nEntre com o quantum:"))
	nDeProcessos = int(input("Ente com o numero de processos"))
	tempoParaFinalizar = 0
	for processo in range(nDeProcessos):
		burst = int(input("entre com a burst do processo %d :" %(processo+1)))
		tempoParaFinalizar = tempoParaFinalizar + burst
		tDeChegada = int(input("entre com o tempo de chegada do processo %d: " %(processo+1)))
		dicProcesso[processo+1] = [burst, tDeChegada]

	listProcessos = []
	ordem = []
	for i in dicProcesso.keys():
		listProcessos.append(i)

	while len(listProcessos):
		primeiroAChegar = listProcessos[0]
		for i in listProcessos:
			if dicProcesso[primeiroAChegar][1] > dicProcesso[i][1]:
				primeiroAChegar = i
		ordem.append(primeiroAChegar)
		listProcessos.remove(primeiroAChegar)

	dicTempoRestante = {}
	dicTempoQueFalta = {}
	for i in dicProcesso.keys():
		dicTempoQueFalta[i] = dicProcesso[i][0]

	processoEmExe = ordem[0]
	burstEmExe = dicProcesso[ordem[0]][0]
	listProcessos = []
	quantumEmExe = 0

	for exe in range(tempoParaFinalizar):
		quantumEmExe = quantumEmExe + 1
		burstEmExe = burstEmExe - 1
		listProcessos.append(processoEmExe)
		if quantumEmExe == quantum or burstEmExe == 0:
			quantumEmExe = 0
			ordem.remove(processoEmExe)
			dicTempoQueFalta[processoEmExe] = burstEmExe
			if burstEmExe > 0:
				add = 0
				for i in ordem:
					if dicProcesso[i][1] > exe+1:
						ordem.insert(ordem.index(i), processoEmExe)
						add = 1
						break
				if add == 0:
					ordem.append(processoEmExe)
			if len(ordem) > 0:
				if dicProcesso[ordem[0]][1] <= exe:
					processoEmExe = ordem[0]
				else:
					if len(ordem) > 1:
						for i in ordem:
							if dicProcesso[i][1] <= exe:
								processoEmExe = i
								break
			burstEmExe = dicTempoQueFalta[processoEmExe]

	for i, processo in enumerate(listProcessos):
		if i == 0:
			dicTempoRestante[processo] = [i]
			if listProcessos[i+1] != processo:
				temp = dicTempoRestante[processo]
				temp.append(i+1)
				dicTempoRestante[processo] = temp 
		elif i == len(listProcessos)-1:
			temp = dicTempoRestante[processo]
			temp.append(i)
			dicTempoRestante[processo] = temp 
		elif listProcessos[i-1] != processo or processo != listProcessos[i+1]:
			if processo in dicTempoRestante:
				temp = dicTempoRestante[processo]
				temp.append(i)
				dicTempoRestante[processo] = temp 
			else:
				dicTempoRestante[processo] = [i]

	for i in dicProcesso.keys():
		finalDoprocesso = dicTempoRestante[i]
		fdp = finalDoprocesso[len(finalDoprocesso)-1]
		tempoDeEspera =  fdp - dicProcesso[i][1] - dicProcesso[i][0] + 1
		turnAround = fdp + 1 - dicProcesso[i][1]
		temp = dicProcesso[i]
		temp.append(tempoDeEspera)
		temp.append(turnAround)
		dicProcesso[i] = temp 

	tempoDeEspera = 0
	turnAround = 0
	for i in dicProcesso.keys():
		tempoDeEspera = tempoDeEspera + dicProcesso[i][2]
		turnAround = turnAround + dicProcesso[i][3]
	for i in dicProcesso.keys():
		print("\nProcesso %d: Burst =  %d -- Tempo de chegada = %d --Tempo de espera = %d -- Turnaround = %d" %(i, dicProcesso[i][0], dicProcesso[i][1], dicProcesso[i][2], dicProcesso[i][3]))
	print("\n\nTempo medio de espera = %f -- Tempo medio de turnaround = %f" %(tempoDeEspera/len(dicProcesso), turnAround/len(dicProcesso)))


elif entre == 5:
	print("Você selecionou Multinivel: \n A menor prioridade tem maior peso, ou seja quanto menor a prioridade será executado primeiro\n")
	quantum = int(input("\nEntre com o quantum:"))
	quantum2 = int(input("\nEntre com o quantum 2:"))
	nDeProcessos = int(input("Ente com o numero de processos"))
	tempoParaFinalizar = 0
	for processo in range(nDeProcessos):
		burst = int(input("entre com a burst do processo %d :" %(processo+1)))
		tempoParaFinalizar = tempoParaFinalizar + burst
		tDeChegada = 0
		prioridade = int(input("entre com a prioridade do processo %d:" %(processo+1)))
		dicProcesso[processo+1] = [burst, tDeChegada, prioridade]

	ordem = []
	ordem2 = []
	for i in dicProcesso.keys():
		ordem.append(i)

	ordemPrioridade = []
	pri = 0
	while len(ordemPrioridade) != len(ordem):
		for processo in ordem:
			if dicProcesso[processo][2] == pri:
				ordemPrioridade.append(processo)
		pri = pri + 1

	dicTempoRestante = {}
	dicTempoQueFalta = {}
	for i in dicProcesso.keys():
		dicTempoQueFalta[i] = dicProcesso[i][0]

	processoEmExe = ordem[0]
	burstEmExe = dicProcesso[ordem[0]][0]
	listProcessos = []
	quantumEmExe = 0

	while len(ordem):
		quantumEmExe = quantumEmExe + 1
		burstEmExe = burstEmExe - 1
		listProcessos.append(processoEmExe)
		if quantumEmExe == quantum or burstEmExe == 0:
			quantumEmExe = 0
			ordem.remove(processoEmExe)
			dicTempoQueFalta[processoEmExe] = burstEmExe
			if burstEmExe > 0:
				ordem2.append(processoEmExe)
			if len(ordem) > 0:
				processoEmExe = ordem[0]
			burstEmExe = dicTempoQueFalta[processoEmExe]

	while len(ordem2):
		for processo in ordemPrioridade:
			if processo in ordem2:
				ordem.append(processo)
				ordem2.remove(processo)

	processoEmExe = ordem[0]
	burstEmExe = dicTempoQueFalta[ordem[0]]
	quantumEmExe = 0

	while len(ordem):
		quantumEmExe = quantumEmExe + 1
		burstEmExe = burstEmExe - 1
		listProcessos.append(processoEmExe)
		if quantumEmExe == quantum2 or burstEmExe == 0:
			quantumEmExe = 0
			ordem.remove(processoEmExe)
			dicTempoQueFalta[processoEmExe] = burstEmExe
			if burstEmExe > 0:
				add = 0
				for i in ordem:
					if dicProcesso[i][2] > dicProcesso[processoEmExe][2]:
						ordem.insert(ordem.index(i), processoEmExe)
						add = 1
						break
				if add == 0:
					ordem.append(processoEmExe)
			if len(ordem) > 0:
				processoEmExe = ordem[0]
			burstEmExe = dicTempoQueFalta[processoEmExe]

	for i, processo in enumerate(listProcessos):
		if i == 0:
			dicTempoRestante[processo] = [i]
			if listProcessos[i+1] != processo:
				temp = dicTempoRestante[processo]
				temp.append(i+1)
				dicTempoRestante[processo] = temp 
		elif i == len(listProcessos)-1:
			temp = dicTempoRestante[processo]
			temp.append(i)
			dicTempoRestante[processo] = temp 
		elif listProcessos[i-1] != processo or processo != listProcessos[i+1]:
			if processo in dicTempoRestante:
				temp = dicTempoRestante[processo]
				temp.append(i)
				dicTempoRestante[processo] = temp 
			else:
				dicTempoRestante[processo] = [i]

	for i in dicProcesso.keys():
		finalDoprocesso = dicTempoRestante[i]
		fdp = finalDoprocesso[len(finalDoprocesso)-1]
		tempoDeEspera =  fdp - dicProcesso[i][1] - dicProcesso[i][0] + 1
		turnAround = fdp + 1 - dicProcesso[i][1]
		temp = dicProcesso[i]
		temp.append(tempoDeEspera)
		temp.append(turnAround)
		dicProcesso[i] = temp 

	print(listProcessos)
	tempoDeEspera = 0
	turnAround = 0
	for i in dicProcesso.keys():
		tempoDeEspera = tempoDeEspera + dicProcesso[i][2]
		turnAround = turnAround + dicProcesso[i][3]
	for i in dicProcesso.keys():
		print("\nProcesso %d: Burst =  %d -- Tempo de chegada = %d --Tempo de espera = %d -- Turnaround = %d" %(i, dicProcesso[i][0], dicProcesso[i][1], dicProcesso[i][2], dicProcesso[i][3]))
	print("\n\nTempo medio de espera = %f -- Tempo medio de turnaround = %f" %(tempoDeEspera/len(dicProcesso), turnAround/len(dicProcesso)))


else:
	print("Opção invalida")
