Mass emailer
############

Python script to send email templates from a list of emails, a template and
replacement data for the templates.

This works as follows:

Create the templates
====================

Create the templates using the Jinja2 syntax. For instance::

    Hi {name}, you are receiving this email because you are {reason}.

    Thanks for all of what you are doing,
    Cheers,
    The team.

Create this file and let's say you name it ``body``. Create a second template
named ``subject`` with the subject of the email.

Create the list of emails + info
================================

Every format supported by `tablib <https://github.com/kennethreitz/tablib>`_
will work correctly.

For instance, let's say we have a json file with the following values, named
``dataset.json``::

  '[
     {"reason": "the one", "email": "toto@yopmail.com", "name": "Mr Toto"},
     {"reason": "right here, right now", "email": "alexis@yopmail.com", "name": "Alexis"}
   ]'

Run the script !
================

Once you've done that, just run the script::

  mass-email -t template-folder -d dataset.json


Or use it as a library
======================

You might prefer to use this software as a library, in this case, it would
look like this::

  import mass_emailer

  mass_emailer.send_emails(templates_folder="mail-template.tpl", dataset="dataset.json")
