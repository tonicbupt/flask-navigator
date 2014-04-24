Flask-Navigation
================

Installation
------------

::

    $ pip install Flask-Navigator

Set Up
------

Just like the most of Flask extension::

    from flask import Flask
    from flask.ext.navigator import Navigation

    app = Flask(__name__)
    nav = Navigation(app)

Or use the app factory pattern::

    nav = Navigation()
    nav.init_app(app)

Create Navigation Bar
---------------------

::

    navbar_top = nav.Bar('top', [
        nav.Item('Home', 'index'),
        nav.Item('Latest News', 'news', {'page': 1}),
    ])

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/news/<int:page>')
    def news(page):
        return render_template('news.html', page=page)

The created navigation bars are accessible in any template with app context

.. code-block:: html+jinja

    <ul>
        {% for item in nav.top %}
        <li class="{{ 'current' if item.is_active else '' }}">
            <a href="{{ item.url }}">{{ item.label }}</a>
        </li>
        {% endfor %}
    </ul>

API
---

Extension Class
~~~~~~~~~~~~~~~

.. autoclass:: flask.ext.navigator.Navigation
   :members: init_app, Bar, Item, ItemReference

Internal Classes
~~~~~~~~~~~~~~~~

.. autoclass:: flask.ext.navigator.navbar.NavigationBar
   :members:

.. autoclass:: flask.ext.navigator.item.Item
   :members:

.. autoclass:: flask.ext.navigator.item.ItemCollection
   :members:
   :inherited-members:

Utilities
~~~~~~~~~

.. autofunction:: flask.ext.navigator.utils.freeze_dict

.. autoclass:: flask.ext.navigator.utils.BoundTypeProperty
   :members:
