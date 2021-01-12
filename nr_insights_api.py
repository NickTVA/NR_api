from urllib import parse

import requests
# curl -H "Accept: application/json" -H "X-Query-Key: YOUR_QUERY_KEY" "https://insights-api.newrelic.com/v1/accounts/YOUR_ACCOUNT_ID/query?nrql=YOUR_QUERY_STRING"


#implementation of a simple wrapper for New Relic partneership api
#https://docs.newrelic.com/docs/new-relic-partnerships/partnerships/partner-api/partner-api-reference

class InsightsAPI:


    BASE_URL = "https://insights-api.newrelic.com/v1/accounts/"



    def __init__(self, api_key, rpm_id):
        self.rpm_id = str(rpm_id)
        self.api_key = api_key
        self.insights_request_url = InsightsAPI.BASE_URL + self.rpm_id + "/query?nrql="
        self.header_data = {"X-Query-Key": self.api_key, "Content-Type": "application/json"}


    def query(self, nrql_string):
        url_safe_nrlq = parse.quote(nrql_string)
        insights_query_url = self.insights_request_url + url_safe_nrlq
        query_request = requests.get(insights_query_url, headers=self.header_data)

        return query_request.json()

