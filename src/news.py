# Choose refinitiv news source from['NewsRoom', 'NewsWire', 'WebNews']

headlines = ek.send_json_request("News_Headlines", 
                                 {
                                     'number': '15', 
                                     'query': 'R:EQNR.OL and Language:LEN',
                                     'dateFrom':'2018-08-21T00:00:00',
                                     'dateTo':'2018-09-21T12:00:00',
                                     'repository':'NewsRoom'
                                 }
                                )
