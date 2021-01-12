# curl -H "Accept: application/json" -H "X-Query-Key: YOUR_QUERY_KEY" "https://insights-api.newrelic.com/v1/accounts/YOUR_ACCOUNT_ID/query?nrql=YOUR_QUERY_STRING"

import sys

from nr_insights_api import InsightsAPI

if __name__ == '__main__':



    if (len(sys.argv) != 3):
        print("Usage: insights_query API_KEY RPM_ID")
        sys.exit(-1)

    api_key = sys.argv[1]
    rpm_id = sys.argv[2]

    insights_api = InsightsAPI(api_key, rpm_id)

    result = insights_api.query("SELECT latest(`python.metric`) FROM Metric SINCE 30 MINUTES AGO TIMESERIES")
#    result = insights_api.query("SELECT rate(count(*), 1 minute)  AS 'Average requests per minute' FROM  MobileRequest WHERE (appId = 730443407 OR appVersionId = 730443407) WHERE `requestDomain` = 'us1-prod.disco-api.com'  SINCE 7 days AGO LIMIT 1000 TIMESERIES")

    print(result)


