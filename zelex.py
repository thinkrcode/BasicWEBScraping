import os
import requests
# url_d, datainstall, showData_d, skipdata, CLI menu_d              "d = done"
try:
        r = requests.get('https://www.smsonay.com')
        content = r.content.decode('utf-8')
        start_swith = '<h2 class="pt-10 mb-20 text-light">'
        end_swith= '</h2>'
        myword = 'SMS'
        temp = []

        if r.status_code == 200:
                print(f"Status: {r.status_code}, Your connection successfully completed.")
        else:
            raise Exception("Status: {r.status_code}, Your connection lost.")

        if myword in content:
            print(f"Word: {myword}, Founded.")
        else:
            print(f"{myword}, Not found.")
                
        def getData():
            try:
                temp = (content.split(start_swith, 1)[1])
                temp = (temp.split(end_swith,1)[0])
                def createFile():
                    try:
                        
                        os.system('mv zelex_pt.txt zelex')
                    except Exception as e:
                        raise Exception({e}, 'An error ocurred')
                createFile()

            except Exception as x:
                print(f'{x}, An error ocurred')

        def showData():
            print(f"Data exporting on line.\n")
            print(temp)

        def readFile():
            y = os.open(os.path.abspath('zelex/zelex_pt.txt'), os.O_RDONLY)
            y = os.read(y, y+y)
            print(y)

        getData()
        readFile()

except requests.exceptions.RequestException as e:
     print(f"{e}, An error ocurred.")
