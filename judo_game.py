import time

class Lutador:
    def __init__(self, nome, peso, golpes, contra_golpes, golpe_preferido, segundo_golpe, nacionalidade):
        self.nome = nome
        self.peso = peso
        self.golpes = set(golpes)
        self.contra_golpes = dict(contra_golpes)
        self.golpe_preferido = golpe_preferido
        self.segundo_golpe = segundo_golpe
        self.tai_sabaki = "Tai-Sabaki"
        self.nacionalidade = nacionalidade
        self.contador_ippone = 0
        self.contador_wazari = 0
        self.contador_shido = 0

possiveis_golpes = ["Uchi-Mata", "Sumi-Gaeshi", "Tomoe-Nage", "Kata-Guruma", "Seoi-Nage", "Sode-Tsuri-Komi-Goshi", "Ouchi-Gari", 
                    "Harai-Goshi", "O-Soto-Gari", "Kouchi-Gari", "Morote-Seoi-Nage", "O-Soto-Otoshi", "Sassae-Tsuri-Komi-Ashi", 
                    "De-Ashi-harai", "Tai-Otoshi", "O-goshi", "Koshi-guruma", "Tsuri-Komi-Goshi", "Uki-goshi", "Yoko-Tomoe-nage", 
                    "Harai-Tsuri-Komi-Ashi", "O-Soto-Guruma"]
possiveis_contra_golpes = ["Uchi-Mata-Sukashi", "Tani-Otoshi", "O-Soto-Gaeshi", "Uchi-mata-sukashi", "Uchi-mata", "Ko-soto-gari", "Hiza-guruma", 
                           "Ko-uchi-gari", "Uki-goshi", "O-soto-gari", "Sumi-gaeshi", "Uki-Otoshi", "Osoto-otoshi", "Ouchi-Gaeshi"]

dicionario_golpes_contra_golpes = {
    "Uchi-Mata": "Uchi-Mata-Sukashi",
    "Seoi-Nage": "Tani-Otoshi",
    "O-Soto-Gari": "O-Soto-Gaeshi",
    "Kouchi-Gari": "Uchi-mata",
    "Morote-Seoi-Nage": "Uchi-mata-sukashi",
    "O-Soto-Otoshi": "Ko-soto-gari",
    "Sassae-Tsuri-Komi-Ashi": "Hiza-guruma",
    "De-Ashi-Harai": "Ko-uchi-gari",
    "Tai-Otoshi": "Hiza-guruma",
    "O-Goshi": "Uki-goshi",
    "Koshi-Guruma": "Uki-goshi",
    "Tsuri-Komi-Goshi": "Uki-goshi",
    "Uki-Goshi": "O-soto-gari",
    "Yoko-Tomoe-Nage": "Sumi-gaeshi",
    "Harai-Goshi": "Uki-Otoshi",  
    "Harai-Tsuri-Komi-Ashi": "Uchi-mata",
    "O-Soto-Guruma": "Osoto-otoshi",
    "Kata-Guruma": "Tani-Otoshi",
    "Ouchi-Gari" : "Ouchi-Gaeshi"
}

class Placar:
    def __init__(self):
        self.contador_ippone_jogador1 = 0
        self.contador_wazari_jogador1 = 0
        self.contador_shido_jogador1 = 0
        self.contador_ippone_jogador2 = 0
        self.contador_wazari_jogador2 = 0
        self.contador_shido_jogador2 = 0

    def atualizar_placar_jogador(self, jogador, ippone, wazari, shido):
        if ippone:
            jogador.contador_ippone += 1
        elif wazari:
            jogador.contador_wazari += 1
        elif shido:
            jogador.contador_shido += 1

    def exibir_placar(self, jogador1, jogador2):
        print("Placar:")
        print(f"{jogador1.nome} - IPPON: {jogador1.contador_ippone}, WAZARI: {jogador1.contador_wazari}, SHIDO: {jogador1.contador_shido}")
        print(f"{jogador2.nome} - IPPON: {jogador2.contador_ippone}, WAZARI: {jogador2.contador_wazari}, SHIDO: {jogador2.contador_shido}")

class JogoJudô:
    def __init__(self):
        self.lutadores = [
            Lutador(nome="Flavio Canto", peso=81, golpes=("De-Ashi-Harai", "Sumi-Gaeshi", "Tomoe-Nage"),
                    contra_golpes={"Uchi-Mata": "Uchi-Mata-Sukashi", 
                                   "Seoi-Nage": "Tani-Otoshi", 
                                   "De-Ashi-Harai": "Ko-uchi-gari"},
                    golpe_preferido="Uchi-Mata", segundo_golpe="Seoi-Nage", nacionalidade="BRA"),
            Lutador(nome="Leando Guilheiro", peso=81, golpes=("Kata-Guruma", "Tai-Otoshi", "Sode-TsuriKomi-Goshi"),
                    contra_golpes={"O-Soto-Gari": "O-Soto-Gaeshi", 
                                   "Seoi-Nage": "Tani-Otoshi", 
                                   "Tai-Otoshi": "Hiza-guruma"},
                    golpe_preferido="Seoi-Nage", segundo_golpe="O-Soto-Gari", nacionalidade="BRA"),
            Lutador(nome="Rogerio Sampaio", peso=81, golpes=("Ouchi-Gari", "Harai-Goshi", "O-Soto-Guruma"),
                    contra_golpes={"O-Soto-Gari": "O-Soto-Gaeshi", 
                                   "Ouchi-Gari" : "Ouchi-Gaeshi", 
                                   "Uchi-Mata": "Uchi-Mata-Sukashi"},
                    golpe_preferido="O-Soto-Gari", segundo_golpe="Uchi-Mata", nacionalidade="BRA"),
            Lutador(nome="Teddy Riner", peso= '+100', golpes=("Sassae-Tsuri-Komi-Ashi", "O-Soto-Otoshi", "Tai-Otoshi"),
                    contra_golpes={"Harai-Goshi": "Uki-Otoshi", 
                                   "O-Soto-Guruma": "Osoto-otoshi", 
                                   "Sassae-Tsuri-Komi-Ashi": "Hiza-guruma"},
                    golpe_preferido="Harai-Goshi", segundo_golpe="O-Soto-Guruma", nacionalidade="FRA"),
            Lutador(nome="Tadahiro Nomura", peso=60, golpes=("Morote-Seoi-Nage", "Tsuri-Komi-Goshi", "Koshi-Guruma"),
                    contra_golpes={"Tai-Otoshi": "Hiza-guruma", 
                                   "Kata-Guruma": "Tani-Otoshi", 
                                   "Morote-Seoi-Nage": "Uchi-mata-sukashi"},
                    golpe_preferido="Kata-Guruma", segundo_golpe="Tai-Otoshi", nacionalidade="JAP"),
            Lutador(nome="Shohei Ono", peso=73, golpes=("Koshi-Guruma", "Tomoe-nage", "Sumi-gaeshi"),
                    contra_golpes={"Harai-Goshi": "Uki-Otoshi", 
                                   "Yoko-Tomoe-Nage": "Sumi-gaeshi", 
                                   "Koshi-Guruma": "Uki-goshi"},
                    golpe_preferido="Harai-Goshi", segundo_golpe="Yoko-Tomoe-nage", nacionalidade="JAP"),
            Lutador(nome="Ilias Iliadis", peso=90, golpes=("O-Goshi", "Kouchi-Gari", "Harai-Tsuri-Komi-Ashi"),
                    contra_golpes={"Koshi-Guruma": "Uki-goshi", 
                                   "Tsuri-Komi-Goshi": "Uki-goshi", 
                                   "Harai-Tsuri-Komi-Ashi": "Uchi-mata"},
                    golpe_preferido="Koshi-guruma", segundo_golpe="Tsuri-Komi-Goshi", nacionalidade="GRE"),
            Lutador(nome="Kim Jae-Bum", peso=81, golpes=("Uki-Goshi", "Kata-Guruma", "Hiza-guruma"),
                    contra_golpes={"Uki-Goshi": "O-soto-gari", 
                                   "Ouchi-Gari" : "Ouchi-Gaeshi", 
                                   "De-Ashi-Harai": "Ko-uchi-gari"},
                    golpe_preferido="De-Ashi-harai", segundo_golpe="Ouchi-Gari", nacionalidade="KOR"),
            Lutador(nome="Daniel Cargnin", peso=66, golpes=("O-Soto-Gari", "Koshi-Guruma", "Kata-Guruma"),
                    contra_golpes={"Morote-Seoi-Nage": "Uchi-mata-sukashi", 
                                   "Seoi-Nage": "Tani-Otoshi", 
                                   "O-Soto-Gari": "O-Soto-Gaeshi"},
                    golpe_preferido="Seoi-Nage", segundo_golpe="Morote-Seoi-Nage", nacionalidade="BRA"),
            Lutador(nome="Rafael Silva 'Baby'", peso= '+100', golpes=("O-Soto-Otoshi", "Uchi-Mata", "O-Soto-Gari"),
                    contra_golpes={"De-Ashi-Harai": "Ko-uchi-gari", 
                                   "Sassae-Tsuri-Komi-Ashi": "Hiza-guruma", 
                                   "O-Soto-Gari": "O-Soto-Gaeshi"},
                    golpe_preferido="Sassae-Tsuri-Komi-Ashi", segundo_golpe="De-Ashi-hara", nacionalidade="BRA")
        ]

        self.pontuacao_jogador1 = 0
        self.pontuacao_jogador2 = 0
        self.wazari_jogador1 = 0
        self.wazari_jogador2 = 0
        self.shido_jogador1 = 0
        self.shido_jogador2 = 0
        self.placar = Placar()

    def apresentacao(self):
        print("|--------------------------------------------------------------------|\n")
        print("| Bem-vindo à Final do Campeonato Mundial 2024 de Judô em Python!    |\n")
        print("|--------------------------------------------------------------------|\n")

    def exibir_golpes(self, jogador):
        print(f"\nGolpes de {jogador.nome}:\n")
        for i, golpe in enumerate(list(jogador.golpes) + [jogador.tai_sabaki, jogador.golpe_preferido, jogador.segundo_golpe], start=1):

            print(f"{i}. {golpe}")
            time.sleep(0.5)

    def escolher_lutador(self, numero_jogador):
        print(f"Escolha seu lutador de preferência, Jogador {numero_jogador}:\n")
        time.sleep(1)
        for i, lutador in enumerate(self.lutadores, start=1):
            print(f"{i}. {lutador.nome}")
            time.sleep(1)
        try:
            escolha = int(input(f"\nJogador {numero_jogador}, escolha seu lutador (1 a 10): ")) - 1
            
            if 0 <= escolha < len(self.lutadores):
                lutador_escolhido = self.lutadores.pop(escolha)

                print("\nInformações do Lutador Escolhido:")
                print(f"Nome: {lutador_escolhido.nome}")
                print(f"Peso: {lutador_escolhido.peso}")
                print(f"Golpe Preferido: {lutador_escolhido.golpe_preferido}")
                print(f"Nacionalidade: {lutador_escolhido.nacionalidade}")

                return lutador_escolhido
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Insira um número válido.")

    def apresentar_luta(self, jogador1, jogador2):  # Remove 'self' from the parameter list
        print(f"\n{str(jogador1.nome)} vs {str(jogador2.nome)}!\n")
        time.sleep(1)
        print("Os corajosos lutadores estão adentrando o Shiai-Jo! O combate está prestes a começar...\n")
        time.sleep(1)
        print("Os lutadores respeitosamente se cumprimentam...\n")
        time.sleep(1)
        print("HAJIME!!!\n")
        time.sleep(1)
        print(f"{jogador1.nome}: Ossu, {jogador2.nome}-san! Que tenhamos uma luta justa e emocionante!\n")
        time.sleep(1)
        print(f"{jogador2.nome}: Ossu, {jogador1.nome}-san! Vamos fazer uma grande luta, que vença o melhor!\n")
        time.sleep(2)


    def escolher_movimento(self, jogador):
        print(f"\n{str(jogador.nome)}, é sua vez de atacar!\n")
        time.sleep(1)
        print(f"{str(jogador.nome)}, escolha seu movimento!\n")
        time.sleep(1)
        self.exibir_golpes(jogador)
        escolha = int(input("\nO que você vai fazer? (1-4): ")) - 1
        movimentos = list(jogador.contra_golpes.keys()) + [jogador.golpes, jogador.golpe_preferido, jogador.segundo_golpe, jogador.tai_sabaki]
        return movimentos[escolha]

    def avaliar_resposta(self, jogador1, jogador2, movimento):
        wazari = False
        ippone = False
        shido = False

        print(f"\n{jogador2.nome}, é sua vez de contra-atacar!\n")
        time.sleep(1)
        print(f"\n{jogador2.nome}, seja rápido! Escolha um movimento em resposta:\n")
        time.sleep(1)

        movimentos_disponiveis = list(jogador2.contra_golpes.values()) + [jogador2.tai_sabaki]
        for i, contra_golpe in enumerate(movimentos_disponiveis, start=1):
            print(f"{i}. {contra_golpe}")
            time.sleep(1)

        escolha = int(input("\nO que você vai fazer? (1-4): ")) - 1

        resposta = movimentos_disponiveis[escolha] if 0 <= escolha < len(movimentos_disponiveis) else jogador2.tai_sabaki
        print(f"\n{jogador2.nome} desviou com um incrível {resposta}!\n")
        time.sleep(2)

        if (str(movimento)) == jogador1.golpe_preferido:
            if resposta == jogador2.contra_golpes.get(jogador1.golpe_preferido):
                wazari = True
                self.placar.atualizar_placar_jogador(jogador1, False, wazari, False)
                print(f"{jogador1.nome} aplicou um WAZARI! {jogador2.nome} sofreu um golpe decisivo e precisará se esforçar para virar o resultado!\n")
                time.sleep(1)
            elif resposta == jogador2.tai_sabaki:
                ippone = True
                self.placar.atualizar_placar_jogador(jogador1, ippone, False, False)
                print(f"{jogador1.nome} aplicou um belíssimo IPPON! {jogador2.nome} caiu de costas no chão! Sem chance de defesa!!!\n")
                time.sleep(1)

        elif (str(movimento)) == jogador1.segundo_golpe:
            if resposta == jogador2.contra_golpes.get(jogador1.segundo_golpe):
                wazari = True
                self.placar.atualizar_placar_jogador(jogador1, False, wazari, False)
                print(f"{jogador1.nome} aplicou um WAZARI! {jogador2.nome} sofreu um golpe decisivo e precisará se esforçar para virar o resultado!\n")
                time.sleep(1)
            elif resposta == jogador2.tai_sabaki:
                wazari = True
                self.placar.atualizar_placar_jogador(jogador1, False, wazari, False)
                print(f"{jogador1.nome} aplicou um WAZARI! {jogador2.nome} sofreu um golpe decisivo e precisará se esforçar para virar o resultado!\n")
                time.sleep(1)

        elif (str(movimento)) not in {jogador1.golpe_preferido, jogador1.segundo_golpe}:
            if resposta == jogador2.contra_golpes.get(str(movimento)):
                wazari = True
                self.placar.atualizar_placar_jogador(jogador2, False, wazari, False)
                print(f"{jogador2.nome} aplicou um WAZARI! {jogador1.nome} sofreu um golpe decisivo e precisará se esforçar para virar o resultado!\n")
                time.sleep(1)

        elif (str(movimento)) == jogador2.tai_sabaki:
            if resposta == jogador1.contra_golpes.get(jogador2.tai_sabaki):
                wazari = True
                self.placar.atualizar_placar_jogador(jogador2, False, wazari, False)
                print(f"{jogador2.nome} aplicou um WAZARI! {jogador1.nome} sofreu um golpe decisivo e precisará se esforçar para virar o resultado!\n")
                time.sleep(1)

        else:
            shido = True
            self.placar.atualizar_placar_jogador(jogador2, False, False, shido)
            print(f"{jogador2.nome} cometeu um SHIDO! {jogador1.nome} ganha uma penalidade!\n")
            time.sleep(1)

            #############################################

        if (str(movimento)) == jogador1.golpe_preferido and resposta == jogador1.contra_golpes.get(str(movimento)):
                wazari = True
                self.placar.atualizar_placar_jogador(jogador1, False, wazari, False)
                print(f"{jogador1.nome} aplicou um belíssimo WAZARI! {jogador2.nome} caiu de lado no chão! Por pouco não caiu de costas!!!\n")


        if (str(movimento)) == jogador2.golpe_preferido and resposta == jogador2.contra_golpes.get(str(movimento)):
                wazari = True
                self.placar.atualizar_placar_jogador(jogador2, False, wazari, False)
                print(f"{jogador2.nome} aplicou um belíssimo WAZARI! {jogador1.nome} caiu de lado no chão! Por pouco não caiu de costas!!!\n")
        
        # elif (str(movimento)) == jogador1.golpe_preferido or (str(movimento)) == jogador1.segundo_golpe and resposta == jogador2.tai_sabaki:
            # ippone = True
            # self.placar.atualizar_placar_jogador(jogador1, ippone, False, False)
            # print(f"{jogador1.nome} aplicou um belíssimo IPPON! {jogador2.nome} caiu sem defesa no chão!\n")

        # elif (str(movimento)) == jogador2.golpe_preferido or (str(movimento)) == jogador2.segundo_golpe and resposta == jogador1.tai_sabaki:
            # ippone = True
            # self.placar.atualizar_placar_jogador(jogador2, ippone, False, False)
            # print(f"{jogador2.nome} aplicou um belíssimo IPPON! {jogador1.nome} caiu sem defesa no chão!\n")

        elif (str(movimento)) == jogador1.tai_sabaki and resposta != jogador1.contra_golpes.get(movimento):
            self.placar.atualizar_placar_jogador(jogador2, False, False, False)
            self.placar.atualizar_placar_jogador(jogador1, False, False, False)
            print(f"{jogador2.nome} se esquivou habilmente! {jogador1.nome} mal pôde enxergar seus movimentos!\n")
        
        elif (str(movimento)) == jogador1.tai_sabaki and resposta == jogador2.tai_sabaki:
            self.placar.atualizar_placar_jogador(jogador2, False, False, False)
            self.placar.atualizar_placar_jogador(jogador1, False, False, False)
            print(f"{jogador2.nome} se movimenta como um raio! {jogador1.nome} mal pôde enxergar seus movimentos!\n")
            time.sleep(1)
            print(f"{jogador1.nome} Acelera o ritmo!\n")
            time.sleep(1)
            print(f"{jogador1.nome} A luta pega fogo e a torcida vai a loucura!!!\n")

        # elif str(movimento_jogador1) not in jogador1.golpes:
            # self.placar.atualizar_placar_jogador(jogador1, False, False, shido)
            # print(f"SHIDO para {jogador1.nome}")
        # elif str(movimento_jogador2) not in jogador2.golpes:
            # self.placar.atualizar_placar_jogador(jogador2, False, False, shido)
            # print(f"SHIDO para {jogador2.nome}")

        return wazari, ippone, shido


    def executar_jogo(self):
        self.apresentacao()

        jogador1 = self.escolher_lutador(1)
        jogador2 = self.escolher_lutador(2)

        self.apresentar_luta(jogador1, jogador2)

        while True:
            movimento_jogador1 = self.escolher_movimento(jogador1)
            if movimento_jogador1 is None:
                self.shido_jogador1 += 1
                print(f"\n{self.shido_jogador1} falta(s) para {jogador1.nome}! Vantagem para {jogador2.nome}!\n")
                if self.shido_jogador1 == 3:
                    print(f"\nFim da partida! {jogador1.nome} desclassificado por Hansoku-Make!\n")
                    self.encerrar_partida(jogador1, jogador2)
                    break
            else:
                wazari_jogador1, ippone_jogador1, shido_jogador1 = self.avaliar_resposta(jogador1, jogador2, movimento_jogador1)

                if ippone_jogador1:
                    self.pontuacao_jogador1 += 100
                    print(f"\nFim da partida! Parabéns, {jogador1.nome}! Você venceu por IPPON e é o novo Campeão Mundial de Judô em Python!\n")
                    self.encerrar_partida(jogador1, jogador2)
                    break
                elif wazari_jogador1:
                    self.pontuacao_jogador1 += 10
                    self.wazari_jogador1 += 1
                    if self.wazari_jogador1 == 2:
                        print(f"\nFim da partida! Parabéns, {jogador1.nome}! Você venceu por dois WAZARIs e é o novo Campeão Mundial de Judô em Python!\n")
                        self.encerrar_partida(jogador1, jogador2)
                        break
                    else:
                        print(f"\n{self.wazari_jogador1} WAZARI(s) para {jogador1.nome}! Continue atacando!\n")
                else:
                    print("\nA disputa está pegando fogo! Os dois lutadores estão com tudo! E o combate continua...\n")
                    time.sleep(1)

            movimento_jogador2 = self.escolher_movimento(jogador2)
            if movimento_jogador2 is None:
                self.shido_jogador2 += 1
                print(f"\n{self.shido_jogador2} falta(s) para {jogador2.nome}! Vantagem para {jogador1.nome}!\n")
                if self.shido_jogador2 == 3:
                    print(f"\nFim da partida! {jogador2.nome} desclassificado por Hansoku-Make!\n")
                    self.encerrar_partida(jogador1, jogador2)
                    break
            else:
                wazari_jogador2, ippone_jogador2, shido_jogador2 = self.avaliar_resposta(jogador2, jogador1, movimento_jogador2)

                if ippone_jogador2:
                    self.pontuacao_jogador2 += 100
                    print(f"\nFim da partida! Parabéns, {jogador2.nome}! Você venceu por IPPON e é o novo Campeão Mundial de Judô em Python!\n")
                    self.encerrar_partida(jogador1, jogador2)
                    break
                elif wazari_jogador2:
                    self.pontuacao_jogador2 += 10
                    self.wazari_jogador2 += 1
                    if self.wazari_jogador2 == 2:
                        print(f"\nFim da partida! Parabéns, {jogador2.nome}! Você venceu por dois WAZARIs e é o novo Campeão Mundial de Judô em Python!\n")
                        self.encerrar_partida(jogador1, jogador2)
                        break
                    else:
                        print(f"\n{self.wazari_jogador2} WAZARI(s) para {jogador2.nome}! Continue atacando!\n")
                else:
                    print("\nA luta continua...\n")
                    time.sleep(1)

            self.placar.exibir_placar(jogador1, jogador2)
            time.sleep(1)

    def encerrar_partida(self, jogador1, jogador2):
        print("\nOs lutadores se cumprimentam em respeito ao final do combate...\n")
        time.sleep(1)
        print("\nDōmo arigatōgozaimasu...\n")
        time.sleep(1)
        print("\nResultado Final:")
        print(f"{jogador1.nome}: {self.pontuacao_jogador1} pontos")
        print(f"{jogador2.nome}: {self.pontuacao_jogador2} pontos")
        time.sleep(2)
        print("\nPlacar Final do combate:")
        self.placar.exibir_placar(jogador1, jogador2)
        time.sleep(2)
        print("\nObrigado por participar do Campeonato Mundial 2024 de Judô em Python!\n")
        time.sleep(1)
        print("\nNos vemos na próxima edição do Incrível Campeonato Mundial de Judô em Python!!!\n")

if __name__ == "__main__":
    jogo = JogoJudô()
    jogo.executar_jogo()

