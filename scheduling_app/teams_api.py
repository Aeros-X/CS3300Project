# teams_api.py
import requests
from .teams_integration import get_access_token
from .models import Chat, Message

#This gets all of the chats if they exist
def get_chats(access_token):
    url = "https://graph.microsoft.com/v1.0/me/chats"

    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)
    chats = response.json().get('value')
    return chats

#This gets all of the chat messages based on the chat id
def get_chat_messages(chat_id, access_token):
    url = f"https://graph.microsoft.com/v1.0/me/chats/{chat_id}/messages"

    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)
    messages = response.json().get('value')
    return messages

#This saves the chats to the database
def save_chats_to_db():
    access_token = get_access_token('a3b437a6-6853-4685-9f2a-e616295684fe', 'Deq8Q~L5Fk6Q1aiC1-MJn..aFUE.sx_~mMdTydeQ', 'f8cdef31-a31e-4b4a-93e4-5f571e91255a')
    chats_data = get_chats(access_token)

    #Makes sure we have chats to pull from
    if chats_data:
        for chat_data in chats_data:
            chat_id = chat_data.get('id')

            #This just looks for if a chat is already made or not
            chat = Chat.objects.get_or_create(chat_id=chat_id)

            #This gets all of the messages, checks if already made or not, creates and links them if not
            messages_data = get_chat_messages(chat_id, access_token)
            for message_data in messages_data:
                message_id = message_data.get('id')
                content = message_data.get('body').get('content')

                #This specifically links it to the chat
                message = Message.objects.get_or_create(message_id=message_id, content=content)
                chat.messages.add(message)

            #Saves the chat and messages
            chat.save()

    return Chat.objects.all()