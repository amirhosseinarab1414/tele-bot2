import requests
import datetime


class BotHandler:
    def __init__(self,token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
        
    def get_updates(self,offset=0,timeout=30):
        method = 'getUpdates'
        params = {'timeout':timeout,'offset': offset}
        resp = requests.post(self.api_url + method , params)
        result_json = resp.json()['result']
        return result_json
    
    def send_message(self, chat_id, text):
        params = {'chat_id':chat_id,'text':text,'parse_mode':'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method , params)
        return resp
    
    
    
    def get_first_update(self):
        get_result = self.get_updates()
        
        
        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None
            
        return last_update
    
    
    
token = '1117059184:AAESFUyr8tZC1j6UvYwMuZnoS5Ut_zfuNzo'
magnito_bot = BotHandler(token)



def main():
    new_offset = 0
    print('hi, nowlaunching...')
    
    while True:
        all_updates=magnito_bot.get_updates(new_offset)
        
        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)
                first_update_id = current_update['update_id']
                if 'text' not in current_update['message']:
                    first_chat_text = 'New member'
                    
                else:
                    first_chat_text = current_update['message']['text']
                first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                    
                else:
                    first_chat_name = "unknown"
                    
                
            if first_chat_text == '/start':
                magnito_bot.send_message(first_chat_id, 'به ربات آزمون کانون مهدویت خوش آمدید،نام و شماره دانشجویی تان را وارد کرده و سپس از قسمت پایین 👇 [/]سوال مورد نظر خود را انتخاب کنید ' )
                new_offset = first_update_id + 1

            if first_chat_text == '/command1':
                magnito_bot.send_message(first_chat_id, 'سوال اول' )
                new_offset = first_update_id + 1
                
                
            if first_chat_text == '/command2':
                magnito_bot.send_message(first_chat_id, 'سوال دوم' )
                new_offset = first_update_id + 1
                
                
            if first_chat_text == '/command3':
                magnito_bot.send_message(first_chat_id, 'سوال سوم' )
                new_offset = first_update_id + 1
                
                
                
            if first_chat_text == '/command4':
                magnito_bot.send_message(first_chat_id, 'سوال چهارم' )
                new_offset = first_update_id + 1
                
                
                
                
            if first_chat_text == '/command5':
                magnito_bot.send_message(first_chat_id, 'سوال پنجم' )
                new_offset = first_update_id + 1
                
                
            
                
                
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()





























