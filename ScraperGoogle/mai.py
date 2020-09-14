import requests, bs4, re, time, selenium
from selenium import webdriver
import datetime

def getText (link) :    #used to get the text format of an html site
    Page = requests.get(link)
    PageData = bs4.BeautifulSoup(Page.text, 'html.parser')
    cleanPageData = str(PageData)
    return cleanPageData

def getListByRegex(start,rawText) :  #ofer a list of objects begginig with a certain regex
    Regex=start+"\"(.*?)\""
    regexSerch=re.compile(Regex)
    results=regexSerch.findall(rawText)
    return results

def generateFile(nameObject,listObjects,indexPage ,priceList): #writes the file
    finalObjects=[]
    for obj in listObjects:
        if (str(obj).__contains__("eMAG")) :
            continue
        else:
            finalObjects.append(obj)

    finalObjects=finalObjects[0:len(finalObjects)-3]

    finalForm=dict(zip(finalObjects,priceList))

    with  open(nameObject+".txt", "a+",encoding="utf-8") as titlesFile:
        for title,price in finalForm.items():
            titlesFile.write(title + " with a PRICE of " + str(price)+ '\n')
        titlesFile.write("Final page "+str(indexPage)+ " \n")



def getObject(link,indexPage):  #for a certain page it removes all the objects and writes them in the file
    print("intrat cu linkul " + link)

    pagedata = requests.get(link)
    HtmlPageData = bs4.BeautifulSoup(pagedata.text, 'html.parser')
    cleanPageData = str(HtmlPageData)

    objects = getListByRegex("alt=", cleanPageData)

    regex = "price\">([0-9]\.*[0-9]*)"
    serchPrice = re.compile(regex)
    listaPreturi = serchPrice.findall(cleanPageData)

    generateFile(serchObject, objects,indexPage,listaPreturi)




driver = webdriver.Chrome(executable_path='C:\\Users\\Vlad\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\selenium\\webdriver\\chromedriver.exe')
driver.get('http://www.google.com/')




serchObject = input("The object you wish to serch : ")

serchObject = serchObject.replace(" ", '+')

for i in range(1):
    matched_elements = driver.get("https://www.google.com/search?q=" + serchObject + "&start=" + str(i))
    wantedLink = "https://www.google.com/search?q=" + serchObject + "&start=" + str(i)

print(wantedLink)
link = wantedLink

cleanPageData=getText(link)


regex = "href=\"(.*?)\""
titlesSearch = re.compile(regex)
titles = titlesSearch.findall(cleanPageData)

titles= getListByRegex("href=",cleanPageData)

for i, tit in enumerate(titles, start=1):
    if str(tit).__contains__('https://www.emag.ro/'):
        tit = tit.partition("/url?q=")[2].partition("&amp")
        emagGoodLink=tit[0]
        break

print("\n" +emagGoodLink)


time.sleep(3)


driver.get(emagGoodLink)


cleanEmagPageData= getText(emagGoodLink)


regex="price\">([0-9]\.*[0-9]*)"

serchPrice=re.compile(regex)
listaPreturi=serchPrice.findall(cleanEmagPageData)
#print(listaPreturi)


objects=getListByRegex("alt=",cleanEmagPageData)

objects.pop(0);
#print(dict(zip(objects,listaPreturi)))


regexTotalNumber="din (\d*)"

totalPageSerch=re.compile(regexTotalNumber)
totalPages=totalPageSerch.findall(cleanEmagPageData)

print("\t Total Number Of Pages is "+ str(totalPages[1])+"\n")


getObject(emagGoodLink,1)
if str(emagGoodLink).endswith('c'):
    getObject(emagGoodLink.replace("/c","/p2/c"),2)
else:
    getObject(emagGoodLink+"/p2", 2)


# driver.get("https://www.epantofi.ro/dama/pantofi/sneakers.html?gclsrc=aw.ds&&gclid=Cj0KCQjw0rr4BRCtARIsAB0_48N3yW5FGOA6exUpcbnvpizGZPh42dxqRg55_WqC2mUBdZU5ILODZKoaAjSXEALw_wcB&gclsrc=aw.ds")
#
# testPageData=getText("https://www.epantofi.ro/dama/pantofi/sneakers.html?gclsrc=aw.ds&&gclid=Cj0KCQjw0rr4BRCtARIsAB0_48N3yW5FGOA6exUpcbnvpizGZPh42dxqRg55_WqC2mUBdZU5ILODZKoaAjSXEALw_wcB&gclsrc=aw.ds")
#
# objectsTest=getListByRegex("alt=",testPageData)
#
# print(objectsTest)













