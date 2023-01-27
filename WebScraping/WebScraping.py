from bs4 import BeautifulSoup
import requests

def main():

    html_text = requests.get(url="https://en.wikipedia.org/wiki/Python_(programming_language)") # this line send request to HTTP request to specific URl.

    content = html_text.content

    soup = BeautifulSoup(content,"html.parser")

    Paragraph = soup.find_all("p")

    # Write data in file:

    fd = open(file="MarvellousWeb.txt",mode="w",encoding="utf-8")
    fd.write("DATA FROM SITE IS: \n")
    
    icnt = 0

    for para in Paragraph:
        line = para.get_text()
        icnt += 1
        fd.write(line)
        #print("LINE IS: ",line)

    print("lines are: ",icnt)

if __name__ =="__main__":
    main()

"""
1. get actual data from site.
2. write that data into a file.
3. new file is get created at run time.
response[200] 200 is a convention number in web that the request is done sucessfully.
"""