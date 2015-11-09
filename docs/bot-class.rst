=========
Bot Class
=========

.. py:currentmodule:: slithergram.bot

.. autoclass:: Bot
   :members: __init__, update_info, serialize_to_bytes, serialize_to_file,
             deserialize_from_bytes, deserialize_from_file

   .. py:attribute:: url

      The URL to use for the API. It's "https://api.telegram.org/bot" + your API
      token + "/".