import sublime, sublime_plugin, sys
from xml.dom.minidom import parseString

class BuildAntTargetCommand(sublime_plugin.TextCommand):

	def is_enabled(self):
		file_name = sublime.active_window().active_view().file_name()
		if not self._check_valid_file(file_name):
			return False

		return True


	def is_visible(self):
		file_name = sublime.active_window().active_view().file_name()
		if not self._check_valid_file(file_name):
			return False

		return True


	def run(self, edit):
		self.build_file = self.view.file_name()

		if not self._check_valid_file(self.build_file):
			return

		# TODO: Setup settings to be used for plugin, like verbose build output,
		# 		and other useful features (TBD)

		# Present target options in popup menu
		self.view.show_popup_menu(self.targets, self._target_select_callback)


	def _target_select_callback(self, index):
		if index > -1:
			target = self.targets[index]

			print("Selected target: " + target)

			build_system = "ant"

			if sys.platform.startswith("win32"):
				build_system = "ant.bat"

			command = {
				"cmd": [
					build_system,
					"-f",
					self.build_file,
					target
				]
			}

			try:
				self.view.window().run_command("exec", command)
			except Exception as ex:
				sublime.status_message("Error running ANT build: " + ex)


	def _get_targets_from_file(self, file):
		try:
			f = open(file)
		except Exception as ex:
			print("File " + file + " could not be opened.")
			return[]

		data = f.read()
		dom = parseString(data)

		targets = []
		dom_targets = dom.getElementsByTagName("target")

		for dom_target in dom_targets:
			target_name = dom_target.getAttributeNode("name").nodeValue
			targets.append(target_name)

		return targets


	def _check_valid_file(self, file_name):
		# Make sure a view file has been specified
		if not file_name:
			return False

		# If it's not an XML file, we don't care about it
		if not file_name.endswith(".xml"):
			return False

		# Find all the available targets in the file
		self.targets = self._get_targets_from_file(file_name)

		# Nothing to build, if not targets found.
		if not len(self.targets):
			return False

		return True
