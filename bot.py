"""
This is the Slithergram module for dealing with bots. It pretty much only has
the Bot class, but it may eventually include abstractions for some other API
features that are exclusive to bots.
"""

import requests
import json

from .main import TelegramError, User


class Bot(User):
    """
    Class for controlling a Telegram bot.

    :param str api_key: api_key: Your bot's API key
    :param bool initial_check: Specifies whether an info check should be made
    :param int user_id: Bot ID, optional if initial_check
    :param str first_name: Bot's name, optional if initial_check
    :param str last_name: Bot's last name, optional
    :param str username: Bot's username, optional
    """

    # noinspection PyMissingConstructor
    def __init__(self, api_key, initial_check=False, **kwargs):
        self.url = 'https://api.telegram.org/bot' + api_key + '/'
        """The API URL that the bot should use. Includes final slash, so you
        should only have to add the method name and parameters."""

        self.api_key = api_key
        """The bot's API key."""

        if not initial_check:
            user_id = kwargs.get('user_id')
            first_name = kwargs.get('first_name')
            last_name = kwargs.get('last_name')
            username = kwargs.get('username')

            if user_id:
                self.user_id = user_id
                """The bot's user ID."""
            else:
                raise TypeError('Missing user_id argument')

            if first_name:
                self.first_name = first_name
                """The bot's first name."""
            else:
                raise TypeError('Missing first_name argument')

            if last_name:
                self.last_name = last_name
                """The bot's last name."""

            if username:
                self.username = username
                """The bot's username."""

        else:
            self.update_info()
        
        self._default_filename = self.first_name

    def __repr__(self):
        return '<bot {0}>'.format(self.user_id)

    def update_info(self):
        """
        Updates the bot's info.

        It makes a request to the Telegram API method getMe for your bot. So, it
        can take a second, and you probably shouldn't use this in any situation
        where getting a result is time-sensitive (e.g. for a web application).

        This method is used in :py:meth:`__init__()` if initial_check is True.
        """

        r = requests.get(self.url + 'getMe')
        if r.status_code == 200:
            response = json.loads(r.text)
            if response['ok']:
                bot_info = response['result']
                self.user_id = bot_info['id']
                self.first_name = bot_info['first_name']
                if 'last_name' in bot_info:
                    self.last_name = bot_info['last_name']
                if 'username' in bot_info:
                    self.username = bot_info['username']
            else:
                raise TelegramError('The result was not "ok"')
        else:
            raise TelegramError('Did not get a 200 response', r.status_code)

    def send_message(self, chat, message, **kwargs):
        """
        Method that will be used to send messages as the bot.

        This is just a temporary version. The real version will be more complex.

        :param Chat chat: Chat you want to send the message in
        :param str message: Message that you want to send
        :param str parse_mode: Specify if you want message MD parsed, optional
        :param bool disable_web_page_preview: Disable link previews, optional
        :param int reply_to_message_id: Message ID you're replying to, optional
        :param ReplyKeyboardMarkup reply_markup: Keyboard markup object to use
        :return: The server's response
        :rtype: requests.models.Response
        """

        payload = {
            'chat_id': chat.chat_id,
            'text': message
        }

        if 'parse_mode' in kwargs:
            payload['parse_mode'] = 'Markdown'
        if 'disable_web_page_preview' in kwargs:
            payload['disable_web_page_preview'] = True
        if 'reply_to_message_id' in kwargs:
            payload['reply_to_message_id'] = kwargs['reply_to_message_id']
        if 'reply_markup' in kwargs:
            payload['reply_markup'] = kwargs['reply_markup'].as_dict()

        r = requests.post(self.url + 'sendMessage', json=json.dumps(payload))
        return r


example_bot = Bot(api_key='123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11',
                  user_id=123456,
                  first_name='Example Bot')
