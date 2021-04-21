from telegram.ext import Updater, CommandHandler

class Command:
	def __init__(self, updater):
		self.list_command = {}
		self.updater = updater

	def remove_command(self, command):
		del self.list_command[command]
		self.updater.dispatcher.remove_handler(CommandHandler(command))

	def add_command(self, command, func, title, desc):
		self.list_command[command] = [title, desc]
		self.updater.dispatcher.add_handler(CommandHandler(command, func))

	def get_list_command(self):
		return self.list_command
