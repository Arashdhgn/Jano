import requests
from bs4 import BeautifulSoup
import pandas as pd


class ShabIrScraper:
    def __init__(self):
        pass
    #to get the links of the popular cities and their names
    def Getsoup(url_site):
        # url_site = "https://shab.ir"
        website = requests.get(url_site)
        soup = BeautifulSoup(website.text,'html.parser')
        return soup

    def GetPopularCitylink(soup):
        CityLinks = []
        CityNames = []
        # url_site = "https://shab.ir"
        # website = requests.get(url_site)
        # soup = BeautifulSoup(website.text,'html.parser')
        WholeText = soup.find_all('a', {'class': "bg-cover city-item rtl-mui-1hlq8s2 e1j1qvdd11"})
        for i in range(len(WholeText)):
            if WholeText[i]:

                CityNamedirty = WholeText[i].find('span', {'class': 'city-name'.split(' ')})
                if type(CityNamedirty) != 'bs4.element.Tag':
                    CityName = str(CityNamedirty)
                    CityName = CityName.replace('<span class="city-name">','').replace('</span>','')
                    CityNames.append(CityName)
                    CityLinks.append('https://www.shab.ir/search/city/' + CityName)
        return [CityNames,CityLinks]


    def getplacespercity(CityName,CityLink):
        PlaceLinks = []
        mainUrl = CityLink+'?page='
        for page in range (1,100):
            url_site = mainUrl + str(page)
            website = requests.get(url_site)
            soup = BeautifulSoup(website.text,'html.parser')
            WholeText = soup.find_all('div', {'class': "MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiCard-root rtl-mui-pdeu6g"})#('li', {'class': "MuiGrid-root MuiGrid-grid-xs-1 MuiGrid-grid-sm-5 MuiGrid-grid-md-4 home-card-item rtl-mui-1wb2hol"})
            # print (WholeText)
            if len(WholeText) == 0:
                break
            for i in range(len(WholeText)):
                PlacelinkDirty = WholeText[i].find('a',href = True )
                LinkPlace = str(WholeText[i]).find('"><')
                PlaceLink = str(PlacelinkDirty)[9:LinkPlace].replace('"><article class="MuiGrid-root MuiGrid-container MuiGrid-direction-xs-c','')
                PlaceLinks.append(PlaceLink)
        return [CityName , PlaceLinks]


    def GetPlaceinfo(PlaceLink):
        if len(PlaceLink) != 0:
            PlaceInfoSoup = ShabIrScraper.Getsoup('https://www.shab.ir/' + PlaceLink)
        else:
            return ['','','','','','','','','','','','','','']
            print ('no place info')

        #code
        WholeText = PlaceInfoSoup.find_all('div', {'class': "productCode MuiBox-root rtl-mui-0"})
        if len(WholeText) != 0 :
            PlaceCode = str(WholeText[0]).replace('<div class="productCode MuiBox-root rtl-mui-0"><p>کدآگهی:</p><p>','').replace ('</p></div>','')
        else :
            PlaceCode = ''
            return ['','','','','','','','','','','','','','']
        print (PlaceCode)

        #name
        WholeText = PlaceInfoSoup.find_all('h1', {'class': "productName"})
        if len(WholeText) != 0 :
            PlaceName = str(WholeText[0]).replace('<h1 class="productName">','').replace ('</h1>','')
        else :
            PlaceName = ''
        print(PlaceName)

        #score
        WholeText = PlaceInfoSoup.find_all('div', {'class': "rating MuiBox-root rtl-mui-0"})
        if len(WholeText) != 0:
            PlaceScore = str(WholeText[0]).replace('<div class="rating MuiBox-root rtl-mui-0">', '').replace('</div>', '')
        else :
            PlaceScore = ''
        print(PlaceScore)

        #From Price
        WholeText = PlaceInfoSoup.find_all('span', {'class': "MuiBox-root rtl-mui-w0wkh2"})
        if len(WholeText) != 0:
            PlaceFromScore = str(WholeText[0]).replace('<span class="MuiBox-root rtl-mui-w0wkh2">', '').replace('<!-- --> <!-- -->تومان</span>', '')
            PlaceFromScore.replace(',','')

        else :
            PlaceFromScore = ''
        print(PlaceFromScore)

        #location
        PlaceProvince = ''
        PlaceCity = ''
        PlaceNeighborhood = ''
        WholeText = PlaceInfoSoup.find_all('p', {'class': "location"})
        if len(WholeText) != 0:
            WholeTextList = str(WholeText[0]).split('،')
            for i in range (len(WholeTextList)):
                if i == 0:
                    PlaceProvince = str(WholeTextList[i]).replace('<p class="location"><a><a> <!-- -->','').replace('<!-- --> ','')
                    print(PlaceProvince)
                if i == 1:
                    PlaceCity = str(WholeTextList[i]).replace(' </a><a>', '').replace('<!-- --> </a><a>','').replace('<!-- -->','').replace('</a></a></p>','')
                    print(PlaceCity)
                if i == 2:
                    PlaceNeighborhood = str(WholeTextList[i]).replace('</a></a></p>', '')
                    print(PlaceNeighborhood)

        #Type
        WholeTextDirty = PlaceInfoSoup.find_all('div', {'class': "infoItem MuiBox-root rtl-mui-0"})
        PlaceBuildingType = ''
        PlaceRentalType = ''
        PlaceSecurityType = ''
        PlaceM2 = ''
        PlaceRooms = ''
        PlaceExtraPersonCost = ''
        PlaceCapacity = ''
        if len(WholeTextDirty) != 0:
            for i in range(len(WholeTextDirty)):
                if i == 0:
                    Wholetext = WholeTextDirty[i].find('h3')
                    WholeTextList= str(Wholetext).split('-->')
                    #Buildingtype
                    if len (WholeTextList) > 1:
                        PlaceBuildingType = WholeTextList[1].replace(" '",'').replace(" '",'').replace('<!--','').replace('</h3>','')
                    if len(WholeTextList) > 3:
                        PlaceRentalType = WholeTextList[3].replace('<!-- ','').replace('</h3>','')
                    if len(WholeTextList) > 5:
                        PlaceSecurityType = WholeTextList[5].replace(' - ','').replace('</h3>','')
                    print (PlaceBuildingType)
                    print (PlaceRentalType)
                    print (PlaceSecurityType)
                    Wholetext2 = WholeTextDirty[i].find_all('p')
                    PlaceM2 = str(Wholetext2[4]).replace('<p class="inlineBlock secondaryInfo"> <!-- -->','').replace('<!-- --> متر</p>','')
                    PlaceRooms = str(Wholetext2[2]).replace('<p class="inlineBlock secondaryInfo">','').replace('<!-- --> <!-- -->اتاق</p>','').replace('</p>','')
                    print(PlaceM2)
                    print (PlaceRooms)
                if i == 1:
                    WholeText = WholeTextDirty[i].find('h3')
                    #Capacity
                    PlaceCapacity = str(WholeText)[:10].replace('<h3>','').replace('<!--','')
                    print (PlaceCapacity)
                    #ExtraPersonCost

                    Wholetext2 = WholeTextDirty[i].find('p')
                    WholeTextList2 = str(Wholetext2).split('-->')
                    if len(WholeTextList2) > 2 :
                        PlaceExtraPersonCost = WholeTextList2[2].replace('<!-- ','')
                        PlaceExtraPersonCost.replace(',','')
                    print(PlaceExtraPersonCost)
        return [PlaceCode,PlaceName,PlaceScore,PlaceFromScore,PlaceProvince,PlaceCity,PlaceNeighborhood,PlaceM2
            ,PlaceRooms,PlaceCapacity,PlaceBuildingType,PlaceRentalType,PlaceSecurityType,PlaceExtraPersonCost]


    def GetShabIRData():
        import time as time

        PlaceData = {'PlaceCode' : [],'PlaceName' : [],'PlaceScore' : [],'PlaceFromPrice' : [],'PlaceProvince' : [],
                     'PlaceCity' : [],'PlaceNeighborhood'  : [],'PlaceM2' : [],'PlaceRooms' : [],'PlaceCapacity' : [],
                     'PlaceBuildingType': [],'PlaceRentalType': [],'PlaceSecurityType': [],'PlaceExtraPersonCost': []}
        CalendarData = {'PlaceCode': [], 'Year': [], 'Month': [], 'Day': [], 'Price': [], 'Currency': [],
                        'is_holiday': [], 'is_peek': [], 'is_unavailable': [], 'is_promoted_day': [],
                        'is_non_bookable': []}
        TestSoup = ShabIrScraper.Getsoup("https://shab.ir")
        CityList = ShabIrScraper.GetPopularCitylink(TestSoup)
        print(CityList)
        CityPlacesLinks = []
        PlacesCityNames = []
        for i in range (len(CityList[0])):
            CityLinkList = ShabIrScraper.getplacespercity(CityList[0][i], CityList[1][i])
            print(CityLinkList)
            CityPlacesLinks.append(CityLinkList[0])
            PlacesCityNames.append(CityLinkList[1])
            print(len(CityLinkList[1]))
            for cityplaceslinklist in CityLinkList:
                time.sleep(10.0)
                for link in cityplaceslinklist:
                    info = ShabIrScraper.GetPlaceinfo(link)
                    Calendarjson = ShabIrScraper.getCalendarJson(link,'from_date=1402-06-01&to_date=1402-07-01')
                    if info != ['','','','','','','','','','','','','','']:
                        PlaceCalendarData = ShabIrScraper.GetPlaceCalendar(Calendarjson[0], info[0])
                        PlaceData['PlaceCode'].append(info[0])
                        PlaceData['PlaceName'].append(info[1])
                        PlaceData['PlaceScore'].append(info[2])
                        PlaceData['PlaceFromPrice'].append(info[3])
                        PlaceData['PlaceProvince'].append(info[4])
                        PlaceData['PlaceCity'].append(info[5])
                        PlaceData['PlaceNeighborhood'].append(info[6])
                        PlaceData['PlaceM2'].append(info[7])
                        PlaceData['PlaceRooms'].append(info[8])
                        PlaceData['PlaceCapacity'].append(info[9])
                        PlaceData['PlaceBuildingType'].append(info[10])
                        PlaceData['PlaceRentalType'].append(info[11])
                        PlaceData['PlaceSecurityType'].append(info[12])
                        PlaceData['PlaceExtraPersonCost'].append(info[13])
                        for i in range(0, len (PlaceCalendarData['PlaceCode'])):
                            CalendarData['PlaceCode'].append(PlaceCalendarData['PlaceCode'][i])
                            CalendarData['Year'].append(PlaceCalendarData['Year'][i])
                            CalendarData['Month'].append(PlaceCalendarData['Month'][i])
                            CalendarData['Day'].append(PlaceCalendarData['Day'][i])
                            CalendarData['Price'].append(PlaceCalendarData['Price'][i])
                            CalendarData['Currency'].append(PlaceCalendarData['Currency'][i])
                            CalendarData['is_holiday'].append(PlaceCalendarData['is_holiday'][i])
                            CalendarData['is_peek'].append(PlaceCalendarData['is_peek'][i])
                            CalendarData['is_unavailable'].append(PlaceCalendarData['is_unavailable'][i])
                            CalendarData['is_promoted_day'].append(PlaceCalendarData['is_promoted_day'][i])
                            CalendarData['is_non_bookable'].append(PlaceCalendarData['is_non_bookable'][i])


        return [PlaceData,CalendarData]
    def getCalendarJson(PlaceLink,Date):

        if len(PlaceLink) != 0:
            PlaceInfoSoup = ShabIrScraper.Getsoup('https://www.shab.ir/' + PlaceLink)
        else:
            return ''
            print('no place info')

        # code
        WholeText = PlaceInfoSoup.find_all('div', {'class': "productCode MuiBox-root rtl-mui-0"})
        if len(WholeText) != 0:
            PlaceCode = str(WholeText[0]).replace('<div class="productCode MuiBox-root rtl-mui-0"><p>کدآگهی:</p><p>',
                                                  '').replace('</p></div>', '')
        else:
            PlaceCode = ''
            return ''
        print(PlaceCode)



        import http.client
        import json

        Connection = http.client.HTTPSConnection("www.shab.ir")

        payload = ""

        headers = {
            'authority': "www.shab.ir",
            'accept': "application/json, text/plain, */*",
            'accept-language': "en-US,en;q=0.9,fa;q=0.8",
            'cookie': "_gcl_au=1.1.810021717.1682783884; analytics_token=734e2e84-10f4-e2ed-98d4-467a240ff4d1; _yngt=93c728b9-cccb-403b-a34e-84ef426b91e7; lang=fa; _hjSessionUser_1492433=eyJpZCI6IjQyY2UzNGU1LWJlZDItNTA4Yi04MTBmLWY5NmEwZWZiNWEyZiIsImNyZWF0ZWQiOjE2ODI3ODM4ODQ4NzMsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.553633045.1684405054; _yngt_iframe=1; _clck=k0vqgf^|2^|fbr^|0^|1228; yektanet_session_last_activity=5/20/2023; _ga=GA1.1.1420522518.1682783883; shab_session=eyJpdiI6InVqU1dHemcxTzhBNUJiMkFva0NqMWc9PSIsInZhbHVlIjoicHpESDBnVGxYZHZUOVp2QmplRTM0Y2lneGVpUnFYWlJ4VTNsaXpKK1JOQzFhYW5YVU8rdVRNbFhnNUNrYW5XRCtkeHdMaGFBQVRHNHVKdXpac0JxcERzS1Ruck1SKzJWS3ByaEcrWk1hRWVLNTFZeDZJUDdOZHpKNHFoTHgxUTMiLCJtYWMiOiI2N2IzOGVlYTk3OTQ0NjQ1NzM2MDRmNjFlOTFkMjMzMzZjODdkNGJhYTJiZGMzODRhM2VjODZiMmQ5Y2E2NmMzIiwidGFnIjoiIn0^%^3D; _ga_5MZJRDTX36=GS1.1.1684589480.9.0.1684589480.0.0.0",
            'referer': "https://www.shab.ir" + PlaceLink,
            'sec-ch-ua': "^\^Google",
            'sec-ch-ua-mobile': "?0",
            'sec-ch-ua-platform': "^\^Windows^^",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            'shab-app': "web",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
        }

        Connection.request("GET", "/api/fa/sandbox/v_1_4/house/"+PlaceCode+"/calendar?"+Date,
                     payload, headers)
        #from_date=1402-02-01&to_date=1402-06-01
        res = Connection.getresponse()
        data = res.read()
        if data is not None and len(data) > 0:
            JsonData = json.loads(str(data.decode("utf-8")))
        # print(type(JsonData))
            return [JsonData,PlaceCode]
        else:
            return ['','']



    def GetPlaceCalendar (JsonData, PlaceCode):

        CalenderData = {'PlaceCode' : [],'Year': [],'Month': [],'Day': [],'Price': [],'Currency': [],'is_holiday': [],'is_peek' : [],'is_unavailable' : [],'is_promoted_day' : [],'is_non_bookable' : []}

        # print(JsonData["data"]['records'])
        if len(JsonData) > 0 and JsonData["data"] is not None:
            if len(JsonData["data"]['records']) > 0:
                for month in JsonData["data"]['records']:
                    for day in JsonData["data"]['records'][month]:
                        CalenderData['PlaceCode'].append(PlaceCode)
                        Yearmonth = month.split('-')
                        CalenderData['Year'].append(Yearmonth[0])
                        CalenderData['Month'].append(Yearmonth[1])
                        CalenderData['Day'].append(day['day'])
                        CalenderData['Price'].append(day['price']['amount'])
                        CalenderData['Currency'].append(day['price']['currency_name'])
                        CalenderData['is_holiday'].append(day['is_holiday'])
                        CalenderData['is_peek'].append(day['is_peak'])
                        CalenderData['is_unavailable'].append(day['is_unavailable'])
                        CalenderData['is_promoted_day'].append(day['is_promoted_day'])
                        CalenderData['is_non_bookable'].append(day['is_non_bookable'])

        return CalenderData





#
# TestSoup = ShabIrScraper.Getsoup("https://shab.ir")
# testprint = ShabIrScraper.GetPopularCitylink(TestSoup)
# print(testprint)
# print (testprint[0])
#
#
# for i in range(len(testprint[0])):
#     testprint2 = ShabIrScraper.getplacespercity(testprint[0][i], testprint[1][i])
#     print (testprint2)
#     print (len(testprint2[1]))
#
# testprint3 = ShabIrScraper.GetPlaceinfo(testprint2[1][0])
#

# url_site = "https://shab.ir"
# website = requests.get(url_site)
# soup = BeautifulSoup(website.text, 'html.parser')
# div1 = soup.find('li', {'class': "splide__slide city-splide-item is-active is-visible"})
#
# print (div1[0])

# PlacesInfo = ShabIrScraper.GetShabIRData()
#
# PlacesInfoDF = pd.DataFrame(PlacesInfo)
# print (PlacesInfoDF)