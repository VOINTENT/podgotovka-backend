from sys import argv

from slack import WebClient
from slack.errors import SlackApiError


def send_message(slack_api_token: str,
                 channel_name: str,
                 author_name: str,
                 title_message: str,
                 text_message: str,
                 icon_emoji: str = ':bulat-in-zoom:',
                 color: str = '#36a64f'):
    try:
        WebClient(token=slack_api_token).chat_postMessage(
            channel=f'#{channel_name}',
            icon_emoji=f'{icon_emoji}',
            attachments=[
                {
                    "fallback": "Backend update",
                    "color": color,
                    "pretext": "Backend update!",
                    "author_name": author_name,
                    "title": title_message,
                    "text": text_message
                }
            ]
        )
    except SlackApiError as exc:
        print(f'Got an error: {exc}')


def is_message_hidden(message: str) -> bool:
    return '--hidden' in message


if __name__ == '__main__':
    if len(argv) != 7:
        raise TypeError('Wrong count of arguments')

    slack_api_token, channel_name, author_name, title_message, text_message, color = (argv[1], argv[2], argv[3],
                                                                                      argv[4], argv[5], argv[6])

    if not is_message_hidden(title_message):
        send_message(
            slack_api_token=slack_api_token,
            channel_name=channel_name,
            author_name=author_name,
            title_message=title_message,
            text_message=text_message,
            color=color
        )
