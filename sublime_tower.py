"""
Open git repos from Sublime Text in Tower.

If you regularly open a shell to run `$ gittower .`, this is faster.
"""

import os.path
import subprocess

import sublime_plugin


def build_cmd_is_in_repo(path):
    return 'cd {} && git rev-parse --is-inside-work-tree'.format(path)


def build_cmd_get_repo_root(path):
    return 'cd {} && git rev-parse --show-toplevel'.format(path)


def build_cmd_open_in_tower(path):
    return 'gittower {}'.format(path)


def is_in_repo(path):
    """
    Return true if current file is inside of a repo.
    """
    cmd = build_cmd_is_in_repo(path)
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
    cmd = build_cmd_get_repo_root(path)
    output = subprocess.check_output(cmd, shell=True, universal_newlines=True,
                                     timeout=2)
    return output.strip()


def open_in_tower(path):
    """
    Open a repo in Tower.app [0], launching it if not running.

    [0]: https://www.git-tower.com/
    """
    cmd = build_cmd_open_in_tower(path)
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
