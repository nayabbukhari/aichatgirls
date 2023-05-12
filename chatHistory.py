import os

CHAT_HISTORY_DIR = "chat_history"


def load_chat_history(user, character):
    file_path = f"{CHAT_HISTORY_DIR}/{user}_{character.name}.txt"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            chat_history = f.read()
    else:
        chat_history = ""
        
    if chat_history == "":
        chat_history = character.mes_example + character.first_mes
        
    return chat_history

def save_chat_history(user, bot_name, chat_history):
    os.makedirs(CHAT_HISTORY_DIR, exist_ok=True)
    file_path = f"{CHAT_HISTORY_DIR}/{user}_{bot_name}.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(chat_history)
        
def reset_chat_history(user, bot_name):
    save_chat_history(user, bot_name, "")
    
#nothing calls this yet
def add_to_chat_history(user, bot_name, message):
    chat_history = load_chat_history(user, bot_name)
    chat_history += f"{user}: {message}\n"
    save_chat_history(user, bot_name, chat_history)
        
def remove_last_response(user, character):
    chat_history = load_chat_history(user, character)
    last_response_start = chat_history.rfind(f"{character.name}: ")
    if last_response_start != -1:
        chat_history = chat_history[:last_response_start]
        save_chat_history(user, character.name, chat_history)