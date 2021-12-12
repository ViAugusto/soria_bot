from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from telegram.ext import Updater, MessageHandler, Filters
from spacy.cli import download
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram import Update
import logging
import os
download('en_core_web_sm')

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

soriabot = ChatBot('Soria', tagger_language=ENGSM)

updater = Updater(token=TOKEN, use_context=True)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
disparador = updater.dispatcher
updater.start_polling()

conversa = ['Oi',
    'qual seu nome?',
    'SoriaBot, e o seu?',
    'Kiro',
    'Nome bonito!',
    'Obrigado, igualmente',
    'hehe',
    '^^',
]
trainer = ListTrainer(soriabot)
trainer.train(conversa)

for arquivos in os.listdir('arquivos'):
    chats = open('arquivos/' + arquivos, 'r', encoding="utf8").readlines()
    trainer.train(chats)

def response(update: Update, context: CallbackContext):
    soriabot_response = soriabot.get_response(update.message.text)
    print(soriabot_response)
    print(type(soriabot_response))
    update.message.reply_text(str(soriabot_response))


def main():
    disparador.add_handler(MessageHandler(Filters.text, response))

if __name__ == '__main__':
    main()

