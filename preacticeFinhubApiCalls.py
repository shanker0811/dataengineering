import requests as req
finhub_api_key="d98v6k9r01qugfv10lagd98v6k9r01qugfv10lb0"
api_url="https://finnhub.io/api/v1/quote"
try :
    response=req.get(api_url,headers={"X-Finnhub-Token": finhub_api_key})
    if(response.status_code==200):
        data=response.json()
        print("Current Price:",data)
    else :
        raise req.exceptions.RequestException(f"API request failed with status code: {response.status_code}")
except req.exceptions.RequestException as e:
    print("Error occurred while making the API request:", e)

exchange="IND" 
current_price=0.0 
price=44

api_url=f"https://finnhub.io/api/v1/stock/market-status"
params={"exchange": exchange, "token": finhub_api_key}
try :
    response=req.get(api_url, params=params)
    if(response.status_code==200):
        data=response.json()
        print("Current Price:",data)
    else :
        raise req.exceptions.RequestException(f"API request failed with status code: {response.status_code}")
except req.exceptions.RequestException as e:
    print("Error occurred while making the API request:", e)

