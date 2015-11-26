#'' e '' retorna verdadeiro
#' ' e '' retorna verdadeiro
#'a' e 'a' retorna verdadeiro
#'a' e 'a     ' retorna verdadeiro
#'ab' e 'ab' retorna verdadeiro
#'ba' e 'ab' retorna verdadeiro
#'b   a' e 'ab' retorna verdadeiro
#'ba' e 'a' retorna falso

def ehanagrama(palavra1 , palavra2):
    dicP1 = {}
    dicP2 = {}
    p1 = []
    p1 = list(palavra1.replace(' ','').lower())
    p2 = []
    p2 = list(palavra2.replace(' ', '').lower())
    lista = []
    lista2 = []
    if(len(p1) == len(p2)):
        for i in p1:
            if i in dicP1:
                temp = dicP1[i]
                dicP1[i] = temp+1
            else:
                dicP1[i] = [1]
        for i in p2:
            if i in dicP2:
                temp = dicP2[i]
                dicP2[i] = temp+1
            else:
                dicP2[i] = [1]
        for i in p1:
            if i in p2:
                lista.append(i)
            else:
                return False
        for i in p2:
            if i in p1:
                lista2.append(i)
        print(lista)
        print(lista2)
        if (len(lista) == len(lista2)) and (dicP1 == dicP2):
            return True

    return False
