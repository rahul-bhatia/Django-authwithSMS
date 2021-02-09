import requests
url = "https://www.fast2sms.com/dev/bulkV2"

querystring = {"authorization":"GZL7dOeVzH3rk6CBXh1Q2TtDsIjwa5cMyv08uoA9xSJFYiNpmqPA5fO8B4bk3yDShHRNvjsV1ounw9Xr","message":"This is test message","language":"english","route":"q","numbers":"7021106142"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)