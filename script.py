historicoEnergiaGerada = [
    ["energia_solar", [30, 35, 40]],
    ["energia_eolica", [20, 25, 30]],
]
historicoEntradas = [["energia_solar", [9, 11, 13]], ["energia_eolica", [8, 10, 12]]]


def calcularCoeficienteAngular(historicoEnergiasGerada, historicoEntradas):
    quantidadeObservacoes = len(historicoEnergiasGerada)
    somaEntradas = historicoEntradas[0] + historicoEntradas[1] + historicoEntradas[2]
    somaGeracoes = (
        historicoEnergiasGerada[0]
        + historicoEnergiasGerada[1]
        + historicoEnergiasGerada[2]
    )
    somaMultiplicacoesEntradasGeracoes = (
        historicoEntradas[0] * historicoEnergiasGerada[0]
        + historicoEntradas[1] * historicoEnergiasGerada[1]
        + historicoEntradas[2] * historicoEnergiasGerada[2]
    )
    somaQuadradosEntradas = (
        historicoEntradas[0] * historicoEntradas[0]
        + historicoEntradas[1] * historicoEntradas[1]
        + historicoEntradas[2] * historicoEntradas[2]
    )
    coeficienteAngular = (
        (quantidadeObservacoes * somaMultiplicacoesEntradasGeracoes)
        - (somaEntradas * somaGeracoes)
    ) / (
        (quantidadeObservacoes * somaQuadradosEntradas) - (somaEntradas * somaEntradas)
    )

    return coeficienteAngular


def calcularIntercepto(coeficienteAngular, historicoEnergiasGeradas, historicoEntradas):
    somaEnergiasGeradas = (
        historicoEnergiasGeradas[0]
        + historicoEnergiasGeradas[1]
        + historicoEnergiasGeradas[2]
    )
    somaEntradas = historicoEntradas[0] + historicoEntradas[1] + historicoEntradas[2]
    quantidadeObservacoes = len(historicoEnergiasGeradas)
    intercepto = (
        somaEnergiasGeradas - (coeficienteAngular * somaEntradas)
    ) / quantidadeObservacoes

    return intercepto


def preverEnergiaGerada(entradaEnergia, historicoEnergiaGerada, historicoEntradas):
    coeficienteAngularEnergia = calcularCoeficienteAngular(
        historicoEnergiaGerada[1], historicoEntradas[1]
    )

    intercepto = calcularIntercepto(
        coeficienteAngularEnergia,
        historicoEnergiaGerada[1],
        historicoEntradas[1],
    )

    energiaGerada = coeficienteAngularEnergia * entradaEnergia + intercepto

    if historicoEnergiaGerada[0] == "energia_solar":
        print(
            "Coeficiente angular: {}\nEntrada de energia: {}\nIntercepto: {}\nEquação da reta: y = {} x {} + {}\nEnergia gerada: {} (Solar)\n".format(
                coeficienteAngularEnergia,
                entradaEnergia,
                intercepto,
                coeficienteAngularEnergia,
                entradaEnergia,
                intercepto,
                energiaGerada,
            )
        )
    else:
        print(
            "Coeficiente angular: {}\nEntrada de energia: {}\nIntercepto: {}\nEquação da reta: y = {} x {} + {}\nEnergia gerada: {} (Eólica)\n".format(
                coeficienteAngularEnergia,
                entradaEnergia,
                intercepto,
                coeficienteAngularEnergia,
                entradaEnergia,
                intercepto,
                energiaGerada,
            )
        )

    return energiaGerada


def monitorarEnergiaIndividualmente(
    entradaEnergia, historicoEnergiaGerada, historicoEntradas
):
    previsaoEnergiaGerada = preverEnergiaGerada(
        entradaEnergia, historicoEnergiaGerada, historicoEntradas
    )

    return previsaoEnergiaGerada


entradaEnergiaSolar = float(input("Insira a quantidade de luz: "))

energiaSolarGerada = monitorarEnergiaIndividualmente(
    entradaEnergiaSolar, historicoEnergiaGerada[0], historicoEntradas[0]
)

entradaEnergiaEolica = float(input("Insira a quantidade de vento: "))

energiaEolicaGerada = monitorarEnergiaIndividualmente(
    entradaEnergiaEolica, historicoEnergiaGerada[1], historicoEntradas[1]
)

energiaAtualColonia = float(input("Insira a reserva de energia atual da colônia: "))

consumoEnergia = float(input("Insira o consumo de energia atual da colônia: "))


def calcularSaldoEnergiaColonia(
    energiaAtualColonia, energiaSolarGerada, energiaEolicaGerada, consumoEnergia
):
    energiaPrevista = energiaSolarGerada + energiaEolicaGerada

    saldoEnergiaFinal = energiaAtualColonia - consumoEnergia + energiaPrevista

    print(
        "\nEnergia gerada: {}\nConsumo atual da colônia: {}\nReserva de energia atual da colônia {}\nSaldo final de energia da colônia: {}\n".format(
            energiaPrevista, consumoEnergia, energiaAtualColonia, saldoEnergiaFinal
        )
    )

    if saldoEnergiaFinal < consumoEnergia:
        print("Ação: Manter suporte à vida ligado e desligar sistemas não essenciais")
    elif saldoEnergiaFinal > consumoEnergia and consumoEnergia > energiaPrevista:
        print("Ação: Reduzir consumo de energia")
    else:
        print("**Ação: Armazenar energia excedente**")


calcularSaldoEnergiaColonia(
    energiaAtualColonia, energiaSolarGerada, energiaEolicaGerada, consumoEnergia
)
