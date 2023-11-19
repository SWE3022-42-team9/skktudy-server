import util.db as db
import psutil
from util.error_object import ErrorObject
from AI.src.chatbot import Chatbot

chatbots= {}

# /chatbot/send
def chatbot_send(uid: str, message: str, image: str | None) -> str | ErrorObject:
    # TODO: Implement
    # parameters:
    #   message: str
    #   image: str | None
    # returns:
    #   str | ErrorObject: response | ErrorObject
    
    # if invalid uid chatbot instance requested
    if uid not in chatbots:
        return ErrorObject(404, "Corresponding chatbot instances to uid not found")
    else:
        # else, call chatbot call
        response = chatbots[uid](messages=message)
        return response
    
# /chatbot/log
def chatbot_log(uid: str) -> dict | ErrorObject:
    # TODO: Implement
    # parameters:
    #   uid: str
    # returns:
    #   dict | ErrorObject: log | ErrorObject

    # check current memory usage by psutil
    memory_usage = psutil.virtual.memory().percent
    if memory_usage > 90:
        return ErrorObject(404, "Memory exceeded, cannot create new chatbot instances")

    # return type will be dict
    log = {}
    
    # if corresponding uid not exists, create new chatbot instance and append
    if uid not in chatbots:
        chatbots[uid] = Chatbot()
    else:
        # Get instance's memory buffer
        inst_memory = chatbots[uid].memory.buffer
        
        """
        log will be created as type
        e.g. log = {
            0: [{'human': 'Hello'}, {'ai': 'Hi, how are you?'}],
            1: [{'human': 'Who are you?'}, {'ai': 'I am a chatbot.'}]
        }
        """
        
        for i in range(0, len(inst_memory), 2):
            log[int(i/2)] = [
                {
                    inst_memory[i].type: inst_memory[i].content
                },
                {
                    inst_memory[i+1].type: inst_memory[i+1].content
                }
            ]
        
    return log