from command import Command
from service import Service
from write_box.main import WriteBox
from write_box.settings import TOKEN

from telegram.ext import Updater

updater = Updater(TOKEN, use_context=True)

command = Command(updater)
service = Service(WriteBox)

command.add_command('midBook1', service.midBook1, 'Middle Book v1', 'Write a similar japan character to all box of Middle Book v1')
command.add_command('lstBook1', service.lstBook1, 'Last Book v1', 'Write a similar japan character to all box of Last Book v1')

updater.start_polling()
updater.idle()