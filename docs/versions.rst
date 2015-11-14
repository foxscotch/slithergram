===============
Version History
===============

.. currentmodule:: slithergram

I'm going to *try* to use `Semantic Versioning`_, but who knows if it'll
work out. This is kinda small, so I normally wouldn't consider versioning all
that necessary, but given that it'll probably map pretty closely to the official
Telegram API, which definitely uses version numbers, I think I should probably
do the same, for dependency reasons.

.. _Semantic Versioning: http://semver.org/

.. contents::

.. _v-0-x-x:

-----
0.x.x
-----


.. _v-0-2-x:

0.2.x
=====


.. _v-0-2-2:

0.2.2
-----

- Change name of :py:attr:`bot.Bot.bot_id` to :py:attr:`bot.Bot.user_id`
- Change :py:meth:`__repr__` for both User and Bot from an instantiation-like
  format to "<user {id}>" and "<bot {id}>"
- Added a preliminary :py:meth:`bot.Bot.send_message` method
- Added non-functional definition of :py:func:`main.convert_json_to_objects`


.. _v-0-2-1:

0.2.1
-----

- Creation of :py:class:`main.TelegramBase`, which now contains the seralization
  methods
- Removed serialization methods from :py:class:`main.User` and made it inherit
  from :py:class:`main.TelegramBase`


.. _v-0-2-0:

0.2.0
-----

Big changes here! Especially in the overall layout of it. I've planned since the
beginning to have formal classes for all of the Telegram API types, but I hadn't
decided until now that they'll all inherit from a base class that contains the
simpler, more universal stuff, like the serialization functions.

For specificity:

- Removed serialization functions from :py:class:`bot.Bot`, stuck them in
  :py:class:`main.User` instead
- :py:class:`bot.Bot` now inherits from :py:class:`main.User`
- Moved :py:exc:`main.TelegramError` to its new home in
  :py:mod:`slithergram.main`


.. _v-0-1-x:

0.1.x
=====


.. _v-0-1-1:

0.1.1
-----

- Removed the capability to use :py:class:`str` objects for
  :py:meth:`bot.Bot.deserialize_from_bytes`. I realized it wouldn't work at all,
  because pickle is not JSON.


.. _v-0-1-0:

0.1.0
-----

- Changed names of :py:meth:`bot.Bot.serialize_to_string` and
  :py:meth:`bot.Bot.deserialize_from_string` to :py:meth:`bot.Bot.serialize_to_bytes`
  and :py:meth:`bot.Bot.deserialize_from_bytes`, respectively


.. _v-0-0-x:

0.0.x
=====


.. _v-0-0-3:

0.0.3
-----

- Removed Bot.base_url. I couldn't think of any situation where I'd need it
  again after the :py:meth:`bot.Bot.__init__` call, so I just hardcoded that into it


.. _v-0-0-2:

0.0.2
-----

- Fixed a bug with :py:meth:`bot.Bot.update_info`. It used the
  :py:attr:`bot.Bot.base_url` attribute rather than just :py:attr:`bot.Bot.url`, leading
  to it retrieving a plain web page, causing a :py:exc:`json.JSONDecodeError`


.. _v-0-0-1:

0.0.1
-----

- Replaced the messy contents of the else block in :py:meth:`bot.Bot.__init__`
  with a call to :py:meth:`bot.Bot.update_info`
- Added '.pkl' file extension to default filename for
  :py:meth:`bot.Bot.serialize_to_file`


.. _v-0-0-0:

0.0.0
-----

This is the first version. I'm not really *sure* if it's supposed to start with
all zeroes, but it gets the job done. Since there aren't any changes to list, I
might as well just make a quick description of what I made before starting this.

- :py:class:`bot.Bot` class in :py:mod:`slithergram.bot`
    - :py:meth:`bot.Bot.__init__`
    - :py:meth:`bot.Bot.__repr__`
    - :py:meth:`bot.Bot.__str__`
    - :py:meth:`bot.Bot.update_info` (:py:meth:`bot.Bot.__init__` should probably call this)
    - :py:meth:`bot.Bot.serlialize_to_string`
    - :py:meth:`bot.Bot.serlialize_to_file`
    - :py:meth:`bot.Bot.deserlialize_from_string`
    - :py:meth:`bot.Bot.deserlialize_from_file`
- :py:obj:`bot.example_bot` :py:class:`bot.Bot` instance in
  :py:mod:`slithergram.bot`, just an example. I'll probably get rid of it or
  comment it out or something.