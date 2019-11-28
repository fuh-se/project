from chalice import Chalice, Response
from urllib import request
import urllib.parse
import json



app = Chalice(app_name='get-a-cat')
app.debug = True

clientID = "708291774949.843032109105"
clientSecret = "da13b7129df5e0ca54e4a5b87f272432"



@app.route('/slack/authorizer',methods=['GET'])
def slack_authorizer():
    try:
        print('into authorizer component')
        event = app.current_request.raw_body.decode("utf-8")
        print('incomming_request: %s'%(event))
        message='authorization initiated.'
        response={'status':'success','message':'%s'%(message)}
        return Response(
        body=json.dumps(response),
        status_code= 200,
        )
    except Exception as e:
        error_msg ='error msg =%s'%(str(e))
        response={'status':'error','message':'%s'%(error_msg)}
        return Response(
        body=json.dumps(response),
        status_code= 500,
        )

def respond(code):
    data = urllib.parse.urlencode(
        (
            ("client_id", clientId),
            ("client_secret", clientSecret),
            ("code", code)
        )
    )
    request = urllib.request.Request(
        "https://slack.com/api/oauth.access",
        data=data,
        method="POST"
    )
    request.add_header(
        "Content-Type",
        "application/x-www-form-urlencoded"
    )
    urllib.request.urlopen(request).read()
    

  
  
    
   


    
    
    

                
    



