import os.path
import subprocess

import sublime
import sublime_plugin


def is_in_repo(path):
    cmd = 'cd {} && git rev-parse --is-inside-work-tree'.format(path)
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True, universal_newlines=True, timeout=2)
    except subprocess.CalledProcessError as e:
        pass
    return output.strip() == 'true'


def get_repo_root(path):
    cmd = 'cd {} && git rev-parse --show-toplevel'.format(path)
    output = subprocess.check_output(cmd, shell=True, universal_newlines=True, timeout=2)
    return output.strip()


def open_in_tower(path):
    cmd = 'gittower {}'.format(path)
    subprocess.check_output(cmd, shell=True, timeout=5)


class TowerOpenCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        current_file_path = self.view.file_name()
        current_dir = os.path.dirname(current_file_path)

        if is_in_repo(current_dir):
            path = get_repo_root(current_dir)
            open_in_tower(path)
        else:
            pass
