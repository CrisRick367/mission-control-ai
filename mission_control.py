NOME_MISSAO = "Helios 1"
NOME_EQUIPE = "Equipe Amon-Rá"

dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

def analisar_temperatura(temp):
    if temp < 18: 
        return "ATENÇÃO", 1, "Temperatura baixa"
    elif 18 <= temp <= 30: 
        return "NORMAL", 0, "Temperatura estável"
    elif 30 < temp <= 35: 
        return "ATENÇÃO", 1, "Temperatura elevada"
    else: 
        return "CRÍTICO", 2, "Risco de superaquecimento"

def analisar_comunicacao(com):
    if com < 30: 
        return "CRÍTICO", 2, "Comunicação em nível crítico"
    elif 30 <= com <= 59: 
        return "ATENÇÃO", 1, "Comunicação instável"
    else: 
        return "NORMAL", 0, "Comunicação estável"

def analisar_bateria(bat):
    if bat < 20: 
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif 20 <= bat <= 49: 
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else: 
        return "NORMAL", 0, "Energia estável"

def analisar_oxigenio(oxi):
    if oxi < 80: 
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif 80 <= oxi <= 89: 
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else: 
        return "NORMAL", 0, "Oxigênio adequado"

def analisar_estabilidade(est):
    if est < 40: 
        return "CRÍTICO", 2, "Estabilidade operacional crítica"
    elif 40 <= est <= 69: 
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"
    else: 
        return "NORMAL", 0, "Estabilidade operacional adequada"

def classificar_ciclo(pontuacao_total):
    if pontuacao_total <= 2: 
        return "MISSÃO ESTÁVEL"
    elif pontuacao_total <= 5: 
        return "MISSÃO EM ATENÇÃO"
    else: 
        return "MISSÃO CRÍTICA"

def analisar_tendencia(risco_primeiro, risco_ultimo):
    if risco_ultimo > risco_primeiro:
        return "A missão apresentou tendência de piora."
    elif risco_ultimo < risco_primeiro:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."

def gerar_recomendacao(status_areas):
    recomendacoes = []
    if status_areas[0] in ["CRÍTICO", "ATENÇÃO"]: recomendacoes.append("Verificar controle térmico")
    if status_areas[1] == "CRÍTICO": recomendacoes.append("Tentar restabelecer contato com a base")
    if status_areas[2] == "CRÍTICO": recomendacoes.append("Ativar modo de economia de energia")
    if status_areas[3] == "CRÍTICO": recomendacoes.append("Acionar protocolo de suporte à vida")
    if status_areas[4] == "CRÍTICO": recomendacoes.append("Reduzir operações não essenciais")

    if not recomendacoes:
        return "Manter operação normal e continuar monitoramento."
    return " | ".join(recomendacoes) + "."

def main():
    print("========================================")
    print("MISSION CONTROL AI")
    print("========================================")
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("========================================")

    riscos_por_ciclo = []
    pontuacao_acumulada_areas = [0, 0, 0, 0, 0]
    soma_valores_areas = [0, 0, 0, 0, 0]
    ciclos_criticos = 0
    ciclo_mais_critico = 0
    maior_pontuacao = -1

    # Requisito 7: Estrutura de repetição para percorrer os ciclos
    for i, ciclo in enumerate(dados_missao):
        temp, com, bat, oxi, est = ciclo

        soma_valores_areas[0] += temp
        soma_valores_areas[1] += com
        soma_valores_areas[2] += bat
        soma_valores_areas[3] += oxi
        soma_valores_areas[4] += est

        # Estruturas condicionais (dentro das funções) geram alertas e pontuações
        st_temp, pt_temp, msg_temp = analisar_temperatura(temp)
        st_com, pt_com, msg_com = analisar_comunicacao(com)
        st_bat, pt_bat, msg_bat = analisar_bateria(bat)
        st_oxi, pt_oxi, msg_oxi = analisar_oxigenio(oxi)
        st_est, pt_est, msg_est = analisar_estabilidade(est)

        pontuacao_acumulada_areas[0] += pt_temp
        pontuacao_acumulada_areas[1] += pt_com
        pontuacao_acumulada_areas[2] += pt_bat
        pontuacao_acumulada_areas[3] += pt_oxi
        pontuacao_acumulada_areas[4] += pt_est

        # Requisito 9: Cálculo de risco por ciclo
        pontuacao_ciclo = pt_temp + pt_com + pt_bat + pt_oxi + pt_est
        riscos_por_ciclo.append(pontuacao_ciclo)

        # Requisito 10: Classificação do ciclo
        classificacao = classificar_ciclo(pontuacao_ciclo)

        if pontuacao_ciclo > maior_pontuacao:
            maior_pontuacao = pontuacao_ciclo
            ciclo_mais_critico = i + 1

        if classificacao == "MISSÃO CRÍTICA":
            ciclos_criticos += 1

        recomendacao = gerar_recomendacao([st_temp, st_com, st_bat, st_oxi, st_est])

        print(f"\nCICLO {i+1}")
        print(f"Temperatura: {temp}°C | {st_temp} | {msg_temp}")
        print(f"Comunicação: {com}% | {st_com} | {msg_com}")
        print(f"Bateria: {bat}% | {st_bat} | {msg_bat}")
        print(f"Oxigênio: {oxi}% | {st_oxi} | {msg_oxi}")
        print(f"Estabilidade: {est}% | {st_est} | {msg_est}")
        print(f"Pontuação de risco do ciclo: {pontuacao_ciclo}")
        print(f"Classificação do ciclo: {classificacao}")
        print(f"Recomendação: {recomendacao}")

    print("\n========================================")
    print("RELATÓRIO FINAL DA MISSÃO")
    print("========================================")
    print(f"Missão: {NOME_MISSAO}\nEquipe: {NOME_EQUIPE}\nQuantidade de ciclos analisados: {len(dados_missao)}")

    qtd_ciclos = len(dados_missao)
    print(f"Média de temperatura: {soma_valores_areas[0]/qtd_ciclos:.2f}°C")
    print(f"Média de comunicação: {soma_valores_areas[1]/qtd_ciclos:.2f}%")
    print(f"Média de bateria: {soma_valores_areas[2]/qtd_ciclos:.2f}%")
    print(f"Média de oxigênio: {soma_valores_areas[3]/qtd_ciclos:.2f}%")
    print(f"Média de estabilidade: {soma_valores_areas[4]/qtd_ciclos:.2f}%")

    print(f"\nCiclo mais crítico: Ciclo {ciclo_mais_critico}")
    print(f"Maior pontuação de risco: {maior_pontuacao}")
    print(f"Risco médio da missão: {sum(riscos_por_ciclo)/qtd_ciclos:.2f}")
    print(f"Quantidade de ciclos críticos: {ciclos_criticos}")

    # Requisito 11: Análise da tendência da missão
    tendencia = analisar_tendencia(riscos_por_ciclo[0], riscos_por_ciclo[-1])
    print(f"\nTendência da missão:\n{tendencia}")

    print("\nPontuação acumulada por área:")
    for i in range(5):
        print(f"{areas_monitoradas[i]}: {pontuacao_acumulada_areas[i]} pontos")

    # Requisito 12: Identificação da área mais afetada
    max_pontos = max(pontuacao_acumulada_areas)
    indice_afetada = pontuacao_acumulada_areas.index(max_pontos)
    print(f"\nÁrea mais afetada:\n{areas_monitoradas[indice_afetada]}")

    risco_medio = sum(riscos_por_ciclo)/qtd_ciclos
    print(f"\nClassificação final da missão:\n{classificar_ciclo(risco_medio)}")

    print("\nConclusão:")
    if risco_medio > 2:
        print("A missão apresentou instabilidade relevante durante a operação. Sistemas exigem acompanhamento.")
    else:
        print("A missão transcorreu dentro dos parâmetros normais de estabilidade.")

if __name__ == "__main__":
    main()