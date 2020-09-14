
import requests, bs4, re, time


def scrapethread(cleanthread):		# We need to feed the thread data into the function
    singlethreadlinksearch = re.compile(r'\<a class="storylink" href="(.+?)"\>')
    singlethreadlink = singlethreadlinksearch.findall(str(cleanthread))

    commenterIDsearch = re.compile(r'user\?id=(.+?)"')
    commenterIDs = commenterIDsearch.findall(str(cleanthread))

    try:
        firstcommenter = commenterIDs[1]		# If there are no commenters this will fail, so we wrap it in a try/except just in case
    except:
        firstcommenter = "No commenters"
    return singlethreadlink, firstcommenter




# get the data of the page downloaded
pagedata = requests.get("https://news.ycombinator.com/")

cleanPageData = bs4.BeautifulSoup(pagedata.text,'html.parser')

print(cleanPageData)


IDsearch = re.compile(r'vote\?id=(\d+)&amp')
threadsIds= IDsearch.findall(str(cleanPageData))

print(len(threadsIds))

commentLinks=[]
for i in range(len(threadsIds)):
    commentLinks.append("https://news.ycombinator.com/item?id=" + threadsIds[i])

print(commentLinks)

thread = requests.get(commentLinks[1])
cleanThread = bs4.BeautifulSoup(thread.text,'html.parser')
print("\n  \n It starst here the second page \n \n ")
#print(cleanThread)



singlethreadlinksearch = re.compile(r'\<a class="storylink" href="(.+?)"\>')		# again, don’t forget the escape \ before characters like < and >
singlethreadlink = singlethreadlinksearch.findall(str(cleanThread))
 #the link of the news
print(singlethreadlink)

commenterIDsearch = re.compile(r'user\?id=(.+?)"')
commenterIDs = commenterIDsearch.findall(str(cleanThread))

print(commenterIDs)


firstCommenter =commenterIDs[1]

print(firstCommenter)

results = []        # We want our results to come back as a list
for i in range(len(commentLinks)):
    thread = requests.get(commentLinks[i])      # Go to each link
    cleanthread = bs4.BeautifulSoup(thread.text, 'html.parser')
    link, commenter = scrapethread(cleanthread)        # Scrape the data and return them to these variables
    results.append(link + [commenter])      # Append the results - note that the link actually returns as a list, rather than a string
    print( f"done with {i}")



