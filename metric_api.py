import json
import time

import requests

from NR_metric import NRMetricElement, Attributes, Metric
current_milli_time = lambda: int(round(time.time() * 1000))




if __name__ == '__main__':

    metrics_url = 'https://metric-api.newrelic.com/metric/v1'
    header_data = {"Api-Key": "NRII-xeynHqC-Tz23ySIygutYX8rv4wtm_R4h"}
    # data = '''[{
    #     "metrics":[{
    #        "name":"nick.testgauge",
    #        "type":"gauge",
    #        "value":4.5,
    #        "timestamp":1584569424296
    #        }]
    # }]'''

#    r = requests.post(metrics_url, data=data, headers=header_data)


    attributes = Attributes("nicktest", "localhost")
    metric = Metric("python.metric", "gauge", 10.0, current_milli_time(), attributes)
    elements = NRMetricElement([metric])


    send_bytes_string = json.dumps([elements.to_dict()])
    send_bytes = send_bytes_string.encode()
    r = requests.post(metrics_url, data=send_bytes, headers=header_data)


    print(r)

