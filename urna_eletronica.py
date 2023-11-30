# urna eletrônica criada para o desafio da disciplina de estrutura de dados

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
    """
    Verifica se o título de eleitor do eleitor está na lista de eleitores.

    Parâmetros:
    - eleitor_titulo (str): Título de eleitor do eleitor a ser verificado.
    - eleitores (list): Lista de eleitores.

    Retorno:
    - bool: True se o título de eleitor está na lista de eleitores, False caso contrário.
    """
    # Itera sobre a lista de eleitores
    for eleitor in eleitores:
        # Compara o título de eleitor fornecido com os títulos de eleitor na lista
        if eleitor_titulo == eleitor['titulo_eleitor']:
            return True  # Título de eleitor encontrado na lista de eleitores

    # Se o título de eleitor não for encontrado após percorrer toda a lista
    return False


def coleta_votos(candidatos, eleitores, votos):
    # Solicitar a UF da urna
    uf_urna = input("Informe a UF da urna: ").upper()

    # Solicitar título de eleitor do eleitor
    titulo_eleitor = input("Digite seu título de eleitor para votar: ")

    # Verificar se o título de eleitor do eleitor está na lista de eleitores
    if verificar_titulo_eleitor(titulo_eleitor, eleitores):
        eleitor_autenticado = True
        print("Eleitor autenticado. Pode prosseguir com a votação.")

        # Adicionar informações sobre o eleitor
        eleitor = [
            eleitor for eleitor in eleitores if eleitor['titulo_eleitor'] == titulo_eleitor][0]
        print("Eleitor:", eleitor['nome'])
        print(f"Estado: {uf_urna}")
    else:
        eleitor_autenticado = False
        print("Título de eleitor não encontrado na lista de eleitores...\n Retornando para o menu")
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


# def salvar_votos():

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
            apurar_votos(votos, candidatos)
        elif escolha == "5":
            mostrar_resultados(votos)
        elif escolha == "6":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha de 1 a 6.")


# Função para apurar os votos
# def apurar_votos()

# def mostrar_resultados()

# Função principal do programa
def main():
    # Chama a função menu_principal para iniciar o programa
    menu_principal()


if __name__ == "__main__":
    # Chama a função principal
    main()
