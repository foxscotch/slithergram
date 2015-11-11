import requests
import json

from .main import TelegramError, User


class Bot(User):
    """
    Class for controlling a Telegram bot.

    :param str api_key: api_key: Your bot's API key
    :param bool initial_check: Specifies whether an info check should be made
    :param int bot_id: Bot ID, optional if initial_check
    :param str first_name: Bot's name, optional if initial_check
    :param str last_name: Bot's last name, optional
    :param str username: Bot's username, optional
    """

    # noinspection PyMissingConstructor
    def __init__(self, api_key, initial_check=False, **kwargs):
        self.url = 'https://api.telegram.org/bot' + api_key + '/'
        self.api_key = api_key

        if not initial_check:
            bot_id = kwargs.get('bot_id')
            first_name = kwargs.get('first_name')
            last_name = kwargs.get('last_name')
            username = kwargs.get('username')

            if bot_id:
                self.bot_id = bot_id
            else:
                raise TypeError('Missing bot_id argument')

            if first_name:
                self.first_name = first_name
            else:
                raise TypeError('Missing first_name argument')

            if last_name:
                self.last_name = last_name

            if username:
                self.username = username

        else:
            self.update_info()

    def __repr__(self):
        return 'Bot(api_key="{0}", initial_check=True)'.format(self.api_key)

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
            result = json.loads(r.text)
            if result['ok']:
                bot_info = result['result']
                self.bot_id = bot_info['id']
                self.first_name = bot_info['first_name']
                if 'last_name' in bot_info:
                    self.last_name = bot_info['last_name']
                if 'username' in bot_info:
                    self.username = bot_info['username']
            else:
                raise TelegramError('The result was not "ok"')
        else:
            raise TelegramError('Did not get a 200 response', r.status_code)


example_bot = Bot(api_key='123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11',
                  bot_id=123456,
                  first_name='Example Bot')
