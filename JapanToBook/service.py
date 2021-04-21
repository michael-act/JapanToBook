from write_box.settings import IMAGES_PATH, LOGFILE_PATH
from command import Command

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

class Service:
    def __init__(self, Writer):
        self.Writer = Writer()


    def midBook1(self, update, context):
        self.update = update

        self.file = IMAGES_PATH
        self.text = context.args[0]

        valid = (1 <= len(self.text) <= 2)
        if valid:
            self.text += ' ' # Counter if the character only 1
            self.file += self.Writer.midBook1(self.text[0], self.text[1])
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(self.file, 'rb'), timeout=120)
            self.logging()

        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Sorry, the character only accepted 2 or 1!', timeout=120)


    def lstBook1(self, update, context):
        self.update = update

        self.file = IMAGES_PATH
        self.text = context.args[0]

        valid = (len(self.text) == 1)
        if valid:
            self.file += self.Writer.lstBook1(self.text)
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(self.file, 'rb'), timeout=120)
            self.logging()
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Sorry, the character only accepted is 1!', timeout=120)


    def logging(self):
        with open(LOGFILE_PATH, 'a', encoding="utf-8") as file:
            timestamp = self.file
            level = 'INFO'
            message = f'Got request from @{self.update.message.chat.username}'
            command = self.Writer.writer
            word = self.text

            full = f'{timestamp} - {level} - {message} - /{command} {word}'

            file.write(full)
            file.close()
