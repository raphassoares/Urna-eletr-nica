# Trabalho da disciplina - Fazer uma urna eletrônica

# Pela leitura do arquivo do trabalho e pensando no funcionamento básico eu preciso de:
# def para o menu
# def main  e condição para conferir e deixar a main ( que é o menu ) rodando.
# def para ler os dados dos candidatos que estarão em um arquivo.txt
# def para ler os dados dos eleitores que estarão em um arquivo.txt
# def para controlar a votação
# def para organizar e mandar para um arquivo os votos
# def para apurar os votos
# def para divulgar o resultado

import pickle
import matplotlib.pyplot as plt


def ler_candidatos():
    # Como vamos ler informações que vão estar em um arquivo, precisamos setar isso para o programa
    arquivo_candidatos = "candidatos.txt"

    # Cria uma lista vazia para armazenar os dados dos candidatos que vamos ler no arquivo candidato
    candidatos = []

    with open(arquivo_candidatos, 'r', encoding='utf-8') as arquivo:
        # Aqui estamos abrindo e lendo o arquivo candidatos no modo 'r', modo leitura, seguindo o encoding citado e
        # estamos chamando o conteúdo dentro dele de "arquivo"
        linhas = arquivo.readlines()
        # Aqui estamos definindo linhas e estamos lendo todas as linhas do arquivo e armazenando-as em uma lista

        # Itera sobre cada linha do arquivo, percorrendo-as.
        for linha_numero, linha in enumerate(linhas, start=1):
            try:
                # Abaixo eu vou usar o comando split para dividir os elementos dentro da linha. Vou usar o marcador
                # da vírgula "," como separador de cada um dos elementos da linha
                dados = linha.strip().split(',')

                # Antes de eu definir o que cada elemento dentro de "dados" é, eu quero confirmar se tem 5
                # Aqui está verificando se tem exatamente 5 elementos, ou seja, se len(dados)
                if len(dados) != 5:
                    # não for igual a 5, então...
                    raise ValueError(
                        # Gera um erro se o formato não for válido
                        "Formato inválido na linha {}: {}".format(linha_numero, linha))

                # Agora, cabe a nós extrair, de dentro da linha, os dados e para eles, criar um dicionário
                # Em outras palavras, eu estou pegando aquilo que está separado por vírgula e dando nome
                nome, numero, partido, estado, cargo = dados
                # Cria o dicionário "candidato"
                candidato = {'nome': nome.strip(), 'numero': int(numero.strip()), 'partido': partido.strip(),
                             'estado': estado.strip(), 'cargo': cargo.strip()}

                # Adiciona o dicionário à lista de candidatos
                candidatos.append(candidato)

            except Exception as e:
                # Tratar erros e imprimir informações sobre a linha com erro
                print("Erro na linha {}: {} - {}".format(linha_numero,
                                                         linha.strip(), str(e)))  # Imprime informações sobre o erro na linha

    # Retornar a lista de candidatos
    return candidatos  # Retorna a lista de candidatos após o processamento do arquivo


def ler_eleitores():
    arquivo_eleitores = "eleitores.txt"

    # cria uma lista vazia para armazenar os eleitores
    eleitores = []

    # Vou abrir o arquivo eleitores em modo leitura de novo, passar pelas linhas do arquivo e deixar salvo isso na variável linhas
    with open(arquivo_eleitores, 'r', encoding='utf-8') as arquivo:
        # Ler todas as linhas
        linhas = arquivo.readlines()

        # Agora, vou iterar sobre as linhas do arquivo
        for linha_numero, linha in enumerate(linhas, start=1):
            try:
                # Aqui, eu vou dividir o que tem dentro da linha criando vários elementos dentro dela. O que eu estou
                # utilizando como marcador para separar é a vírgula ","
                dados = linha.strip().split(',')

                # Ok, na linha de cima eu pedi para dividir tudo que está dentro da linha. Essa divisão, para atender o código
                # abaixo precisa criar 5 elementos. Caso não crie, vai dar errado, por essa razão eu preciso ter certeza, verificando...
                if len(dados) != 5:
                    raise ValueError(
                        "Formato inválido na linha {}: {}".format(linha_numero, linha))
                # O que aconteceu acima: Bascimente uma condição if que, se não tiver 5 elementos pós dividão, está errado e o código aponta onde

                # Eu criei a variável dados ali em cima. Ela vem da leitura do arquivo eleitores. Porém, essa variável agora,
                # carrega uma lista, com 5 elementos, que estão divididos pela virgula.
                # o que está rolando abaixo? Estou definindo que, dentro de "dados" tem outras 5 variáveis. Estou apontando quem
                # elas são e quais são seus valores. Vale lembrar que a orgem que eu coloco é importante.
                # os dados de 'nome' estão indo para a variavel nome pq elas estão na mesma posição ali.
                nome, rg, titulo_eleitor, municipio, estado = dados
                eleitor = {'nome': nome.strip(), 'rg': rg.strip(), 'titulo_eleitor': titulo_eleitor.strip(),
                           'municipio': municipio.strip(), 'estado': estado.strip()}

                # agora, com toda essa organização, eu vou adicionar a variável eleitor, toda organizada como está acima
                # dentro da lista eleitores, que está vazia e criamos no começo dessa def
                eleitores.append(eleitor)

            except Exception as e:
                # Tratar erros e imprimir informações sobre a linha com erro
                print("Erro na linha {}: {} - {}".format(linha_numero,
                      linha.strip(), str(e)))

    # retorna a lista de eleitores
    return eleitores


def verificar_titulo_eleitor(eleitor_titulo, eleitores):

    # itera sobre a lista de eleitores
    for eleitor in eleitores:
        # compara o título de eleitor inserido via input com o valor titulo_eleitor dentro da varivável eleitor
        if eleitor_titulo == eleitor['titulo_eleitor']:
            return True  # Isso quer dizer que o título digitado pelo eleitor for comparado e está ok com o do arquivo

    # Se o valor do input percorrer a lista e não encontrar nada compativel
    return False


def coleta_votos(candidatos, eleitores, votos, eleitores_que_votaram):
    op = "S"
    uf_urna = input("Digite a UF da urna: ").upper()
    while op == "S":
        titulo_eleitor = input("Digite seu título de eleitor para votar: ")
        if verificar_titulo_eleitor(titulo_eleitor, eleitores) and titulo_eleitor not in eleitores_que_votaram:
            eleitor_autenticado = True
            print("Eleitor autenticado. Pode prosseguir com a votação")
            eleitor = [
                eleitor for eleitor in eleitores if eleitor['titulo_eleitor'] == titulo_eleitor][0]
            print("Eleitor: ", eleitor['nome'])
            print("Estado: ", eleitor['estado'])
        else:
            eleitor_autenticado = False
            print(
                "Título de eleitor não encontrado ou eleitor já votou...\n Retornando para o Menu")
            return votos, eleitores_que_votaram

        # Adiciona o título do eleitor à lista de eleitores que já votaram
        eleitores_que_votaram.append(titulo_eleitor)

        voto_nominal = {}

        # Coletamos os votos para cada cargo, agora seguindo a nova ordem
        voto_nominal['Deputado Estadual'] = coletar_voto(
            "Deputado Estadual: ", candidatos, [], uf_urna)
        voto_nominal['Deputado Federal'] = coletar_voto(
            "Deputado Federal: ", candidatos, [])
        voto_nominal['Senador'] = coletar_voto(
            "Senador: ", candidatos, [], uf_urna)
        voto_nominal['Governador'] = coletar_voto(
            "Governador: ", candidatos, [], uf_urna)
        voto_nominal['Presidente'] = coletar_voto(
            "Presidente: ", candidatos, [])

        votos.append({'eleitor': eleitor, 'voto_nominal': voto_nominal})

        print("Voto registrado com sucesso!")

        op = input("Deseja continuar a votação? S/N: ").upper()

    return votos, eleitores_que_votaram


def coletar_voto(cargo, candidatos, candidatos_votados, uf_urna=None):
    while True:
        numero_candidato = input(f"Informe o voto para {
                                 cargo} (ou deixe em branco para voto em branco): ").strip()

        if numero_candidato == "":
            confirmacao_branco = input(
                "Confirma o voto em branco (S ou N)? ").upper()
            if confirmacao_branco == 'S':
                return None  # Voto em branco
            else:
                print("Voto cancelado. Informe outro número.")
        elif numero_candidato.isdigit():
            numero_candidato = int(numero_candidato)

            candidato_encontrado = next(
                (candidato for candidato in candidatos if candidato['numero'] == numero_candidato
                 and candidato not in candidatos_votados
                 and (uf_urna is None or candidato['estado'] == uf_urna)),
                None
            )

            if candidato_encontrado:
                print(f"Candidato: {candidato_encontrado['nome']} | Partido: {
                      candidato_encontrado['partido']}")
                confirmacao = input("Confirma o voto (S ou N)? ").upper()

                if confirmacao == 'S':
                    return candidato_encontrado
                else:
                    print("Voto cancelado. Informe outro número.")
            else:
                confirmacao_nulo = input(
                    "Número de candidato inválido. Confirma anular o voto (S ou N)? ").upper()
                if confirmacao_nulo == 'S':
                    print("Voto anulado.")
                    return None  # Voto nulo
                else:
                    print("Voto cancelado. Informe outro número.")
        else:
            confirmacao_nulo = input(
                "Número inválido. Confirma anular o voto (S ou N)? ").upper()
            if confirmacao_nulo == 'S':
                print("Voto anulado.")
                return None  # Voto nulo
            else:
                print("Voto cancelado. Informe outro número.")


def salvar_votos(votos):
    # Nome do arquivo binário
    nome_arquivo_binario = "votos.bin"

    # Abrir o arquivo binário em modo de escrita (wb) usando a codificação UTF-8
    with open(nome_arquivo_binario, 'wb') as arquivo_binario:
        # Usa o módulo pickle para serializar e salvar os votos no arquivo binário
        pickle.dump(votos, arquivo_binario, protocol=pickle.HIGHEST_PROTOCOL)


def apurar_votos(votos, candidatos):
    resultados = {'Deputado Estadual': {'candidatos': {}, 'estado': None, 'votos': 0},
                  'Deputado Federal': {'candidatos': {}, 'estado': None, 'votos': 0},
                  'Senador': {'candidatos': {}, 'estado': None, 'votos': 0},
                  'Governador': {'candidatos': {}, 'estado': None, 'votos': 0},
                  'Presidente': {'candidatos': {}, 'estado': None, 'votos': 0}}

    for voto in votos:
        # Ajuste aqui para considerar apenas um voto nominal por eleitor
        eleitor = voto['eleitor']
        voto_nominal = voto['voto_nominal']
        for cargo, candidato in voto_nominal.items():
            if candidato:
                if candidato['numero'] not in resultados[cargo]['candidatos']:
                    resultados[cargo]['candidatos'][candidato['numero']] = {
                        'nome': candidato['nome'],
                        'partido': candidato['partido'],
                        'votos': 0
                    }
                resultados[cargo]['estado'] = candidato['estado']
                resultados[cargo]['candidatos'][candidato['numero']
                                                ]['votos'] += 1
                resultados[cargo]['votos'] += 1

    # Correção aqui para contar apenas um voto por eleitor
    total_votos = len(votos)

    return resultados, total_votos


def mostrar_resultados(resultados, eleitores_aptos, total_votos, candidatos):
    print("\n==== Resultados ====")
    print(f"Eleitores Aptos: {eleitores_aptos}")
    print(f"Total de Votos Nominais: {total_votos}")

    print()

    for cargo, info in resultados[0].items():
        percentual_cargo = (info['votos'] / total_votos) * \
            100 if total_votos > 0 else 0
        print(f"Cargo: {cargo} | Estado: {info['estado']} | Votos: {
              info['votos']} ({percentual_cargo:.2f}%)")

        # Encontrar o candidato eleito (com maior porcentagem)
        candidato_eleito = max(info['candidatos'].values(
        ), key=lambda x: x['votos'] / info['votos'] if info['votos'] > 0 else 0)

        for numero, candidato_info in info['candidatos'].items():
            percentual_candidato = (
                candidato_info['votos'] / info['votos']) * 100 if info['votos'] > 0 else 0
            resultado_formatado = f"Candidato: {candidato_info['nome']} | Partido: {
                candidato_info['partido']} | Votos: {candidato_info['votos']} ({percentual_candidato:.2f}%)"

            # Adicionar "Eleito" ao candidato com maior porcentagem
            if candidato_info == candidato_eleito:
                resultado_formatado += " - Eleito"

            print(resultado_formatado)

        print()


def mostrar_grafico(resultados):
    # Função para mostrar gráfico de resultados
    cargos = []
    votos = []
    nomes_eleitos = []

    for cargo, info in resultados[0].items():
        # Encontrar o candidato eleito (com maior porcentagem)
        candidato_eleito = max(info['candidatos'].values(),
                               key=lambda x: x['votos'] / info['votos'] if info['votos'] > 0 else 0)

        cargos.append(cargo)
        votos.append(info['votos'])
        nomes_eleitos.append(candidato_eleito['nome'])

    # Criar gráfico de barras
    fig, ax = plt.subplots()
    bars = ax.bar(cargos, votos, color='blue')

    # Adicionar nome do eleito sobre cada barra
    for bar, nome_eleito in zip(bars, nomes_eleitos):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height,
                nome_eleito, ha='center', va='bottom', fontsize=8, fontweight='bold')

    plt.xlabel('Cargos')
    plt.ylabel('Número de Votos')
    plt.title('Resultado da Eleição')
    plt.show()


def menu_principal():
    # Função que define e organiza o menu e sua lógica
    # Dar início às variáveis
    candidatos = []
    eleitores = []
    votos = []
    resultados = None  # Inicializa resultados como None
    eleitores_que_votaram = []  # Lista para armazenar eleitores que já votaram

    while True:
        # Opções do Menu
        print("\n==== Menu Principal ====")
        print("1 - Ler arquivo de candidatos")
        print("2 - Ler arquivo de eleitores")
        print("3 - Inicial Votação")
        print("4 - Apurar votos")
        print("5 - Mostrar resultados")
        print("6 - Fechar programa")
        print("7 - Mostrar gráfico")

        # Para obter a escolha do usuário:
        escolha = input("Escolha a opção (1 a 7): ")

        # Realiza a ação de acordo com a escolha do usuário:
        if escolha == "1":
            candidatos = ler_candidatos()
            print("Arquivo de candidatos lido com sucesso.")
        elif escolha == "2":
            eleitores = ler_eleitores()
            print("Arquivo de eleitores lido com sucesso")
        elif escolha == "3":
            votos, eleitores_que_votaram = coleta_votos(
                candidatos, eleitores, votos, eleitores_que_votaram)
        elif escolha == "4":
            resultados = apurar_votos(votos, candidatos)
        elif escolha == "5":
            if resultados is not None:
                eleitores_aptos = len(eleitores)
                total_votos = len(votos)
                mostrar_resultados(resultados, eleitores_aptos,
                                   total_votos, candidatos)
            else:
                print("Você precisa apurar os votos antes de mostrar os resultados.")
        elif escolha == "6":
            print("Encerrando o programa. Até logo!")
            break
        elif escolha == "7":  # Adicione a opção para mostrar o gráfico
            if resultados is not None:
                mostrar_grafico(resultados)
            else:
                print("Você precisa apurar os votos antes de mostrar o gráfico.")
        else:
            print("Opção inválida. Por favor, escolha de 1 a 7.")


def main():
    # Ela serve para chamar a função "menu_principal" e iniciar o programa
    menu_principal()
    # Aqui está sendo definindo o def munu_principal como a função principal do programa


if __name__ == "__main__":
    # chama a função principal
    main()
    # Aqui, basicamente estão verificando se o escript está sendo executado como programa principal, e ele faz isso
    # chamando a função principal.
