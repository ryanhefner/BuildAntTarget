import sublime, sublime_plugin

class BuildAntTasksCommand(sublime_plugin.TextCommand):
	def onLoad(self, view):
		print view.filename(), 'just got loaded'

	def onModified(self, view):
		print view.filename(), 'just got modified'

	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World!")
