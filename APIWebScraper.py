import http.client

conn = http.client.HTTPSConnection("www.shab.ir")

payload = ""

headers = {
    'authority': "www.shab.ir",
    'accept': "application/json, text/plain, */*",
    'accept-language': "en-US,en;q=0.9,fa;q=0.8",
    'cookie': "_gcl_au=1.1.810021717.1682783884; analytics_token=734e2e84-10f4-e2ed-98d4-467a240ff4d1; _yngt=93c728b9-cccb-403b-a34e-84ef426b91e7; lang=fa; _hjSessionUser_1492433=eyJpZCI6IjQyY2UzNGU1LWJlZDItNTA4Yi04MTBmLWY5NmEwZWZiNWEyZiIsImNyZWF0ZWQiOjE2ODI3ODM4ODQ4NzMsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.553633045.1684405054; _yngt_iframe=1; _clck=k0vqgf^|2^|fbr^|0^|1228; yektanet_session_last_activity=5/20/2023; _ga=GA1.1.1420522518.1682783883; shab_session=eyJpdiI6InVqU1dHemcxTzhBNUJiMkFva0NqMWc9PSIsInZhbHVlIjoicHpESDBnVGxYZHZUOVp2QmplRTM0Y2lneGVpUnFYWlJ4VTNsaXpKK1JOQzFhYW5YVU8rdVRNbFhnNUNrYW5XRCtkeHdMaGFBQVRHNHVKdXpac0JxcERzS1Ruck1SKzJWS3ByaEcrWk1hRWVLNTFZeDZJUDdOZHpKNHFoTHgxUTMiLCJtYWMiOiI2N2IzOGVlYTk3OTQ0NjQ1NzM2MDRmNjFlOTFkMjMzMzZjODdkNGJhYTJiZGMzODRhM2VjODZiMmQ5Y2E2NmMzIiwidGFnIjoiIn0^%^3D; _ga_5MZJRDTX36=GS1.1.1684589480.9.0.1684589480.0.0.0",
    'referer': "https://www.shab.ir/houses/show/57024?from=search",
    'sec-ch-ua': "^\^Google",
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': "^\^Windows^^",
    'sec-fetch-dest': "empty",
    'sec-fetch-mode': "cors",
    'sec-fetch-site': "same-origin",
    'shab-app': "web",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    }

conn.request("GET", "/api/fa/sandbox/v_1_4/house/57024/calendar?from_date=1402-02-01&to_date=1402-06-01", payload, headers)

res = conn.getresponse()
data = res.read()
print(type(data))


# import ast
# ByteData = data
# DictData = ByteData.decode("utf-8")
# mydata = ast.literal_eval(ByteData)
#
# print (type(mydata))



print(data.decode("utf-8"))

import json
import pandas as pd

CalenderData = {'Year': [],'Month': [],'Day': [],'Price': [],'Currency': [],'is_holiday': [],'is_peek' : [],'is_unavailable' : [],'is_promoted_day' : [],'is_non_bookable' : []}
JsonData = json.loads(str(data.decode("utf-8")))
print(type(JsonData))
print(JsonData["data"]['records'])

for month in JsonData["data"]['records']:
        for day in JsonData["data"]['records'][month]:
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

            print(day)

CalenderDataDF = pd.DataFrame(CalenderData)

print(CalenderDataDF)