from random import randint

class Forca:

    def __init__(self):
        self.status = 0
        self.letrasErradas = []
        self.letrasCorretas = []
        self.palavrasSecretas = [
            "maca",
            "limao",
            "uva",
            "abacaxi",
            "pera",
            "banana"
        ]

        indexPalavra = randint(0, 5)
        self.palavraAtual = self.palavrasSecretas[indexPalavra]

    def getForcaStatus(self):
        switch = [
            '''
            +-----+
            |     |
            |     |
            |
            |
            |
            |
            ===========
            ''',

            '''
            +-----+
            |     |
            |     |
            |     0
            |
            |
            |
            ===========
            ''',

            '''
            +-----+
            |     |
            |     |
            |     0
            |     |
            |
            |
            ===========
            ''',

            r'''
            +-----+
            |     |
            |     |
            |     0
            |    /|
            |
            |
            ===========
            ''',

            r'''
            +-----+
            |     |
            |     |
            |     0
            |    /|\
            |
            |
            ===========
            ''',

            r'''
            +-----+
            |     |
            |     |
            |     0
            |    /|\
            |    /
            |
            ===========
            ''',

            r'''
            +-----+
            |     |
            |     |
            |     0
            |    /|\
            |    / \
            |
            ===========
            ''',
        ]
        return switch[self.status]

    def findOccurrences(self, string, char):
        return [i for i, letter in enumerate(string) if letter == char]

    def playGame(self):
        qntLetras = len(self.palavraAtual)
        letrasPalavraSecreta = []
        for i in range(qntLetras):
            letrasPalavraSecreta.append("_")
        
        while(self.status < 6):
            if(not "_" in letrasPalavraSecreta):
                break

            print("======== TEMA: FRUTAS ========")
            print("Letras erradas: " + "-".join(self.letrasErradas))
            print(self.getForcaStatus())
            print("Palavra: " + " ".join(letrasPalavraSecreta))
            
            letraDigitada = input("Digite uma letra: ")
            arrIndexLetra = self.findOccurrences(self.palavraAtual, letraDigitada)

            if(len(arrIndexLetra) > 0):
                print("ACERTOU!")
                for indexLetra in arrIndexLetra:                                        
                    letrasPalavraSecreta[indexLetra] = letraDigitada                    
            else:
                print("ERROU :(")
                self.letrasErradas.append(letraDigitada)
                self.status += 1

        print(self.getForcaStatus())
        print("Palavra: " + " ".join(letrasPalavraSecreta))

        if(self.status == 6):
            print("RESULTADO: PERDEU!!! A palavra era {}. Tente novamente...".format(self.palavraAtual))
        else:
            print("RESULTADO: VENCEU!!! A palavra era {}.".format(self.palavraAtual))