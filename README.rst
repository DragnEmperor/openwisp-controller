WHOIS lookup and Fuzzy Location basic Implementation
====================================================
WHOIS details fetch and location creation is done as follows:

.. image:: https://github.com/DragnEmperor/openwisp-controller/blob/feature/whois-details/gif/Creation.gif
    :alt: Creation Process of Device with public last_ip

The change in last_ip is done by manually changing IP in FakeIPMiddleware:

.. image:: https://github.com/DragnEmperor/openwisp-controller/blob/feature/whois-details/gif/Updation.gif
    :alt: Update Process of Device with public last_ip

**The task that does the above processes can be found here : https://github.com/DragnEmperor/openwisp-controller/blob/feature/whois-details/openwisp_controller/config/tasks.py**

Added ip_middleware to ``MIDDLEWARE`` for simulating change in last_ip
----------------------------------------------------------------------

.. code-block:: python

    MIDDLEWARE = [
    'openwisp2.ip_middleware.FakeIPMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
  ]
  
**NOTE: Change IP in the middleware to simulate changes in last_ip of device**

**For a more complete overview of the OpenWISP modules and architecture**,
see the `OpenWISP Architecture Overview
<https://openwisp.io/docs/stable/general/architecture.html>`_.

.. image:: https://raw.githubusercontent.com/openwisp/openwisp2-docs/master/assets/design/openwisp-logo-black.svg
    :target: http://openwisp.org
    :alt: OpenWISP

Documentation
-------------

- `Usage documentation <https://openwisp.io/docs/stable/controller/>`_
- `Developer documentation
  <https://openwisp.io/docs/stable/controller/developer/>`_

Contributing
------------

Please refer to the `OpenWISP contributing guidelines
<http://openwisp.io/docs/developer/contributing.html>`_.

Changelog
---------

See `CHANGES
<https://github.com/openwisp/openwisp-controller/blob/master/CHANGES.rst>`_.

License
-------

See `LICENSE
<https://github.com/openwisp/openwisp-controller/blob/master/LICENSE>`_.

Support
-------

See `OpenWISP Support Channels <http://openwisp.org/support.html>`_.
