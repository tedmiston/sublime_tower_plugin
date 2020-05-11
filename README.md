# Sublime Tower plugin

[![Maintainability](https://api.codeclimate.com/v1/badges/5ab9fa0d51db7ca94521/maintainability)](https://codeclimate.com/github/tedmiston/sublime_tower_plugin/maintainability)

Open git repos from Sublime Text 3 in [Tower](https://www.git-tower.com/).

![Demo video](https://raw.githubusercontent.com/wiki/tedmiston/sublime_tower_plugin/images/demo.gif)

## Install

(Recommended) Install via Package Control:

1. Open `Package Control: Install Package` and search for `Tower`.

(Alternative) Install via GitHub:

1. `Package Control: Add Repository` <https://github.com/tedmiston/sublime_tower_plugin>
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

In the command palette, you can run:

- `UnitTesting: Test Current Package`
- `UnitTesting: Test Current Package with Coverage`.

Note: To run the tests, the plugin must be installed as source.  You can do that by doing a `git clone` in `~/Library/Application\ Support/Sublime\ Text\ 3/Packages/`.

## Lint

Run:

    pycodestyle .
    flake8
