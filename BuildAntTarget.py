import sublime, sublime_plugin, sys, os
from xml.dom.minidom import parseString

class BuildAntTargetCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		self.build_file = self.view.file_name();

		# Make sure a view file has been specified
		if not self.build_file:
			return;

		# If it's not an XML file, we don't care about it
		if not self.build_file.endswith(".xml"):
			return;

		# Find all the available targets in the file
		self.targets = self._get_targets_from_file(self.build_file);

		# Nothing to build, if not targets found.
		if not len(self.targets):
			return;

		# Present target options in popup menu
		self.view.show_popup_menu(self.targets, self._target_select_callback);


	def _target_select_callback(self, index):
		if (index > -1):
			target = self.targets[index];

			print("Selected target: " + target);

			build_system = "ant";

			if sys.platform.startswith("win32"):
				build_system = "ant.bat";

			command = {
				"cmd": [
					build_system,
					"-f",
					self.build_file,
					target
				]
			};

			try:
				self.view.window().run_command("exec", command);
			except Exception as ex:
				sublime.status_message("Error running ANT build: " + ex);


	def _get_targets_from_file(self, file):
		try:
			f = open(file);
		except Exception as ex:
			print("File " + file + " could not be opened.");
			return[];

		data = f.read();
		dom = parseString(data);

		targets = [];
		dom_targets = dom.getElementsByTagName("target");

		for dom_target in dom_targets:
			target_name = dom_target.getAttributeNode("name").nodeValue;
			targets.append(target_name);

		return targets;
