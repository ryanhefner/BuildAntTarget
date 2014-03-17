Build Ant Target
================

A [Sublime Text 2](http://www.sublimetext.com/2) and [3](http://www.sublimetext.com/3) plugin that allows you to...

**build an ant target from any valid ANT build file, regardless of its location in your project!**

---

Overview
--------

A super simple plugin that extends on Sublime Text's existing ANT build support,
but extends its flexibility by allowing you to build from any open ANT build file
in your project, not just a `build.xml` in the root of your project.

And, it lists the available targets in your build file, for quick selection.

Requirements
------------

- Make sure you have ANT installed on your machine.
	- https://ant.apache.org/manual/install.html
	- or via [Homebrew](http://brew.sh)
		- `brew update`
		`brew install ant`
- Make sure that your ANT install is linked to `/usr/local/ant`*.
	- `sudo ln -s /usr/local/bin/ant /usr/local/ant`
- That‘s it!

Installation
------------

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


Options
-------

Coming soon...


Footnotes
---------

* -  This is the default location that the Sublime Text ANT build system uses.
