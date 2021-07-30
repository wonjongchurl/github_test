import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2328967028851-2325750287413-EZG01snsLo0Dm5OTxSwW1pmA"
 
post_message(myToken,"#stock","ssssssssssssss")
