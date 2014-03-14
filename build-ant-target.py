import sublime, sublime_plugin
# from xml.dom.minidom import parse
# import xml.dom.minidom

class BuildAntTargetCommand(sublime_plugin.TextCommand):
	def onLoad(self, view):
		# fileName = view.fileName()

		# TODO(hi@ryanhefner.com): See if using the view.settings().get('syntax') would be better for this.
		# if not fileName.endsWith('.xml')
		# 	return

		# TODO(hi@ryanhefner.com): Confirm that the XML file is a valid ANT build file.

		# TODO(hi@ryanhefner.com): Loop through the document and make a list of the available actions
		# TODO(hi@ryanhefner.com): Store the targets in a global array for later use? 

		# print view.fileName(), 'just got loaded'
		return

	def onModified(self, view):
		# print view.fileName(), 'modified'
		return

	def run(self, edit):
		# TODO(hi@ryanhefner.com): Look into overriding ANT build call/keyboard shortcut
		
		# TODO(hi@ryanhefner.com): Present a popup menu with a list of available tasks/targets

		self.view.insert(edit, 0, "Hello, World!")
