import requests
import pickle
import json


class TelegramError(Exception):
    pass


class Bot():
    base_url = 'https://api.telegram.org/bot'

    def __init__(self, api_key, no_initial_check=True, **kwargs):
        """
        Init function for Bot.

        Args:
            api_key: Your bot's API key.
            no_initial_check: Specifies that no bot info check should be made.
            **kwargs:
                bot_id: Bot ID
                first_name: Bot's name
                last_name: Bot's last name, optional
                username: Bot's username, optional
        """

        self.url = self.base_url + api_key + '/'
        self.api_key = api_key

        if no_initial_check:
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
            r = requests.get(self.base_url + 'getMe')
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

    def __repr__(self):
        """
        The repr function for Bot. It's not a perfect representation of the very
        same object. But it's descriptive enough.
        """
        return 'Bot(api_key="{0}", no_initial_check=False)'.format(self.api_key)

    def __str__(self):
        """
        The str function for Bot. It returns the first_name of the bot, and it's
        mostly just intended to be the name of the file for serialization.
        """
        return self.first_name

    def update_info(self):
        r = requests.get(self.base_url + 'getMe')
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

    def serialize_to_string(self):
        return pickle.dumps(self)

    def serialize_to_file(self, filename=None):
        if not filename:
            filename = self.__str__()
        pickle.dump(self, open(filename, 'wb+'))

    @staticmethod
    def deserialize_from_string(deserialization_string):
        return pickle.loads(deserialization_string)

    @staticmethod
    def deserialize_from_file(filename=None):
        return pickle.load(open(filename, 'rb'))


example_bot = Bot(api_key='123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11', bot_id=123, first_name='Example Bot')