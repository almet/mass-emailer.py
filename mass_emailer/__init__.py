# -*- coding: utf-8 -*-
import argparse
import smtplib

from email.mime.text import MIMEText

from jinja2 import FileSystemLoader, Environment
from tablib import Dataset


def send_emails(templates_folder, dataset, server, sender, tls=False,
                username=None, password=None, email_field='email', cc=None):
    if cc is None:
        cc = []
    else:
        cc = [cc, ]

    records = Dataset().load(open(dataset).read(), format="tsv")

    simple_loader = FileSystemLoader(templates_folder)
    env = Environment(loader=simple_loader)
    subject_template = env.get_template("subject")
    body_template = env.get_template("body")

    # Connect to the server
    server = smtplib.SMTP(server)
    if tls:
        server.starttls()
    if username and password:
        server.login(username, password)

    # Now, for each record in the dataset, loop and send emails !
    for record in records.dict:
        to = record[email_field]
        text = body_template.render(**record)
        message = MIMEText(text, 'plain', 'UTF-8')
        message['Subject'] = subject_template.render(**record)
        message['From'] = sender
        message['To'] = to
        message['Cc'] = ", ".join(cc)
        server.sendmail(sender, cc + [to, ],  message.as_string())
    server.quit()


def main():
    parser = argparse.ArgumentParser(
        description='A tool to send multiple emails from a template')

    parser.add_argument('-t', '--templates', dest='templates_folder',
                        help='Path where to find the templates files.',
                        default='templates')

    parser.add_argument('-d', '--dataset', dest='dataset',
                        help='Location of the dataset file.',
                        default='dataset.json')

    parser.add_argument('-s', '--server', dest='server',
                        help='Server to send emails from.',
                        default='localhost:1025')

    parser.add_argument('-f', '--sender', dest='sender',
                        help='Email address you want to use as a sender.',
                        default='massmailer@yopmail.com')

    parser.add_argument('--tls', dest='tls', action='store_true',
                        default=False, help='Should connect using TLS.')

    parser.add_argument('-u', '--username', dest='username',
                        default=None, help='Username.')

    parser.add_argument('-p', '--password', dest='password',
                        default=None, help='Password.')

    parser.add_argument('-e', '--email-field', dest='email_field',
                        help='Field to use as an email field.',
                        default='email')

    parser.add_argument('--cc', dest='cc',
                        help='Address to put in cc.', default=None)

    args = parser.parse_args()
    send_emails(args.templates_folder, args.dataset, args.server, args.sender,
                args.tls, args.username, args.password,
                email_field=args.email_field, cc=args.cc)
