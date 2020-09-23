import itertools
from string import punctuation

filename = 'Article2.txt'

#fonction auxiliaire pour enlever la ponctuation d'une string
def noponctuation(s):
    return ''.join(c for c in s if c not in punctuation)

#fonction map : pour un texte donné, renvoyer une liste de n-uplets (word,1) des mots du texte
#Un décompte des mots du texte sera ensuite réalisé avec la fonction reduce
#L'idée est d'effectuer le décompte des mots ligne à ligne, puis d'additionner le tout.

def map(input_value):
    input_value=noponctuation(input_value)                         #on enlève la ponctuation pour faire plus simple
    return ([(word,1) for word in (input_value.lower()).split()])  #on enlève les majuscules


#fonction réduce : prend en argument un n-uplet (word1,w11),(word1,w12),...(wordn,wn1), (wordn,wn2)
# .. et renvoie un n-uplet (word1, w11+w12+..))...(wordn,wn1+wn2+...)
#Cette fonction réduce est capable de faire plus qu'une fonction additionnant uniquement les (word1,1)...(wordn,1)
#renvoyés par la fonction map ci dessus
#Elle est utilisable pour sommer le nombre d'occurences sur une ligne
#Et réutilisable pour sommer ensuite les occurences ligne par ligne
#On fait 2 calculs successifs via cette fonction : occurence d'un mot sur une ligne,
# et occurence sur une série de lignes
def reduce(lista):
    lenghth=len(lista)
    wordscounted=[]  #liste des mots déja comptés [word1,word2,..]
    sum=[]           #liste des mots et de leur décompte [(word1,w11+w12+...),(word2,w21+w22+)...(wordn,wn1+wn2)]

    if lista==[]:
        pass   #si on rentre une liste vide, reduce ne renvoie rien
    else:

      for k in range(0,lenghth):
        current_word=(lista[k])[0]                 #on commence par la gauche de la liste à compter
        current_count=((lista[k])[1]-1)            #on initialise le décompte
        if current_word in wordscounted:
            pass  #si on a déjà compté ce mot, on ne le recompte pas
        else:
            wordscounted.append(current_word)      #on ajoute le mot à la liste des mots déjà comptés
            for i in range(k,lenghth):
                if current_word==((lista[i])[0]):
                    current_count=current_count+(lista[i])[1]
                    #on regarde si le mot réapparait plus loin dans la liste
                    # et on ajoute le décompte au décompte déja effectué

                else :
                    current_count=current_count
                    #s'il ne réapparait pas on garde le décompte tel quel
            sum.append((current_word,current_count))
      return(sum)


def mapreduce(filename):
    #la fonction mapreduce prend en argument un ficher text
    fileread = open(filename, 'r')                   #lire le fichier
    rows = [line.rstrip() for line in fileread]      #créer une liste avec les lignes du texte
    numberlines=len(rows)
    print(numberlines)
    Masterlist=[]
    result=[]

    for i in range(0,numberlines):
        a=reduce(map(rows[i]))                      #on utilise reduce sur chaque ligne
        if isinstance(a,list):
         Masterlist=Masterlist+reduce(map(rows[i]))  #on ajoute les décomptes par ligne à une masterlist
        else:
          pass
          # si reduce ne renvoie pas une liste de (word1,1)...car on tombe sur une ligne vide
          #alors on passe

    result = reduce(Masterlist)                     #on effectue le décompte sur la MasterList
    print(result)


mapreduce('Article1.txt') #exemple sur un article



















































