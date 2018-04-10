# Sublime Tower plugin

[![Maintainability](https://api.codeclimate.com/v1/badges/eb0bffbeb2ec6b122823/maintainability)](https://codeclimate.com/github/tedmiston/sublime-tower-plugin/maintainability)

Open git repos from Sublime Text in [Tower](https://www.git-tower.com/).

![Demo video](https://raw.githubusercontent.com/wiki/tedmiston/sublime-tower-plugin/images/demo.gif)

## Install

Install via Package Control:

Open `Package Control: Install Package` and search for `Tower`.

## Usage

Open `Command Palette` and type `Tower`.

## Development

Install the plugin source code:

	cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
	git clone https://github.com/tedmiston/sublime-tower-plugin.git

To debug in the Sublime console:

	view.run_command('tower_open')

## Lint

Run:

	pycodestyle .
	flake8
