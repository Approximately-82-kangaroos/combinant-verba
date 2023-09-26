import requests
import time
import string
from itertools import product

OUT_FILE = "/your directory here/combinant-verba.txt"

def get_tor_session():
    session = requests.session()
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session

def generate_permutations(password):
    subDict = {
	    'a': ['a','A','@','4'],
    	'b': ['b','B','8','6'],
    	'c': ['c','C','[','{','(','<'], 
	    'd': ['d','D',], 
	    'e': ['e','E','3'], 
	    'f': ['f','F'], 
	    'g': ['g','G','6','9'], 
	    'h': ['h','H','#'], 
	    'i': ['i','I','1','l','L','|','!','(',')','[',']','{','}','/','\\',':',';','7'], 
	    'j': ['j','J','i','I',':',';'], 
	    'k': ['k','K','|<'], 
	    'l': ['l','L','i','I','|','!','1','(',')','[',']','{','}','/','\\',':',';','7'], 
	    'm': ['m','M','^^'], 
	    'n': ['n','N'], 
	    'o': ['o','O','0','Q','()','[]','{}'], 
	    'p': ['p','P'], 
	    'q': ['q','Q','9','0','O'], 
	    'r': ['r','R'], 
	    's': ['s','S','$','5','z','Z'], 
	    't': ['t','T','+','7'], 
	    'u': ['u','U','v','V'], 
	    'v': ['v','V','u','U'], 
	    'w': ['w','W','vv','VV','uu','UU'], 
	    'x': ['x','X','+','*','><'], 
	    'y': ['y','Y','v','V'], 
	    'z': ['z','Z','2','s','S'],
        'A': ['a','A','@','4'],
        'B': ['b','B','8','6'],
    	'C': ['c','C','[','{','(','<'], 
	    'D': ['d','D',], 
	    'E': ['e','E','3'], 
	    'F': ['f','F'], 
	    'G': ['g','G','6','9'], 
	    'H': ['h','H','#'], 
	    'I': ['i','I','1','l','L','|','!','(',')','[',']','{','}','/','\\',':',';','7'], 
	    'J': ['j','J','i','I',':',';'], 
	    'K': ['k','K','|<'], 
	    'L': ['l','L','i','I','|','!','1','(',')','[',']','{','}','/','\\',':',';','7'], 
	    'M': ['m','M','^^'], 
	    'N': ['n','N'], 
	    'O': ['o','O','0','Q','()','[]','{}'], 
	    'P': ['p','P'], 
	    'Q': ['q','Q','9','0','O'], 
	    'R': ['r','R'], 
	    'S': ['s','S','$','5','z','Z'], 
	    'T': ['t','T','+','7'], 
	    'U': ['u','U','v','V'], 
	    'V': ['v','V','u','U'], 
	    'W': ['w','W','vv','VV','uu','UU'], 
	    'X': ['x','X','+','*','><'], 
	    'Y': ['y','Y','v','V'], 
	    'Z': ['z','Z','2','s','S'],
        '0': ['0','o','O','Q'],
        '1': ['1','l','L','i','I','|','!','(',')','[',']','{','}','/','\\'],
        '2': ['2','s','S','z','Z','5','@'],
        '3': ['3','e','E','8','#'],
        '4': ['4','a','A','@','$'],
        '5': ['5','z','Z','2','s','S','%'],
        '6': ['6','b','B','8','^'],
        '7': ['7','t','T','y','Y','1','l','L','i','I','|','!','(',')','[',']','{','}','/','\\','&'],
        '8': ['8','B','b','O','o','0','()','[]','{}','*'],
        '9': ['9','g','G','6','(']
    }
    dummyCharacters = (string.punctuation + string.digits)
    letters = []
    #place substitution sets into the letters array
    for val in password:
        if val in subDict.keys():
            letters.append(subDict[val])
        else:
            letters.append(val)
    # return list(product(*letters))
    return [''.join(item) for item in product(*letters)]

session = get_tor_session()
pwd_list = []

open(OUT_FILE, "w").write("")

with open(OUT_FILE, "a") as outfile:
    with open('sources.list') as pwd_list_file:
        i = 0
        for line in pwd_list_file:
            file_to_cat = session.get(line.strip()).text
            for line2 in iter(file_to_cat.splitlines()):
                i += 1
                pwd_list2 = generate_permutations(line2)
                j = 0
                for pwd in pwd_list2:
                   if pwd in pwd_list:
                       print("Passing...")
                   else:
                       j += 1
                       pwd_list.append(pwd)
                       outfile.write(f"{pwd}\n")
                       print(f"{pwd}\t{i}\t{len(pwd_list2)}\t{j}\t{len(pwd_list)}")
