import os
import requests
# My program running on smsonay.com and just get data.
# I want update my project near.
try:
        r = requests.get('https://www.smsonay.com')
        content = r.content.decode('utf-8')
        start_swith = '<h2 class="pt-10 mb-20 text-light">'
        end_swith= '</h2>'
        myword = 'SMS'
        mylist = []

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
                mylist = (temp.split(end_swith,1)[0])
                def createFile():
                    try:
                        output = open('zelex_pt.txt','w')
                        output.write(mylist)
                        os.system('mv zelex_pt.txt zelex')
                    except Exception as e:
                        raise Exception({e}, 'An error ocurred')
                createFile()

            except Exception as x:
                print(f'{x}, An error ocurred')

        def showData():
            print(f"Data exporting on line.\n")
            print(mylist)


        def readFile():
            temp = open('zelex/zelex_pt.txt')
        getData()
        readFile()

except requests.exceptions.RequestException as e:
     print(f"{e}, An error ocurred.")
