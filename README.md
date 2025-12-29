# Log Analyzer em Python (Relatório de Eficiência de API)

## Visão Geral

Este projeto é um _script_ de automação em **Python** projetado para processar logs de servidor e gerar um relatório conciso sobre o desempenho e a confiabilidade de _endpoints_ de API.

O objetivo é transformar dados brutos de log em métricas acionáveis, permitindo a **identificação rápida de gargalos de performance** (latência alta) e a **taxa de erros** por rota. Esta ferramenta simula o trabalho de engenharia de _observability_ e otimização de sistemas, uma prática essencial no desenvolvimento Back-end.

## Por que este projeto é relevante

O projeto demonstra a capacidade de ir além do desenvolvimento básico, focando em métricas de sistema:

-   **Análise de Desempenho:** Prova a habilidade de usar dados para encontrar e diagnosticar problemas de _performance_ e _escalabilidade_.
-   **Scripts de Automação:** Confirma a proficiência na criação de ferramentas de automação e análise em **Python**.
-   **Identificação de Gargalos:** Replica a função de análise exploratória de dados para identificar ineficiências.

## Tecnologias Utilizadas

-   **Python:** Linguagem principal para processamento e análise.
-   **Módulos Nativos:** `re` (Expressões Regulares) para parsear os logs e `collections` (`defaultdict`) para agregação eficiente de dados.

## Design e Tradeoffs (Compensações de Design)

No design desta ferramenta, a principal compensação (_tradeoff_) foi entre **Velocidade de Processamento (Eficiência)** e **Complexidade de Ferramentas (Simplicidade)**, demonstrando a capacidade de fazer escolhas bem fundamentadas:

| Característica                  | Decisão Tomada                                  | Justificativa (Tradeoff)                                                                                                                                                                                                                                            |
| :------------------------------ | :---------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Ferramenta de Processamento** | Uso de **Python nativo** (`re`, `defaultdict`). | **Ganho:** Simplicidade, zero dependências e alta velocidade para arquivos de médio porte. **Sacrifício:** Não oferece o poder de escalabilidade de ferramentas complexas. Priorizei a **rapidez na entrega da análise**.                                           |
| **Parsing de Logs**             | Uso de **Expressões Regulares (`re`)**.         | **Ganho:** Flexibilidade para adaptar o script a diferentes formatos de log com facilidade. **Sacrifício:** É ligeiramente mais lento que métodos de _string_ puro, mas oferece maior **robustez** e **manutenibilidade** do código para diferentes padrões de log. |

## 🚀 Como Executar o Projeto

### Pré-requisitos

Certifique-se de ter o Python 3 instalado. Nenhuma biblioteca externa é necessária.

### Instalação

Clone este repositório para sua máquina local:

```bash
git clone https://github.com/luscaBr2/log-analyzer.git
```

Garanta que o arquivo server.log (contendo logs no formato esperado) exista no mesmo diretório.
Execute o script no seu terminal:

```bash
py log_analyzer.py
```
