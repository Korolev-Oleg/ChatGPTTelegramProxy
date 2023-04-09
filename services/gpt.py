import openai

from db.models import User, Message
from loguru import logger


def init(api_key):
    openai.api_key = api_key


def build_gpt_chat_messages(user: User, question: str, no_context=False):
    if user.get_messages_count() and not no_context:
        messages = []
        for message in reversed(user.get_messages()):
            messages.append(dict(role='user', content=message.question))
            messages.append(dict(role='assistant', content=message.answer))
        return messages + [dict(role='user', content=question)]
    else:
        return [
            dict(role='user', content=question),
        ]


@logger.catch()
def get_response(user, question):
    logger.debug(build_gpt_chat_messages(user, question, no_context=True))
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=build_gpt_chat_messages(user, question, no_context=True),
    )
    answer = response.choices[0].message.content
    print(answer, response)
    user.create_message(question, answer)
    return answer
