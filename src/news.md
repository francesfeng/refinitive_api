# Extract news headlines and article

#### Choose refinitiv news source from['NewsRoom', 'NewsWire', 'WebNews']

```
headlines = ek.send_json_request("News_Headlines", 
                                 {
                                     'number': '15', 
                                     'query': 'R:EQNR.OL and Language:LEN',
                                     'dateFrom':'2018-08-21T00:00:00',
                                     'dateTo':'2018-09-21T12:00:00',
                                     'repository':'NewsRoom'
                                 }
                                )
```



#### Extract news article and meta 

```
import refinitiv.data as rd
import time 

# createa a session
rd.open_session()

```
The open_session() function creates and open sessions based on the information contained in the refinitiv-data.config.json configuration file. Please edit this file to set the session type and other parameters required for the session you want to open.

```
baseurl = "/data/news/v1/stories/"
fullcodelist = pd.DataFrame()
compNews['storyText'] = str()
compNews['q_codes'] = str()
compNews['pIDs_mentioned'] = str()
compNews['RICs_mentioned'] = str()
compNews['urgency'] = str()

for i, uri in enumerate(compNews['storyId']):
    request_definition = rd.delivery.endpoint_request.Definition(
        url = baseurl + uri,
        method = rd.delivery.endpoint_request.RequestMethod.GET
    )
    response = request_definition.get_data()
    time.sleep(0.1)
    rawr = response.data.raw
    if 'newsItem' in rawr.keys():
        compNews['storyText'][i] = rawr['newsItem']['contentSet']['inlineData']['$']
        topics = rawr['newsItem']['contentMeta']['subject']
        rics = [x for x in rawr['newsItem']['assert'] if x['_qcode'].startswith("R:")]
        compNews['q_codes'][i] = [d['_qcode'] for d in topics]
        compNews['pIDs_mentioned'][i] = [x for x in compNews['q_codes'][i] if x.startswith("P:")]
        compNews['RICs_mentioned'][i] = [d['_qcode'] for d in rics] 
        compNews['urgency'] = rawr['newsItem']['contentMeta']['urgency']['$'] # 1 = hot, 3 = regular
    ```
