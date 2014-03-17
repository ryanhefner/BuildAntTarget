Build Ant Target
================

A [Sublime Text 2](http://www.sublimetext.com/2) and [3](http://www.sublimetext.com/3) plugin that allows you to...

**build _any_ target from _any_ valid ANT build file, regardless of its location in your project!**

---

Overview
--------

A super simple plugin that extends on Sublime Text's existing ANT build support,
by extending its flexibility, allowing you to build from any open ANT build file
in your project, not just a `build.xml` in the root of your project.

And, it lists the available targets in your build file, for quick target
selection and building.

Inspired by the work done on [SuperAnt](https://github.com/aphex/SuperAnt), but
developed with greater flexibility in mind, based on existing project structures.

Requirements
------------

- Make sure you have ANT installed on your machine.
	- https://ant.apache.org/manual/install.html
	- or via [Homebrew](http://brew.sh)
		- `brew update`
		`brew install ant`
- Make sure that your ANT install is linked to `/usr/local/ant` \(*\).
	- `sudo ln -s /usr/local/bin/ant /usr/local/ant`
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

- Use the keyboard shortcut, `command+alt+b`, on any opened ANT build file
- Select from a list of the available targets, via the popup menu
- Watch your build happen via the Build Results panel

Options
-------

_Coming soon..._


Footnotes
---------

* - This is the default location that the Sublime Text ANT build system uses.
	I was able to find this out thanks to this link [Sublime Text with SuperAnt path is not correct](http://superuser.com/questions/690282/sublime-text-with-superant-path-is-not-correct)

