import os
import requests

# --- Configuration ---
TARGET_URL = '' # first input
SEARCH_WORD = ''  # second input
START_DELIMITER = '' #automation index
END_DELIMITER = '' #automation index

# --- file configs ---
FILE_DIR = 'zelex'
FILE_NAME = 'zelex_pt.txt'
FULL_PATH = os.path.join(FILE_DIR, FILE_NAME)

# --- Global State ---
# Use global variables to share data between functions (carefully)
global parsed_data
temp = []

def siteStatus():
        if req.status_code == 200:
            print(f"Status: {req.status_code}, Your connection successfully completed.")
        else:
            raise Exception("Status: {r.status_code}, Your connection lost.")

def findWord():
    global parsed_data
    siteStatus()
    SEARCH_WORD = input('write your word: ')
    if SEARCH_WORD in content:
        print(f"Word: {SEARCH_WORD}, Founded.")
        START_DELIMITER = content.index(SEARCH_WORD)

        #first split control block
        while START_DELIMITER > 0 and content[START_DELIMITER] != '>':
            START_DELIMITER -= 1
        print('First split setted.')

        if START_DELIMITER == '>':
            START_DELIMITER += 1
        #second split control block
        print('Second split setted.')
        END_DELIMITER = START_DELIMITER # exploted

        while content[END_DELIMITER] != '<':
            END_DELIMITER += 1
        
        if END_DELIMITER == '<':
            END_DELIMITER -= 1
        parsed_data = content[START_DELIMITER:END_DELIMITER]
        print(parsed_data)

    else:
        print(f"{SEARCH_WORD}, Not found.")
        
def getData():
    global parsed_data
    if not content:
        print('Data not fetched, data is empty.')
        return
    
    try:
        def createFile():
            try:
                with open('zelex_pt.txt','w') as fileobject:
                    fileobject.write(parsed_data)
                os.system('mv zelex_pt.txt zelex')
                print('File created')
            except Exception as e:
                raise Exception({e}, 'An error ocurred')
        createFile()

    except Exception as x:
        print(f'{x}, An error ocurred')

def showData():
    print(f"Data exporting on line.\n")
    if parsed_data == None:
        print('Your parsed_data is NULL.')
        return
    print('here is your data:')
    print(parsed_data)

def readFile():
    with open(FULL_PATH, 'r', encoding='utf-8') as f:
        print(f.read())

try: #main block
    while True:
        print("""
         
            SELECT YOUR CHOICE
              
        1 - Set Website
        2 - Fetch Your Word
        3 - Get DATA
        4 - Show DATA
        5 - Read Current FILE DATA
        6 - Quit
                
        """)

        usrch = input('CH: ')

        match (usrch):
            case '1':
                print("add a manual 'http://' or 'https://' and don't insert end '/'")
                TARGET_URL = input('Which site will you get?: ')
                req = requests.get(TARGET_URL, timeout=10)
                content = req.content.decode('utf-8')
            case '2':
                findWord()
            case '3':
                getData()
            case '4':
                showData()
            case '5':
                readFile()
            case '6':
                break
            case _:
                print('your choice is Invalid, select any option 1,2,3,4')

except requests.exceptions.RequestException as e:
     print(f"{e}, An error ocurred.")
except KeyboardInterrupt as ki:
    print('\nQuitting...')
    quit
