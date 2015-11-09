===============
Version History
===============

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


.. _v-0-0-x:

0.0.x
=====


.. _v-0-0-2:

0.0.2
-----

- Fixed a bug with :py:meth:`Bot.update_info()`. It used the :py:attr:`base_url`
  attribute rather than just :py:attr:`url`, leading to it retrieving a plain
  web page, causing a :py:exc:`JSONDecodeError`


.. _v-0-0-1:

0.0.1
-----

- Replaced the messy contents of the else block in :py:meth:`Bot.__init__()`
  with a call to :py:meth:`Bot.update_info()`
- Added '.pkl' file extension to default filename for
  :py:meth:`Bot.serialize_to_file()`


.. _v-0-0-0:

0.0.0
-----

This is the first version. I'm not really *sure* if it's supposed to start with
all zeroes, but it gets the job done. Since there aren't any changes to list, I
might as well just make a quick description of what I made before starting this.

- :py:class:`Bot` class in :py:mod:`slithergram.bot`
    - :py:attr:`base_url`
    - :py:meth:`__init__()`
    - :py:meth:`__repr__()`
    - :py:meth:`__str__()`
    - :py:meth:`update_info()` (:py:meth:`__init__()` should probably call this)
    - :py:meth:`serlialize_to_string()`
    - :py:meth:`serlialize_to_file()`
    - :py:meth:`deserlialize_from_string()`
    - :py:meth:`deserlialize_from_file()`
- :py:obj:`example_bot` :py:class:`Bot` instance in :py:mod:`slithergram.bot`,
  just an example. I'll probably get rid of it or comment it out or something.