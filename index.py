# Send-Text-Message

#### https://www.fast2sms.com

# Write the message here
message = 'This is my first message'

# Number where you want to send message
numbers = '9137826518'

# This Function send your message
def send_text_message(message, numbers):
    api_key = 'Enter your API Key here'
    sender_id = 'TXTIND'
    url = "https://www.fast2sms.com/dev/bulkV2"
    payload = f"sender_id={sender_id}&message={message}&route=v3&numbers={numbers}"
    # print(payload)
    headers = {
        'authorization': api_key,
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    
    return response.text

# Call the function
send_text_message(message, numbers)
