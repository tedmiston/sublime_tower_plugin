# Sublime Tower plugin

[![Maintainability](https://api.codeclimate.com/v1/badges/5ab9fa0d51db7ca94521/maintainability)](https://codeclimate.com/github/tedmiston/sublime_tower_plugin/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/5ab9fa0d51db7ca94521/test_coverage)](https://codeclimate.com/github/tedmiston/sublime_tower_plugin/test_coverage)

Open git repos from Sublime Text in [Tower](https://www.git-tower.com/).

Tested on both Tower 2 and Tower 3 (beta channel).

![Demo video](https://raw.githubusercontent.com/wiki/tedmiston/sublime_tower_plugin/images/demo.gif)

## Install

(Recommended) Install via Package Control:

1. Open `Package Control: Install Package` and search for `Tower`.

(Alternative) Install via GitHub:

1. `Package Control: Add Repository` https://github.com/tedmiston/sublime_tower_plugin
1. `Package Control: Install Package` sublime_tower_plugin

    Note: this requires installing updates manually via `Package Control: Upgrade Package`.

## Usage

Open `Command Palette` and type `Tower`.

## Development

Install the plugin source code:

	cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
	git clone https://github.com/tedmiston/sublime_tower_plugin.git

To debug in the Sublime console:

	view.run_command('tower_open')

## Test

This project uses the [SublimeText/UnitTesting](https://github.com/SublimeText/UnitTesting) test framework.

In the command palette, run `UnitTesting: Test Current Package` or `UnitTesting: Test Current Package with Coverage`.

## Lint

Run:

	pycodestyle .
	flake8
