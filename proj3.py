import numpy as np
# DNA baser
BASES = ["A", "T", "C", "G"]

def get_random_sequence(n, seed = None):
    """
    Returnerar en slumpmässig DNA-sekvens med längden n.
    Parameters
    ----------
    n : int
    Sekvensens längd.
    seed : int, optional
    Slumpfrö som kan användas för reproducerbara resultat.
    Returns
    -------
    str
    En slumpmässig DNA-sekvens.
    """
    np.random.seed(seed)
    rand_ids = np.random.randint(0,4,int(n))
    seq = ''.join([BASES[idx] for idx in rand_ids])
    return seq


def dna_shift_encrypt(seq, key):
    """
    Returnerar en krypterad DNA-sträng genom att skifta baserna med key steg.
    Parameters
    ----------
    seq : str
    Okrypterad DNA-sekvens
    key : int
    Antalet steg DNA-baserna skiftas
    Returns
    -------
    str
    Den krypterade DNA-sekvensen
    """
    #skapar en ny lista för de nya krypterade bokstäverna
    krypt_1 = []
    for i in seq:
        index = BASES.index(i) #tar indexet av BASES av varje bokstav i seq 
        nytt_index = (index + key) % 4 # lägger till key till indexet och kör modolu 4 på den då index ska vara mellan 0 och 3
        krypt_1.append(BASES[nytt_index]) #lägger till i listan
    

    krypt_seq_1 = ''.join(krypt_1) #gör om listan till en sträng
    return krypt_seq_1


def dna_shift_decrypt(encrypt_seq, key):
    """
    Returnerar en dekrypterad DNA-sträng som har krypterats genom att skifta
    baserna med key steg.
    Parameters
    ----------
    encrypt_seq : str
    Krypterad DNA-sekvens
    key : int
    Antalet steg DNA-baserna skiftas
    Returns
    -------
    str
    Den okrypterade DNA-sekvensen
    """
    dekrypt_1 = []
    for i in encrypt_seq:
        index = BASES.index(i)
        nytt_index = (index - key) % 4 # subtraherar med key istället för adderar eftersom vill ta tillbaka det
        dekrypt_1.append(BASES[nytt_index])
   
    seq_1 = ''.join(dekrypt_1)
    return seq_1


def bases_krypto(key_word):
    """Returnerar en subsituerad DNA baser lista baserad på key_word"""

    stor_lista = list(key_word.upper()) #gör alla bokstäver till stora och lägger till de i en lista
    krypto_lista = [] #tom lista där de subsituerade dna baserna läggs till
    for i in stor_lista:
        if i in BASES:
            krypto_lista.append(i) #om en bokstav i key_word finns i dna baser så läggs den till i listan
    
    for j in range(len(krypto_lista) - 1, 0, -1): #spannet börjar på längden -1 av krypto_lista och slutar på 0 och hoppar ett steg åt vänster varje gång. 
        if krypto_lista[j] in krypto_lista[:j]:
            krypto_lista.pop(j) #om sista bokstaven i listan är samma som en bokstav i listan fram till sista bokstaven så tas den bort från listan

    for i in BASES:
        if i not in krypto_lista:
            krypto_lista.append(i) #om en bokstav i bASES inte finns i krypto_lista så adderas den till listan

    return krypto_lista


def dna_substitution_encrypt(seq, key_word):
    """
    Returnerar en krypterad DNA-sträng genom substitution baserad på key_word.
    Parameters
    ----------
    seq : str
    Okrypterad DNA-sekvens
    key_word : str
    Nyckelord som definierar substutitionen
    Returns
    -------
    str
    Den krypterade DNA-sekvensen
    """
    krypto_lista =bases_krypto(key_word) #kallar på dna bas listan

    krypt_2 = [] #lägger till vad bokstäverna i seq är av den nya listan
    
    for i in seq:
        index = BASES.index(i) #vi får fram vilket index i har i BASES
        krypt_2.append(krypto_lista[index]) #använder indexet från bases för att få fram vilken bokstav den är från nya lsitan

    krypt_seq_2 = ''.join(krypt_2) #gör listan till en sträng
    return krypt_seq_2


def dna_substitution_decrypt(encrypt_seq, key_word):
    """
    Returnerar en dekrypterad DNA-sträng som har krypterats genom substitution
    baserad på key_word.
    Parameters
    ----------
    encrypt_seq : str
    Krypterad DNA-sekvens
    key_word : str
    Nyckelord som definierar substutitionen
    Returns
    -------
    str
    Den okrypterade DNA-sekvensen
    """
    dekrypt_lista = bases_krypto(key_word)

    dekrypt_2 = []
        
    for i in encrypt_seq:
        index = dekrypt_lista.index(i)
        dekrypt_2.append(BASES[index]) # går åt andra steget, från nya listan till BASES

    seq_2 = ''.join(dekrypt_2)
    return seq_2


def dna_checksum(seq):
    """
    Returnerar en kontrollsumma baserad på en DNA-sekvens definierad som 1*antal_A
    + 2*antal_T + 3*antal_C + 4*antal_G.
    Parameters
    ----------
    seq : str
    DNA-sekvens
    Returns
    -------
    int
    Kontrolsumman
    """
    lista = list(seq) #gör strängen seq rill en lista
    a = lista.count('A') #kollar hur många A som finns i listan
    g = lista.count('G')
    c = lista.count('C')
    t = lista.count('T')
    checksum = a + 2 * t + 3 * c + 4 * g
    return checksum