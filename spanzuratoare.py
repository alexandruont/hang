class indiciuCuvant:
    def __init__(self, index: int, hint: str, word: str):
        self.mIndex: int = index
        self.mWord = word
        self.mHint = hint

    def __str__(self):
        return f"Index: {self.mIndex}, Hint: {self.mHint}, Word: {self.mWord}\n"

    def __repr__(self):
        return f"Index: {self.mIndex}, Hint: {self.mHint}, Word: {self.mWord}\n"


cuvinteIncarcate = []


def loadIntoBuffer():
    file = open("cuvinte_de_verificat.txt", "r", encoding='utf-8')
    for line in file:
        elements = line.split(';')
        cuvinteIncarcate.append(indiciuCuvant(elements[0], elements[1], elements[2].rstrip()))
    file.close()


def indexLitereCunoscute(word_pattern: str) -> list[int]:
    return [i for i, char in enumerate(word_pattern) if char != '*']

cuvantAles: indiciuCuvant
incercariTotale = 0

def indiciu(letter):
    global incercariTotale
    incercariTotale += 1
    return [i for i, char in enumerate(cuvantAles.mWord) if char == letter]

def hangman(hint):
    askCounter = 0
    ultimaL = ''
    cuvintePosibile = [x.mWord for x in cuvinteIncarcate if len(x.mHint) == len(hint)]
    litereCunoscute = indexLitereCunoscute(hint)
    cuvintePosibile = [word for word in cuvintePosibile if all(word[index] == hint[index] for index in litereCunoscute)]
    while True:
        if len(cuvintePosibile) == 1:
            print("Cuvantul tau este:" + str(cuvintePosibile))
            print("Cuvantul a fost gasit in: " + str(askCounter) + " incercari")
            break
        else:
            ultimaL = cuvintePosibile[0][askCounter]
            litereGasite = indiciu(ultimaL)
            cuvintePosibile = [word for word in cuvintePosibile if all(word[index] == ultimaL for index in litereGasite)]
            askCounter += 1

if __name__ == "__main__":
    print("!HANGMAN!")
    
    loadIntoBuffer()
    print("Numarul de cuvinte: " + str(len(cuvinteIncarcate)))
            
    print("!!!Sa incepem!!!")
    for word in cuvinteIncarcate:
        cuvantAles = word
        hangman(cuvantAles.mHint)
    print("Cuvintele au fost gasite in: " + str(incercariTotale) + " incercari")