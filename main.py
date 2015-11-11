"""
This is the main slithergram module. It contains most of the general stuff, like
the Telegram API types, the exception(s), and the base class.
"""

import requests
import pickle
import json


class TelegramError(Exception):
    pass


class TelegramBase:
    """
    This class includes methods that should be part of all Telegram-related
    objects.
    """

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
            filename = self.__str__() + '.pkl'
        pickle.dump(self, open(filename, 'wb+'))
        return filename

    @staticmethod
    def deserialize_from_bytes(deserialization_string):
        """
        Loads a pickle representation of an object from a bytes object.

        :param bytes deserialization_string: Bytes object to load from
        :return: The instance that was loaded
        :rtype: User
        """

        return pickle.loads(deserialization_string)

    @staticmethod
    def deserialize_from_file(filename):
        """
        Loads a pickle representation of an object from a file.

        :param str filename: Name of file to load from
        :return: The instance that was loaded
        :rtype: User
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
        self.first_name = first_name

        if last_name:
            self.last_name = last_name
        if username:
            self.username = username

    def __repr__(self):
        """
        The repr function for User. It's not a perfect representation of the
        very same object, but it's descriptive enough.
        """

        return 'User(user_id={0}, first_name{1})'.format(self.user_id,
                                                         self.first_name)

    def __str__(self):
        """
        The str function for User. It returns the first_name of the user, and
        it's mostly just intended to be the name of the file for serialization.
        Because first names don't have to be unique, it probably isn't a very
        good idea to use this in important contexts.
        """

        return self.first_name