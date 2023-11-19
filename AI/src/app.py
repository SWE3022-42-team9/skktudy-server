import json
from pathlib import Path
from typing import List

from flask import Flask, request

from chatbot import Chatbot

FILE_SAVE_PATH = str(Path(__file__).parent.parent) + "/data/"


chatbots = {}

app = Flask(__name__)


# TODO: Add image decode method
@app.route("/chatbot/send", methods=["POST"])
def chatbot_send() -> str:
    """
    Main method for initializing the chatbot with uid, and sending requests to OPENAI API through the chatbot object and returning the response.

    Args:
        uid (`str`):
            The user id for the chatbot. This is used to keep track of the chatbot's memory and state independently for each user.
        message (`str`):
            The message to send to the chatbot. This is the message that the chatbot will respond to.
        files (`List[str]`, *optional*):
            Not yet implemented. This will be used to send files/images to the chatbot for QA, summarization, quiz generation, etc.


    Returns:
        response (`str`): The response from the chatbot.
    """

    if request.method == "POST":
        data = request.get_json()

        uid = data["uid"]
        message = data["message"]

        if uid not in chatbots:
            chatbots[uid] = Chatbot()

        response = chatbots[uid](messages=message, files=None)
        return response


@app.route("/chatbot/log", methods=["POST"])
def chatbot_log() -> dict[int, List[dict[str, str]]]:
    """
    Returns the chat history for the chatbot given the user id.

    Args:
        uid (`str`):
            The user id for the chatbot. This is used to return the chat history specific to the user.

    Returns:
        log (`dict[int, List[dict[str, str]]]`): The history of the chatbot's conversation with the user.

        e.g. log = {
        0: [{'human': 'Hello'}, {'ai': 'Hi, how are you?'}],
        1: [{'human': 'Who are you?'}, {'ai': 'I am a chatbot.'}]
        }
    """

    if request.method == "POST":
        data = request.get_json()

        uid = data["uid"]

        log = {}
        for i in range(0, len(chatbots[uid].memory.buffer), 2):
            log[int(i / 2)] = [
                {
                    chatbots[uid]
                    .memory.buffer[i]
                    .type: chatbots[uid]
                    .memory.buffer[i]
                    .content
                },
                {
                    chatbots[uid]
                    .memory.buffer[i + 1]
                    .type: chatbots[uid]
                    .memory.buffer[i + 1]
                    .content
                },
            ]

        # Wrap the log in a JSON object and encode it in UTF-8 for korean characters
        return json.dumps(log, ensure_ascii=False).encode("utf8")


@app.route("/chatbot/reset", methods=["POST"])
def chatbot_reset() -> None:
    """
    Resets the chatbot's memory and state given the user id.

    Args:
        uid (`str`):
            The user id for the chatbot. This is used to reset the chatbot's memory and state specific to the user.

    Returns:
        None
    """
    if request.method == "POST":
        data = request.get_json()

        uid = data["uid"]

        chatbots[uid].reset_session()

        return "Reset Success", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0")
