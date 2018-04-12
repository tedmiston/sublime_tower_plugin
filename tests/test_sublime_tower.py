import sys
import unittest

sublime_tower = sys.modules['sublime_tower_plugin.sublime_tower']


class SublimeTowerPluginTestCase(unittest.TestCase):

    def test_build_cmd_is_in_repo(self):
        actual = sublime_tower.build_cmd_is_in_repo('test_dir')
        expected = 'cd test_dir && git rev-parse --is-inside-work-tree'
        self.assertEqual(actual, expected)

    def test_build_cmd_get_repo_root(self):
        actual = sublime_tower.build_cmd_get_repo_root('test_dir')
        expected = 'cd test_dir && git rev-parse --show-toplevel'
        self.assertEqual(actual, expected)

    def test_build_cmd_open_in_tower(self):
        actual = sublime_tower.build_cmd_open_in_tower('test_dir')
        expected = 'gittower test_dir'
        self.assertEqual(actual, expected)
