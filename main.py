"""
This is the main slithergram module. It contains most of the general stuff, like
the Telegram API types, the exception(s), and the base class.
"""

import requests
import pickle
import json


def convert_json_to_objects(json_string):
    """
    Converts a JSON string from the API to a collection of objects that
    correspond to the classes defined in this module.

    (It's not implemented yet)

    :param str json_string: JSON string
    :return: Collection of objects
    :rtype: dict
    """

    pass


class TelegramError(Exception):
    pass


class TelegramBase:
    """
    This class includes methods that should be part of all Telegram-related
    objects.
    """
    
    _default_filename = 'Telegram_serialization'

    def serialize_to_bytes(self):
        """
        Creates and returns a pickle string representation of the instance.

        :return: Pickle serialization string
        :rtype: bytes
        """

        return pickle.dumps(self)

    def serialize_to_file(self, filename=None):
        """
        Creates and saves a pickle file for the instance. By default, it uses
        "first_name.pkl" as the file name, where first_name is the object's real
        first_name attribute. Then it returns the file name.

        :param str filename: File name you want to save as
        :return: File name it was saved as
        :rtype: str
        """

        if not filename:
            filename = self._default_filename + '.pkl'
        pickle.dump(self, open(filename, 'wb+'))
        return filename

    @staticmethod
    def deserialize_from_bytes(deserialization_string):
        """
        Loads a pickle representation of an object from a bytes object.

        :param bytes deserialization_string: Bytes object to load from
        :return: The instance that was
        """

        return pickle.loads(deserialization_string)

    @staticmethod
    def deserialize_from_file(filename):
        """
        Loads a pickle representation of an object from a file.

        :param str filename: Name of file to load from
        :return: The instance that was loaded
        """

        return pickle.load(open(filename, 'rb'))


class User(TelegramBase):
    """
    Class for the Telegram API User type.

    :param int user_id: User's ID
    :param str first_name: User's first name
    :param str last_name: User's last name, optional
    :param str username: User's username, optional
    """

    def __init__(self, user_id, first_name, last_name=None, username=None):

        self.user_id = user_id
        """The user's user ID."""

        self.first_name = first_name
        """The user's first name."""

        if last_name:
            self.last_name = last_name
            """The user's last name"""

        if username:
            self.username = username
            """The user's username."""
        
        self._default_filename = self.first_name

    def __repr__(self):
        """
        The repr function for User. It's not a perfect representation of the
        very same object, but it's descriptive enough.
        """

        return '<user {0}>'.format(self.user_id)

    def __str__(self):
        """
        The str function for User. It returns the first_name of the user, and
        it was originally intended to be the name of the file for serialization.
        Because first names don't have to be unique, it probably isn't a very
        good idea to use this in important contexts.
        """

        return self.first_name


class Chat(TelegramBase):
    pass


class Message(TelegramBase):
    pass


class PhotoSize(TelegramBase):
    pass


class Audio(TelegramBase):
    pass


class Document(TelegramBase):
    pass


class Sticker(TelegramBase):
    pass


class Video(TelegramBase):
    pass


class Voice(TelegramBase):
    pass


class Contact(TelegramBase):
    pass


class Location(TelegramBase):
    pass


class Update(TelegramBase):
    pass


class InputFile(TelegramBase):
    pass


class UserProfilePhotos(TelegramBase):
    pass


class ReplyKeyboardMarkup(TelegramBase):
    """
    Class for defining a custom keyboard.

    :param list keyboard: Custom keyboard to use
    """
    def __init__(self, keyboard=None, **kwargs):
        presets = {
            'four_choices': [
                ['A', 'B'],
                ['C', 'D']
            ],
            'calculator': [
                [['7'], ['8'], ['9'], ['*']],
                [['4'], ['5'], ['6'], ['/']],
                [['1'], ['2'], ['3'], ['-']],
                [['0'], ['.'], ['='], ['+']]
            ]
        }

        if keyboard:
            self.keyboard = keyboard

        if 'resize_keyboard' in kwargs and kwargs['resize_keyboard']:
            self.resize_keyboard = kwargs['resize_keyboard']
        else:
            self.resize_keyboard = False

        if 'one_time_keyboard' in kwargs and kwargs['one_time_keyboard']:
            self.one_time_keyboard = kwargs['one_time_keyboard']
        else:
            self.one_time_keyboard = False

        if 'selective' in kwargs and kwargs['selective']:
            self.selective = kwargs['selective']
        else:
            self.selective = False

        if 'preset' in kwargs:
            try:
                self.keyboard = presets[kwargs['preset']]
            except KeyError:
                raise ValueError('You chose an invalid preset')

        if 'keyboard' not in self.__dict__:
            raise ValueError('Must have a keyboard')

    def as_dict(self):
        return self.__dict__


class ReplyKeyboardHide(TelegramBase):
    pass


class ForceReply(TelegramBase):
    pass


class File(TelegramBase):
    pass

