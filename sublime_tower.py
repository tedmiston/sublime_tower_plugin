"""
Open git repos from Sublime Text in Tower.

If you regularly open a shell to run `$ gittower .`, this is faster.
"""

import os.path
import subprocess

import sublime
import sublime_plugin


def is_in_repo(path):
    """
    Return true if current file is inside of a repo.
    """
    cmd = 'cd {} && git rev-parse --is-inside-work-tree'.format(path)
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT,
                                         shell=True, universal_newlines=True,
                                         timeout=2)
    except subprocess.CalledProcessError as e:
        pass
    return output.strip() == 'true'


def get_repo_root(path):
    """
    Determine the repo root directory from a nested path.
    """
    cmd = 'cd {} && git rev-parse --show-toplevel'.format(path)
    output = subprocess.check_output(cmd, shell=True, universal_newlines=True,
                                     timeout=2)
    return output.strip()


def open_in_tower(path):
    """
    Open a repo in Tower.app [0], launching it if not running.

    [0]: https://www.git-tower.com/
    """
    cmd = 'gittower {}'.format(path)
    subprocess.check_output(cmd, shell=True, timeout=5)


class TowerOpenCommand(sublime_plugin.TextCommand):
    """
    Open the repo of the currently viewed file in Tower.
    """

    def run(self, edit):
        """
        Sublime entrypoint.
        """
        current_file_path = self.view.file_name()
        current_dir = os.path.dirname(current_file_path)

        if is_in_repo(current_dir):
            path = get_repo_root(current_dir)
            open_in_tower(path)
        else:
            pass
