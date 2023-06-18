import WebScraper
import pandas as pd

PlacesInfo = WebScraper.ShabIrScraper.GetShabIRData()

PlacesInfoDF = pd.DataFrame(PlacesInfo[0])
print (PlacesInfoDF)

PlacesInfoDF.to_csv('PlacesInfoShabIr.csv', encoding='utf-8')

PlacesCalendarDF = pd.DataFrame(PlacesInfo[1])

print (PlacesCalendarDF)

PlacesCalendarDF.to_csv('PlacesCalendarShabIr.csv', encoding='utf-8')

