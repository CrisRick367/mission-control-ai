# Mission Control AI - Helios 1

## Descrição do Projeto
O **Mission Control AI** é um sistema em Python para monitoramento de missões espaciais. Ele organiza dados simulados, realiza análises automáticas de risco e gera um relatório com as condições operacionais da missão.

* **Missão:** Helios 1
* **Equipe:** Equipe Amon-Rá

## Estrutura de Dados
Os dados são processados por meio da matriz `dados_missao`. Cada linha corresponde a um ciclo, e as colunas seguem a ordem estrita:
1. Temperatura interna (°C)
2. Comunicação com a base (%)
3. Nível de bateria (%)
4. Suporte de oxigênio (%)
5. Estabilidade operacional (%)

## Regras de Alerta e Pontuação
O sistema classifica as métricas e atribui pontos de risco:
* **NORMAL:** 0 ponto
* **ATENÇÃO:** 1 ponto
* **CRÍTICO:** 2 pontos

### Limites de Classificação:

**Temperatura Interna**
* Abaixo de 18°C: ATENÇÃO
* Entre 18°C e 30°C: NORMAL
* Acima de 30°C até 35°C: ATENÇÃO
* Acima de 35°C: CRÍTICO

**Comunicação com a Base**
* Abaixo de 30%: CRÍTICO
* Entre 30% e 59%: ATENÇÃO
* A partir de 60%: NORMAL

**Sistema de Energia (Bateria)**
* Abaixo de 20%: CRÍTICO
* Entre 20% e 49%: ATENÇÃO
* A partir de 50%: NORMAL

**Suporte de Oxigênio**
* Abaixo de 80%: CRÍTICO
* Entre 80% e 89%: ATENÇÃO
* A partir de 90%: NORMAL

**Estabilidade Operacional**
* Abaixo de 40%: CRÍTICO
* Entre 40% e 69%: ATENÇÃO
* A partir de 70%: NORMAL

## Classificação do Ciclo
A pontuação do ciclo é a soma das 5 áreas analisadas.
* **0 a 2 pontos:** MISSÃO ESTÁVEL
* **3 a 5 pontos:** MISSÃO EM ATENÇÃO
* **6 a 10 pontos:** MISSÃO CRÍTICA

## Execução
```text
mission-control-ai/
├── README.md
└── mission_control.py
