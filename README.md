Build Ant Target
================

A [Sublime Text 2](http://www.sublimetext.com/2) and [3](http://www.sublimetext.com/3) plugin that allows you to...

**build _any_ target from _any_ valid Ant build file, regardless of its location in your project!**

---

Overview
--------

A super simple plugin that extends Sublime Text's existing Ant build support,
by adding more flexibility, allowing you to build from any open build file
in your project, not just a `build.xml` in the root of your project.

It also allows you to select your desired target to build, for projects that have
more than one target defined.

Requirements
------------

- Make sure you have Ant installed on your machine.
	- https://ant.apache.org/manual/install.html
	- or via [Homebrew](http://brew.sh)
		- `brew update`
		- `brew install ant`
- Make sure that your Ant installation is linked to `/usr/local/ant` \(*\).
	- `sudo ln -s /usr/local/bin/ant /usr/local/ant`
		- NOTE: This assumes your existing Ant install is located at `/usr/local/bin/ant`.
		  You can figure out where you Ant is installed by running, `which ant`.
- That‘s it!

Installation
------------

**COMING SOON!** It is available through
[Sublime Package Contol](http://wbond.net/sublime_packages/package_control) and
this is the recommended way of installation (brings configuration instructions,
automatic updates with changelogs…).

### Alternative installation methods

#### From github

You can install from github if you want, although Package Control automates
just that. Go to your `Packages` subdirectory under Sublime Text's data directory:

##### Sublime Text 2

* Windows: `%APPDATA%\Sublime Text 2`
* OS X: `~/Library/Application Support/Sublime Text 2`
* Linux: `~/.config/sublime-text-2`
* Portable Installation: `Sublime Text 2/Data`

##### Sublime Text 3

* Windows: `%APPDATA%\Sublime Text 3`
* OS X: `~/Library/Application Support/Sublime Text 3`
* Linux: `~/.config/sublime-text-3`
* Portable Installation: `Sublime Text 3/Data`

#### Manually

[Download](https://github.com/ryanhefner/BuildAntTarget/archive/master.zip)
the plugin as a zip. Copy the *BuildAntTarget* directory to its location
(see prior section).

Usage
-----

## Build Target

There are two ways in which you can initiate the building of an Ant target, via
the Keyboard Shortcut or Context Menu.

**NOTE:** Both of these methods require that you initiate the command from an
opened, and valid, Ant build file.

### Keyboard Shortcut

- Use the keyboard shortcut, `command+alt+b`, on any opened Ant build file
- Select target via the popup menu
- Watch your build happen via the Build Results panel

### Context Menu

- Right-click on the opened build file
- Navigate to `Build Ant Target > Build Target`
- Select target via the popup menu
- Watch your build happen via the Build Results panel

Options
-------

_Coming soon..._


Footnotes
---------

* - This is the default location that the Sublime Text ANT build system uses.
	I was able to find this out thanks to this link [Sublime Text with SuperAnt path is not correct](http://superuser.com/questions/690282/sublime-text-with-superant-path-is-not-correct)

