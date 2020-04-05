import requests
import json

import datetime
class API():
    def __init__(self):
        self.all_min = self.call_api('last_day')
        self.all_max = self.call_api('current_day')
        self.vietnam = self.call_api('vietnam')
        self.result = self.call_api('result')
    def call_api(self, country):
        payload = {}
        headers= {}        
        if country == "last_day":
            result = {
                'cases': 0,
                'deaths': 0,
                'recovered': 0
            }

            url = url = "https://corona.lmao.ninja/yesterday"
            response = requests.request("GET", url, headers=headers, data = payload)
            response_dict = json.loads(response.text)
            for i in response_dict:
                result['cases'] = str(int(i['cases']) + int(result['cases'])) 
                result['deaths'] = str(int(i['deaths']) + int(result['deaths'])) 
                result['recovered'] = str(int(i['recovered']) + int(result['recovered']))  

            return result        

        elif country == "current_day":
            url = "https://corona.lmao.ninja/all"
            response = requests.request("GET", url, headers=headers, data = payload)
            response_dict = json.loads(response.text)
            result = {
                'cases': response_dict['cases'],
                'deaths': response_dict['deaths'],
                'recovered': response_dict['recovered']
            }
            return result
        elif country == "vietnam":
            url = "https://corona.lmao.ninja/countries/vietnam"
            response = requests.request("GET", url, headers=headers, data = payload)
            response_dict = json.loads(response.text)
            result = {
                'cases': response_dict['cases'],
                'deaths': response_dict['deaths'],
                'recovered': response_dict['recovered'],
                'active': response_dict['active']
            }
            return result
        else:
            result = {
                'USA_cases': None,
                'USA_deaths': None,
                'Italy_cases': None,
                'Italy_deaths': None,
                'UK_cases': None,
                'UK_deaths': None,
                'Russia_cases': None,
                'Russia_deaths': None,
                'Spain_cases': None,
                'Spain_deaths': None,
                'China_cases': None,
                'China_deaths': None,
                'Korea_cases': None,
                'Korea_deaths': None,
                'France_cases': None,
                'France_deaths': None
            }        

            url = url = "https://corona.lmao.ninja/countries?sort=country"
            response = requests.request("GET", url, headers=headers, data = payload)
            response_dict = json.loads(response.text)
            for i in response_dict:
                if i['country']=='USA':
                    result['USA_cases'] = i['cases']
                    result['USA_deaths'] = i['deaths']
                if i['country']=='Italy':
                    result['Italy_cases'] = i['cases']
                    result['Italy_deaths'] = i['deaths']
                if i['country']=='China':
                    result['China_cases'] = i['cases']
                    result['China_deaths'] = i['deaths']
                if i['country']=='UK':
                    result['UK_cases'] = i['cases']
                    result['UK_deaths'] = i['deaths']
                if i['country']=='Russia':
                    result['Russia_cases'] = i['cases']
                    result['Russia_deaths'] = i['deaths']
                if i['country']=='France':
                    result['France_cases'] = i['cases']
                    result['France_deaths'] = i['deaths']
                if i['country']=='Spain':
                    result['Spain_cases'] = i['cases']
                    result['Spain_deaths'] = i['deaths']
                if i['country']=='S. Korea':
                    result['Korea_cases'] = i['cases']
                    result['Korea_deaths'] = i['deaths']
            return result

if __name__ == "__main__":
    api = API()
    api.call_api("dsada")
