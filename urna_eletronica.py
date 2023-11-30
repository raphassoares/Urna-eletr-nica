# urna eletrônica criada para o desafio da disciplina de estrutura de dados
import pickle


def ler_candidatos():
    # Nome do arquivo
    # Nome do arquivo que contém os dados dos candidatos e que vamos utilizar
    nome_arquivo = "candidatos.txt"

    # Lista para armazenar os candidatos
    candidatos = []  # Inicialização de uma lista vazia para armazenar os dados dos candidatos

    # Abrir o arquivo em modo de leitura
    # "r" modo read, leitura - utf-8 indica a codificação de caracteres que deve ser usada ao ler ou escrever no arquivo.
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        # Ler todas as linhas do arquivo
        linhas = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena em uma lista

        # Iterar sobre as linhas do arquivo
        # Itera sobre cada linha do arquivo
        for linha_numero, linha in enumerate(linhas, start=1):
            try:
                # Dividir a linha nos elementos usando a vírgula como separador
                # Divide a linha em elementos usando ',' como separador
                dados = linha.strip().split(',')

                # Validar se há informações suficientes na linha
                if len(dados) != 5:  # Verifica se a linha contém exatamente 5 elementos
                    raise ValueError(
                        # Gera um erro se o formato não for válido
                        "Formato inválido na linha {}: {}".format(linha_numero, linha))

                # Extrair os dados e criar um dicionário
                nome, numero, partido, estado, genero = dados  # Desempacota os dados da linha
                candidato = {'nome': nome.strip(), 'numero': int(numero.strip()), 'partido': partido.strip(),
                             # Cria um dicionário com os dados do candidato
                             'estado': estado.strip(), 'genero': genero.strip()}

                # Adicionar o candidato à lista
                # Adiciona o dicionário à lista de candidatos
                candidatos.append(candidato)

            except Exception as e:
                # Tratar erros e imprimir informações sobre a linha com erro
                print("Erro na linha {}: {} - {}".format(linha_numero,
                                                         linha.strip(), str(e)))  # Imprime informações sobre o erro na linha

    # Retornar a lista de candidatos
    return candidatos  # Retorna a lista de candidatos após o processamento do arquivo


# Função para ler os dados dos eleitores a partir de um arquivo
def ler_eleitores():
    # Nome do arquivo
    nome_arquivo = "eleitores.txt"

    # Lista para armazenar os eleitores
    eleitores = []

    # Abrir o arquivo em modo de leitura
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        # Ler todas as linhas do arquivo
        linhas = arquivo.readlines()

        # Iterar sobre as linhas do arquivo
        for linha_numero, linha in enumerate(linhas, start=1):
            try:
                # Dividir a linha nos elementos usando a vírgula como separador
                dados = linha.strip().split(',')

                # Validar se há informações suficientes na linha
                if len(dados) != 5:
                    raise ValueError(
                        "Formato inválido na linha {}: {}".format(linha_numero, linha))

                # Extrair os dados e criar um dicionário
                nome, rg, titulo_eleitor, municipio, estado = dados
                eleitor = {'nome': nome.strip(), 'rg': rg.strip(), 'titulo_eleitor': titulo_eleitor.strip(),
                           'municipio': municipio.strip(), 'estado': estado.strip()}

                # Adicionar o eleitor à lista
                eleitores.append(eleitor)

            except Exception as e:
                # Tratar erros e imprimir informações sobre a linha com erro
                print("Erro na linha {}: {} - {}".format(linha_numero,
                                                         linha.strip(), str(e)))

    # Retornar a lista de eleitores
    return eleitores


def verificar_titulo_eleitor(eleitor_titulo, eleitores):

    # Itera sobre a lista de eleitores
    for eleitor in eleitores:
        # Compara o título de eleitor fornecido com os títulos de eleitor na lista
        if eleitor_titulo == eleitor['titulo_eleitor']:
            return True  # Título de eleitor encontrado na lista de eleitores

    # Se o título de eleitor não for encontrado após percorrer toda a lista
    return False


def coleta_votos(candidatos, eleitores, votos):
    op = "S"
    while op == "S":
        # ele criou uma variavel op...essa variavel, toda vez que ela for "S", ela recomeça a votação sem que eu precise voltar no menu

        # Solicitar título de eleitor do eleitor
        titulo_eleitor = input("Digite seu título de eleitor para votar: ")

        # Chama a função verificar_titulo_eleitor para ver se o título digitado está na lista
        if verificar_titulo_eleitor(titulo_eleitor, eleitores):
            eleitor_autenticado = True
            print("Eleitor autenticado. Pode prosseguir com a votação.")

            # se estiver na lista, devolve que foi autenticado e informa o nome e o estado do eleitor
            eleitor = [
                eleitor for eleitor in eleitores if eleitor['titulo_eleitor'] == titulo_eleitor][0]
            print("Eleitor:", eleitor['nome'])
            print("Estado:", eleitor['estado'])
        else:
            eleitor_autenticado = False
            print(
                "Título de eleitor não encontrado na lista de eleitores...\n Retornando para o menu")
            return

        # Lista para armazenar candidatos já votados
        candidatos_votados = []

        # Coleta de votos para Deputado Estadual
        voto_dep_estadual = coletar_voto(
            "Deputado Estadual", candidatos, candidatos_votados)

        # Adiciona o candidato votado à lista de candidatos votados
        candidatos_votados.append(voto_dep_estadual)

        # Coleta de votos para Deputado Federal
        voto_dep_federal = coletar_voto(
            "Deputado Federal", candidatos, candidatos_votados)

        # Adiciona o candidato votado à lista de candidatos votados
        candidatos_votados.append(voto_dep_federal)

        # Coleta de votos para Senador
        voto_senador = coletar_voto("Senador", candidatos, candidatos_votados)

        # Adiciona o candidato votado à lista de candidatos votados
        candidatos_votados.append(voto_senador)

        # Coleta de votos para Governador
        voto_governador = coletar_voto(
            "Governador", candidatos, candidatos_votados)

        # Adiciona o candidato votado à lista de candidatos votados
        candidatos_votados.append(voto_governador)

        # Coleta de votos para Presidente
        voto_presidente = coletar_voto(
            "Presidente", candidatos, candidatos_votados)

        # Adiciona o candidato votado à lista de candidatos votados
        candidatos_votados.append(voto_presidente)

        # Adiciona os votos à lista de votos
        votos = {}
        votos["Deputado Estadual"] = voto_dep_estadual
        votos["Deputado Estadual"] = voto_dep_estadual
        votos["Deputado Federal"] = voto_dep_federal
        votos["Senador"] = voto_senador
        votos["Governador"] = voto_governador
        votos["Presidente"] = voto_presidente

        print(votos)

        # Salvar votos em um arquivo binário
        salvar_votos(votos)
        op = input("Deseja continuar a votação? S/N")
# BASICAMENTE O rafael sugeriu uma correção em votos, pois antes estava como dicionário com append e isso nao existe.
# criou-se um dicionario votos, e esse dicionáro passou a salvar individualmente cada voto de cada eleitor

# o professor, corrigiu a questão da repetição. O codigo antes era executado uma vez a votação e depois voltava para o menu, agora ele criou uma repetição enquanto eu quiser pode continuar votando


def coletar_voto(genero, candidatos, candidatos_votados):
    while True:
        numero_candidato = input(f"Informe o voto para {genero}: ").strip()

        # Verificar se o número do candidato é válido e não foi votado anteriormente
        candidato_encontrado = next(
            (candidato for candidato in candidatos if candidato['numero'] == int(numero_candidato)
             and candidato not in candidatos_votados), None)

        if candidato_encontrado:
            print(f"Candidato: {candidato_encontrado['nome']} | Partido: {
                  candidato_encontrado['partido']}")
            confirmacao = input("Confirma o voto (S ou N)? ").upper()

            if confirmacao == 'S':
                return candidato_encontrado
            else:
                print("Voto cancelado. Informe outro número.")
        else:
            print(f"Número de candidato inválido para {
                  genero}. Tente novamente.")


def salvar_votos(votos):
    # Nome do arquivo binário
    nome_arquivo_binario = "votos.bin"

    # Abrir o arquivo binário em modo de escrita (wb) usando a codificação UTF-8
    with open(nome_arquivo_binario, 'wb') as arquivo_binario:
        # Usa o módulo pickle para serializar e salvar os votos no arquivo binário
        pickle.dump(votos, arquivo_binario, protocol=pickle.HIGHEST_PROTOCOL)


def carregar_votos():
    # Nome do arquivo binário
    nome_arquivo_binario = "votos.bin"

    try:
        # Abrir o arquivo binário em modo de leitura (rb) usando a codificação UTF-8
        with open(nome_arquivo_binario, 'rb') as arquivo_binario:
            # Usa o módulo pickle para desserializar e carregar os votos do arquivo binário
            votos = pickle.load(arquivo_binario)
            return votos
    except FileNotFoundError:
        # Se o arquivo não for encontrado, retorna uma lista vazia
        return []


def menu_principal():
    # Inicialização de variáveis
    candidatos = []
    eleitores = []
    votos = []

    while True:
        # Exibir opções do menu
        print("\n===== Menu Principal =====")
        print("1 - Ler arquivo de candidatos")
        print("2 - Ler arquivo de eleitores")
        print("3 - Iniciar votação")
        print("4 - Apurar votos")
        print("5 - Mostrar resultados")
        print("6 - Fechar programa")

        # Obter a escolha do usuário
        escolha = input("Escolha a opção (1 a 6): ")

        # Realizar ações conforme a escolha do usuário
        if escolha == "1":
            candidatos = ler_candidatos()
            print("Arquivo de candidatos lido com sucesso.")
        elif escolha == "2":
            eleitores = ler_eleitores()
            print("Arquivo de eleitores lido com sucesso.")
        elif escolha == "3":
            coleta_votos(candidatos, eleitores, votos)
        elif escolha == "4":
            carregar_votos(votos, candidatos)
        elif escolha == "5":
            mostrar_resultados(votos)
        elif escolha == "6":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha de 1 a 6.")


# def apurar_votos()


# def mostrar_resultados()


def main():
    # Chama a função menu_principal para iniciar o programa
    menu_principal()


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    # Chama a função principal
    main()
