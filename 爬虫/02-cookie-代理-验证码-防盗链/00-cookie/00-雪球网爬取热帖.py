import os
import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/97.0.4692.71 Safari/537.36',
    'Cookie': 'xq_a_token=1ce5d8004d990273892c085f2b8dc832edd23fde; xqat=1ce5d8004d990273892c085f2b8dc832edd23fde; xq_r_token=1085f78243dfbbacd4186e7b1f3d58d9632367e1; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY4OTAzNTY5NiwiY3RtIjoxNjg2NTM4MDc2ODEzLCJjaWQiOiJkOWQwbjRBWnVwIn0.BJx-PS85hb2UrLL1YkbQnqI--0YR_LEvPL9Ip3woGaZwG6nLh6h2Qe5npEMDM6nmg5rU3j6oWc9WlilOcnP5S-vN-uUSxeCNt0coO8KkNQxMQw2cMMB6ebPD-96sWhYSvh6hOOSVOIDri4AjcfDA2fu8h6UBZ-rsue4E5aqFMxO9nsZhxhWvSSNpNRnXjJs2Y-5pEDIKFNKuW3Z2DLS3hipzXJziTMjnVUIL6yRRG_Sj4ZeOxQybTNHKdtxdMfpAdzuxm7mRnE9Pl5tvQq38hjH2uPQC1hnJlL-06fVm5TCgEZd2MYhNkqpNTtkXyKlmN8tlm2gJDntHpi_9PyMCVw; u=551686538136345; device_id=eb583fe897379378b527f9de10acd45e; Hm_lvt_1db88642e346389874251b5a1eded6e3=1686538137; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1686538137'
}
url = 'https://xueqiu.com/statuses/hot/listV2.json'
param = {
    "since_id": "-1",
    "max_id": "502523",
    "size": "15",
}
response = requests.get(url=url,headers=headers,params=param)
data = response.json()
print(data)