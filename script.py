historicoEnergiaGerada = [
    ["energia_solar", [30, 35, 40]],
    ["energia_eolica", [20, 25, 30]],
]
historicoEntradas = [["energia_solar", [9, 11, 13]], ["energia_eolica", [8, 10, 12]]]
entradaEnergiaSolar = float(input("Insira a quantidade de luz: "))
entradaEnergiaEolica = float(input("Insira a quantidade de vento: "))
consumoEnergia = float(input("Insira o consumo de energia: "))
energiaAtualColonia = float(input("Insira a energia atual: "))


def calcularCoeficienteAngular(historicoEnergiaGerada, historicoEntradas):
    coeficienteAngular = (historicoEnergiaGerada[2] - historicoEnergiaGerada[1]) / (
        historicoEntradas[2] - historicoEntradas[1]
    )

    return coeficienteAngular


def calcularIntercepto(ultimaEnergiaGeradaIndividualmente, coeficienteAngular, entrada):
    intercepto = ultimaEnergiaGeradaIndividualmente - (coeficienteAngular * entrada)

    return intercepto


def preverEnergiaGerada(entradaEnergiaSolar, entradaEnergiaEolica):
    coeficienteAngularEnergiaSolar = calcularCoeficienteAngular(
        historicoEnergiaGerada[0][1], historicoEntradas[0][1]
    )

    interceptoEnergiaSolar = calcularIntercepto(
        historicoEnergiaGerada[0][1][2],
        coeficienteAngularEnergiaSolar,
        historicoEntradas[0][1][2],
    )

    energiaSolarGerada = (
        coeficienteAngularEnergiaSolar * entradaEnergiaSolar + interceptoEnergiaSolar
    )

    coeficienteAngularEnergiaEolica = calcularCoeficienteAngular(
        historicoEnergiaGerada[1][1], historicoEntradas[1][1]
    )

    interceptoEnergiaEolica = calcularIntercepto(
        historicoEnergiaGerada[1][1][2],
        coeficienteAngularEnergiaEolica,
        historicoEntradas[1][1][2],
    )

    energiaEolicaGerada = (
        coeficienteAngularEnergiaEolica * entradaEnergiaEolica + interceptoEnergiaEolica
    )

    return energiaSolarGerada + energiaEolicaGerada


def monitorarEnergiaColonia(consumoEnergia, entradaEnergiaSolar, entradaEnergiaEolica):
    previsaoEnergiaGerada = preverEnergiaGerada(
        entradaEnergiaSolar, entradaEnergiaEolica
    )
    saldoEnergia = energiaAtualColonia - consumoEnergia
    print(
        "Previsão de geração de energia: {}\nSaldo atual de energia: {}".format(
            previsaoEnergiaGerada, saldoEnergia
        )
    )

    if energiaAtualColonia < consumoEnergia:
        print("Ação: Manter suporte à vida ligado e desligar sistemas não essenciais")
    elif (
        energiaAtualColonia > consumoEnergia and consumoEnergia > previsaoEnergiaGerada
    ):
        print("Ação: Reduzir consumo de energia")
    else:
        print("Ação: Armazenar energia excedente")


monitorarEnergiaColonia(consumoEnergia, entradaEnergiaSolar, entradaEnergiaEolica)
