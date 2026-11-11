# Atividade em grupo | Cap 1 - A Aurora Estabelece os Primeiros Sistemas da Colônia

A aplicação simula o monitoramento energético de uma colônia por meio de estimativas de geração solar e eólica. A partir de dados históricos, o sistema calcula a geração prevista de cada fonte, projeta o saldo energético e apresenta recomendações para auxiliar na tomada de decisões.

## Funcionamento

O sistema é dividido em três etapas:

### 1. Previsão de geração energética

O programa utiliza três registros históricos de cada fonte energética, relacionando as condições ambientais com a quantidade de energia gerada.

Para estimar a geração, aplica a **regressão linear pelo método dos mínimos quadrados**, calculando os coeficientes angular e linear de uma reta para cada fonte.

Com os valores informados pelo usuário, são realizadas duas previsões independentes:

- **Solar:** estima a geração a partir da quantidade de luz.
- **Eólica:** estima a geração a partir da quantidade de vento.

As estimativas são somadas para determinar a geração total prevista.

### 2. Cálculo do saldo energético

O sistema considera a reserva atual da colônia, o consumo informado e a geração total prevista.

O cálculo é representado pela seguinte expressão:

$$
S_{\text{final}} = E_{\text{atual}} - C + G_{\text{prevista}}
$$

Onde:

- $S_{\text{final}}$: saldo energético projetado;
- $E_{\text{atual}}$: reserva atual de energia;
- $C$: consumo informado;
- $G_{\text{prevista}}$: geração total estimada.

### 3. Tomada de decisão

Com base no saldo energético projetado, o programa avalia condições predefinidas e apresenta uma recomendação:

| Condição avaliada | Ação recomendada |
|---|---|
| Saldo projetado menor que o consumo | Manter o suporte à vida ligado e desligar sistemas não essenciais |
| Saldo projetado maior que o consumo e consumo maior que a geração prevista | Reduzir o consumo de energia |
| Demais situações | Armazenar energia excedente |

## Tecnologias e conceitos

- **Python 3**
- Listas e listas aninhadas
- Funções e modularização
- Estruturas condicionais
- Regressão linear por mínimos quadrados
- Operações matemáticas

## Como executar

**Pré-requisito:** Python 3 instalado.

Clone o repositório:

```bash
git clone https://github.com/kelvencarlos/fiap-03.git
```

Acesse a pasta:

```bash
cd fiap-03
```

Execute o arquivo principal:

```bash
python script.py
```

Substitua `script.py` pelo nome do arquivo Python que contém a implementação.

Não são necessárias bibliotecas externas.

## Exemplo de execução

A seguir, um exemplo utilizando os seguintes valores:

| Parâmetro | Valor informado |
|---|---:|
| Quantidade de luz | 10 |
| Quantidade de vento | 10 |
| Reserva atual da colônia | 100 |
| Consumo atual | 80 |

**Saída:**

```text
Insira a quantidade de luz: 10

Coeficiente angular: 2.5
Entrada de energia: 10.0
Intercepto: 7.5
Equação da reta: y = 2.5 x + 7.5
Energia gerada: 32.5 (Solar)

Insira a quantidade de vento: 10

Coeficiente angular: 2.5
Entrada de energia: 10.0
Intercepto: 0.0
Equação da reta: y = 2.5 x + 0.0
Energia gerada: 25.0 (Eólica)

Insira a reserva de energia atual da colônia: 100

Insira o consumo de energia atual da colônia: 80

Energia gerada: 57.5
Consumo atual da colônia: 80.0
Reserva de energia atual da colônia: 100.0
Saldo final de energia da colônia: 77.5

Ação: Manter suporte à vida ligado e desligar sistemas não essenciais
```

Nesse cenário, a geração solar prevista é de 32,5 unidades e a geração eólica é de 25 unidades, totalizando 57,5 unidades.

O saldo projetado é:

$$
S_{\text{final}} = 100 - 80 + 57{,}5 = 77{,}5
$$

Como o resultado é inferior ao consumo informado (80), o programa seleciona a primeira regra de decisão.

## Documentação técnica

Para conhecer os detalhes da implementação, incluindo a organização dos dados, o desenvolvimento matemático da regressão linear, os cálculos dos coeficientes, os gráficos e as limitações da solução, consulte o relatório técnico disponível neste repositório.