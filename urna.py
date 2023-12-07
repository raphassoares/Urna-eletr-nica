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
# fornece funcionalidades para serialização e desserialização de objetos Python, permitindo a gravação e leitura de dados de forma eficiente.

import matplotlib.pyplot as plt
# utilizada para criação de gráficos e visualizações, sendo pyplot uma interface para interagir com o Matplotlib de maneira semelhante ao MATLAB.


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
    # para cada eleitor dentro de eleitores - sendo que ambos vem da def ler_eleitores -
    for eleitor in eleitores:
        # compara o título de eleitor inserido via input com o valor titulo_eleitor dentro da varivável eleitor
        if eleitor_titulo == eleitor['titulo_eleitor']:
            # Isso quer dizer que o título digitado pelo eleitor for comparado e está ok com o do arquivo
            return True, eleitor['estado']
        # devolve o título e o estado do eleitor para ser usado posteriormente
    return False, None


def coleta_votos(candidatos, eleitores, votos, eleitores_que_votaram):
    op = "S"
    while True:
        # Cria uma repetição para que a UF apenas aceite letras e, em caso de algo diferente, pede apenas letras e volta
        # para a repetição até ser só letas
        uf_urna = input("Digite a UF da urna: ").upper()

    # Verifica se a entrada contém apenas letras
        if uf_urna.isalpha():
            print("UF da urna:", uf_urna)
            break
        else:
            print("Por favor, digite apenas letras. Tente novamente.")

    while op == "S":
        # Cria a repetição que, enquanto a resposta para a pergunta lá no final,
        # se eu quero continuar a votação for S, a votação vai continuar.
        titulo_eleitor = input("Digite seu título de eleitor para votar: ")

       # Verifica o título do eleitor e obtém o estado associado a esse título
        titulo_valido, estado_eleitor = verificar_titulo_eleitor(
            titulo_eleitor, eleitores)

        if titulo_valido and titulo_eleitor not in eleitores_que_votaram:
            # Verifica se o estado do eleitor é o mesmo da UF digitada
            if estado_eleitor == uf_urna:
                eleitor_autenticado = True
                print("Eleitor autenticado. Pode prosseguir com a votação")
                eleitor = [
                    eleitor for eleitor in eleitores if eleitor['titulo_eleitor'] == titulo_eleitor][0]
                print("Eleitor: ", eleitor['nome'])
                print("Estado: ", eleitor['estado'])
            else:
                eleitor_autenticado = False
                print(
                    "O estado do eleitor não corresponde à UF da urna. Eleitor não autorizado a votar.")
                return votos, eleitores_que_votaram
        else:
            eleitor_autenticado = False
            print(
                "Título de eleitor não encontrado ou eleitor já votou...\n Retornando para o Menu")
            return votos, eleitores_que_votaram

        eleitores_que_votaram.append(titulo_eleitor)
        # Adiciona o título do eleitor à lista de eleitores que já votaram. Isso quer dizer que, no processo de votação, depois que o título de eleitor 1 votar, ele não pode repetir
        # pois ele foi adicionado ao parâmetro eleitores_que_votaram.

        voto_nominal = {}
        # Inicializa um dicionário vazio para armazenar os votos nominais.

        # Coletamos os votos para cada cargo, respeitando a função coletar_votos, que é quem está definindo a lógica da coleta - o que pode e o que não pode -.
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
        # Note que, apenas os votos para deputado federal e presidente não usam a variável uf_urna.
        # isso porque, é com o uso dela que filtramos os votos ( cargos que são atrelados a estados devem obedecer a uf da urna)
        votos.append({'eleitor': eleitor, 'voto_nominal': voto_nominal})
        # Adiciona um dicionário contendo informações sobre o eleitor e seus votos à lista de votos.

        print("Voto registrado com sucesso!")

        op = input("Deseja continuar a votação? S/N: ").upper()
        # Solicita ao usuário se deseja continuar a votação e converte a resposta para letras maiúsculas. Aqui, no caso, nós ainda estamos dentro daquele while lá de cima.

    return votos, eleitores_que_votaram
    # Retorna as listas 'votos' e 'eleitores_que_votaram' após a conclusão da votação.


def coletar_voto(cargo, candidatos, candidatos_votados, uf_urna=None):
    # Define uma função chamada coletar_voto que recebe quatro parâmetros: cargo, candidatos, candidatos_votados e uf_urna.
    # Aqui está sendo definida a regra lógica da votação.

    while True:
        numero_candidato = input(f"Informe o voto para {
                                 cargo} (ou deixe em branco para voto em branco): ").strip()
        # Solicita ao usuário que informe o número do candidato para o cargo especificado.

        if numero_candidato == "":
            # Verifica se o número do candidato está em branco.
            confirmacao_branco = input(
                "Confirma o voto em branco (S ou N)? ").upper()
            # Pergunta ao usuário se confirma o voto em branco e converte a resposta para letras maiúsculas.
            if confirmacao_branco == 'S':
                return None
            # Se a confirmação for sim, o voto é registrado em branco.
            # Aqui pode ser o espaço para atacar a falta de registro de voto Branco/nulo
            else:
                print("Voto cancelado. Informe outro número.")
        elif numero_candidato.isdigit():
            numero_candidato = int(numero_candidato)
            # Verifica se o número do candidato é composto por digitos. Por segurança, converte para inteiro

            candidato_encontrado = next(
                (candidato for candidato in candidatos if candidato['numero'] == numero_candidato
                 and candidato not in candidatos_votados
                 and (uf_urna is None or candidato['estado'] == uf_urna)),
                None
            )
            # Utiliza uma expressão geradora para encontrar o candidato correspondente ao número informado.
            # Uma expressão geradora em Python é uma maneira concisa de criar iteradores. Ela utiliza a sintaxe de compreensão de listas, mas difere na forma como os valores são armazenados na memória.
            # Em vez de criar uma lista completa na memória, a expressão geradora gera os elementos um de cada vez, sob demanda, economizando assim recursos.

            if candidato_encontrado:
                print(f"Candidato: {candidato_encontrado['nome']} | Partido: {
                      candidato_encontrado['partido']}")
                # Exibe informações sobre o candidato encontrado.
                confirmacao = input("Confirma o voto (S ou N)? ").upper()
                # Confirma se é nele que vc quer votar
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
    # Inicializa um dicionário chamado 'resultados' para armazenar os resultados da apuração para cada cargo.
    resultados = {'Deputado Estadual': {'candidatos': {}, 'estado': None, 'votos': 0},
                  'Deputado Federal': {'candidatos': {}, 'estado': None, 'votos': 0},
                  'Senador': {'candidatos': {}, 'estado': None, 'votos': 0},
                  'Governador': {'candidatos': {}, 'estado': None, 'votos': 0},
                  'Presidente': {'candidatos': {}, 'estado': None, 'votos': 0}}
    # Cada cargo,é associado a um sub-dicionário contendo três informações cruciais.
    # Primeiramente, a chave 'candidatos' é reservada para um dicionário vazio, projetado para conter detalhes específicos sobre os candidatos que concorrem a esse cargo.
    # Em seguida, a chave 'estado' é inicialmente configurada como None, indicando que o estado vinculado a esse cargo ainda não foi especificado, podendo ser atualizado posteriormente.
    # Finalmente, a chave 'votos' é inicializada com o valor zero, representando o número acumulado de votos registrados para esse cargo.
    for voto in votos:
        # percorre cada voto na lista de votos. Para cada voto, são extraídas informações sobre o eleitor e seus votos nominais.
        eleitor = voto['eleitor']
        voto_nominal = voto['voto_nominal']
        for cargo, candidato in voto_nominal.items():
            # Dentro do loop externo, inicia um loop for interno que percorre cada cargo e candidato no voto nominal.
            # Verifica se o candidato não é nulo e, se não estiver no dicionário de candidatos para o cargo, adiciona as informações do candidato.
            if candidato:
                # Verifica se o candidato não é nulo.
                if candidato['numero'] not in resultados[cargo]['candidatos']:
                    # Se o número do candidato ainda não estiver no dicionário de candidatos para o cargo,
                    # adiciona as informações do candidato.
                    resultados[cargo]['candidatos'][candidato['numero']] = {
                        'nome': candidato['nome'],
                        'partido': candidato['partido'],
                        'votos': 0
                    }
                resultados[cargo]['estado'] = candidato['estado']
                # Atualiza as informações sobre o estado do cargo.

                resultados[cargo]['candidatos'][candidato['numero']
                                                ]['votos'] += 1
                # Incrementa o número de votos para o candidato específico.

                resultados[cargo]['votos'] += 1
                # Incrementa o número total de votos para o cargo.

    total_votos = len(votos)
    # Calcula o total de votos contando o número de elementos na lista de votos.

    return resultados, total_votos
    # Retorna o dicionário de resultados e o total de votos.


def mostrar_resultados(resultados, eleitores_aptos, total_votos, candidatos):
    # Imprime os cabeçalhos e informações gerais sobre a eleição
    print("\n==== Resultados ====")
    print(f"Eleitores Aptos: {eleitores_aptos}")
    print(f"Total de Votos Nominais: {total_votos}")

    print()
    # Esse print é só para pular uma linha mesmo

    for cargo, info in resultados[0].items():
        # Itera sobre cada cargo nos resultados
        percentual_cargo = (info['votos'] / total_votos) * \
            100 if total_votos > 0 else 0
        # Calcula o percentual de votos para o cargo
        print(f"Cargo: {cargo} | Estado: {info['estado']} | Votos: {
              info['votos']} ({percentual_cargo:.2f}%)")
        # Imprime informações sobre o cargo, incluindo o estado, votos e percentual

        # Encontrar o candidato eleito (com maior porcentagem)
        candidato_eleito = max(info['candidatos'].values(
        ), key=lambda x: x['votos'] / info['votos'] if info['votos'] > 0 else 0)
        # Aqui precisamos ir com calma Essa linha de código busca encontrar o candidato eleito para um cargo específico.
        # Para fazer isso, ela compara todos os candidatos que concorreram ao cargo, levando em conta a quantidade de votos que cada um recebeu em relação ao total de votos para aquele cargo.
        # A expressão x['votos'] / info['votos'] calcula essa proporção para cada candidato.
        # A função max é utilizada para encontrar o candidato que tem a maior proporção, ou seja, o candidato com a maior quantidade de votos em relação ao total de votos para o cargo.
        # A parte if info['votos'] > 0 else 0 garante que não haja divisão por zero, considerando zero se não houver votos no cargo.
        # Ao final, a variável candidato_eleito recebe o candidato que teve a maior proporção de votos, indicando assim o candidato eleito para o cargo.

        # Itera sobre cada candidato no cargo
        for numero, candidato_info in info['candidatos'].items():
            percentual_candidato = (
                candidato_info['votos'] / info['votos']) * 100 if info['votos'] > 0 else 0
            # Calcula o percentual de votos para o candidato
            resultado_formatado = f"Candidato: {candidato_info['nome']} | Partido: {
                candidato_info['partido']} | Votos: {candidato_info['votos']} ({percentual_candidato:.2f}%)"
            # Formata o resultado com informações sobre o candidato, partido, votos e percentual

            # Adicionar "Eleito" ao candidato com maior porcentagem
            if candidato_info == candidato_eleito:
                resultado_formatado += " - Eleito"

            print(resultado_formatado)

        print()


def mostrar_grafico(resultados):
    cargos = []
    votos = []
    nomes_eleitos = []
    porcentagens_eleitos = []

    # Inicializando as listas com dados de todos os cargos
    for cargo, info in resultados[0].items():
        cargos.append(cargo)
        candidato_eleito = max(info['candidatos'].values(),
                               key=lambda x: x['votos'] / info['votos'] if info['votos'] > 0 else 0)
        votos.append(candidato_eleito['votos'])
        nomes_eleitos.append(candidato_eleito['nome'])
        porcentagem_eleito = (candidato_eleito['votos'] / info['votos']) * 100
        porcentagens_eleitos.append(porcentagem_eleito)

    # Criando o gráfico de barras
    fig, ax = plt.subplots()
    bars = []

    for cargo, votos_eleito, nome_eleito, porcentagem_eleito in zip(cargos, votos, nomes_eleitos, porcentagens_eleitos):
        # Criando a barra ajustada
        bar = ax.bar(cargo, votos_eleito, color='blue')
        bars.append(bar)

        # Adicionando o nome do eleito e a porcentagem de votos sobre a barra
        height = bar[0].get_height()
        ax.text(bar[0].get_x() + bar[0].get_width() / 2, height,
                f'{nome_eleito}\n{porcentagem_eleito:.2f}%', ha='center', va='bottom', fontsize=8, fontweight='bold')

    # Configurando o eixo y para o total de votos nominais na eleição
    ax.set_ylim(0, max(votos)+1)  # Adicionando uma margem para melhor visualização

    plt.xlabel('Cargos')
    plt.ylabel('Número de Votos')
    plt.title('Resultado da Eleição')

    plt.show()


def salvar_votos_txt(votos, resultados, eleitores):
    nome_arquivo_txt = "votos_resultados.txt"

    with open(nome_arquivo_txt, 'w', encoding='utf-8') as arquivo_txt:
        # Escreve informações sobre os votos no arquivo de texto
        arquivo_txt.write("==== Resultados ====\n")
        arquivo_txt.write(f"Eleitores Aptos: {len(eleitores)}\n")
        arquivo_txt.write(f"Total de Votos Nominais: {len(votos)}\n\n")

        for cargo, info in resultados[0].items():
            percentual_cargo = (info['votos'] / len(votos)) * \
                100 if len(votos) > 0 else 0
            arquivo_txt.write(f"Cargo: {cargo} | Estado: {info['estado']} | Votos: {
                              info['votos']} ({percentual_cargo:.2f}%)\n")

            candidato_eleito = max(info['candidatos'].values(
            ), key=lambda x: x['votos'] / info['votos'] if info['votos'] > 0 else 0)

            for numero, candidato_info in info['candidatos'].items():
                percentual_candidato = (
                    candidato_info['votos'] / info['votos']) * 100 if info['votos'] > 0 else 0
                resultado_formatado = f"Candidato: {candidato_info['nome']} | Partido: {
                    candidato_info['partido']} | Votos: {candidato_info['votos']} ({percentual_candidato:.2f}%)"
                if candidato_info == candidato_eleito:
                    resultado_formatado += " - Eleito"
                arquivo_txt.write(f"{resultado_formatado}\n")

            arquivo_txt.write("\n")


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
        print("6 - Mostrar gráfico")
        print("7 - Votos txt")
        print("8 - Fechar programa")

        # Para obter a escolha do usuário:
        escolha = input("Escolha a opção (1 a 8): ")

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
            if resultados is not None:
                mostrar_grafico(resultados)
            else:
                print("Você precisa apurar os votos antes de mostrar o gráfico.")
        elif escolha == "7":
            salvar_votos_txt(votos, resultados, eleitores)
            print("Votos e resultados salvos com sucesso.")
        elif escolha == "8":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha de 1 a 8.")


def main():
    # Ela serve para chamar a função "menu_principal" e iniciar o programa
    menu_principal()
    # Aqui está sendo definindo o def munu_principal como a função principal do programa


if __name__ == "__main__":
    # chama a função principal
    main()
    # Aqui, basicamente estão verificando se o escript está sendo executado como programa principal, e ele faz isso
    # chamando a função principal.


# v5 - Urna funcional
