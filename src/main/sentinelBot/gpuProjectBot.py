import requests

def botTelegramSendMessage(textMessage:str):

    botToken:str  = '5308865554:AAHI6UOyscNy1nyWZiaf5FRktP9oVwPb6Go'
    reciverChatId:str = '1562546603'
    botSendText:str = f'https://api.telegram.org/bot{botToken}/sendMessage?chat_id={reciverChatId}&parse_mode=Markdown&text={textMessage}'
    response:requests = requests.get(botSendText)

    return response.json()
