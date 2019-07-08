import requests

servercheck()

def servercheck():

    url = 'https://samplewebiste.com'
    
    req = requests.get(url)
    
    response=req.status_code
    
    print(response)
    
    if(response!=200):
        print("Not getting 200 response....")
    else:
        print("Server is getting 200 response....")
        
   
