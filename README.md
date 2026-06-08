# Mission Control AI - Helios 1

## Descrição do Projeto
[cite_start]O **Mission Control AI** é um sistema em Python desenvolvido para simular o monitoramento inteligente de uma missão espacial experimental[cite: 8]. [cite_start]O programa organiza dados simulados, analisa-os de forma automática e gera um relatório detalhado sobre as condições operacionais da missão[cite: 9].

* **Nome da Missão:** Helios 1
* **Nome da Equipe:** Equipe Amon-Rá

## Estrutura de Dados
[cite_start]A base do projeto utiliza uma matriz principal chamada `dados_missao` [cite: 46][cite_start], estruturada como uma lista de listas onde cada linha representa um ciclo de monitoramento e cada coluna representa uma informação específica[cite: 49, 50, 51]. [cite_start]A ordem exata das colunas é[cite: 59, 60]:
1. [cite_start]**Temperatura:** Temperatura interna do módulo em °C[cite: 61].
2. [cite_start]**Comunicação:** Qualidade do sinal de comunicação com a base em %[cite: 61].
3. [cite_start]**Bateria:** Nível de bateria do sistema de energia em %[cite: 61].
4. [cite_start]**Oxigênio:** Nível de oxigênio disponível no suporte de vida em %[cite: 61].
5. [cite_start]**Estabilidade:** Estabilidade geral dos sistemas operacionais em %[cite: 61].

## Regras de Alerta e Pontuação de Risco
[cite_start]Cada parâmetro é classificado automaticamente e recebe uma pontuação específica de risco[cite: 129, 146]:
* [cite_start]**NORMAL:** 0 ponto[cite: 147].
* [cite_start]**ATENÇÃO:** 1 ponto[cite: 148].
* [cite_start]**CRÍTICO:** 2 pontos[cite: 149].

### Critérios de Classificação por Área:

#### [cite_start]Temperatura Interna [cite: 134, 135]
* Menor que 18°C: ATENÇÃO (1 ponto)
* De 18°C até 30°C: NORMAL (0 pontos)
* Maior que 30°C até 35°C: ATENÇÃO (1 ponto)
* Maior que 35°C: CRÍTICO (2 pontos)

#### [cite_start]Comunicação com a Base [cite: 136, 137]
* Menor que 30%: CRÍTICO (2 pontos)
* De 30% até 59%: ATENÇÃO (1 ponto)
* 60% ou mais: NORMAL (0 pontos)

#### [cite_start]Sistema de Energia (Bateria) [cite: 138, 140]
* Menor que 20%: CRÍTICO (2 pontos)
* De 20% até 49%: ATENÇÃO (1 ponto)
* 50% ou mais: NORMAL (0 pontos)

#### [cite_start]Suporte de Oxigênio [cite: 141, 142]
* Menor que 80%: CRÍTICO (2 pontos)
* De 80% até 89%: ATENÇÃO (1 ponto)
* 90% ou mais: NORMAL (0 pontos)

#### [cite_start]Estabilidade Operacional [cite: 143, 144]
* Menor que 40%: CRÍTICO (2 pontos)
* De 40% até 69%: ATENÇÃO (1 ponto)
* 70% ou mais: NORMAL (0 pontos)

## Análise de Ciclo e Relatório Final

* [cite_start]**Pontuação do Ciclo:** É a soma dos pontos de risco das 5 áreas monitoradas, variando de 0 a 10 pontos[cite: 150].
* [cite_start]**Classificação do Estado do Ciclo[cite: 157]:**
  * 0 a 2 pontos: MISSÃO ESTÁVEL
  * 3 a 5 pontos: MISSÃO EM ATENÇÃO
  * 6 a 10 pontos: MISSÃO CRÍTICA
* [cite_start]**Análise de Tendência:** Compara o risco do primeiro ciclo com o do último ciclo[cite: 159]. [cite_start]Se o último for maior, a tendência é de piora; se for menor, é de melhora; se for igual, permaneceu estável[cite: 165, 166, 167].
* [cite_start]**Área Mais Afetada:** Identificada por meio da soma da pontuação de risco de cada área ao longo de todos os ciclos, determinando qual setor acumulou maior criticidade[cite: 170].

## [cite_start]Estrutura do Repositório [cite: 341, 342]
```text
mission-control-ai/
├── README.md
└── mission_control.py
