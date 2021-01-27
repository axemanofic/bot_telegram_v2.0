#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telebot import types

import bot_handlers
import bot_callback
from config import TOKEN
from misc import bot
from flask import Flask, request
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)

@app.route('/{}'.format(TOKEN), methods=['POST'])
def index():
    bot.process_new_updates([types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "ok", 200


if __name__ == '__main__':
    app.run()
