import shlex
import sublime
import sublime_plugin
import time
import os

class GTM(sublime_plugin.EventListener):
    update_interval = 30
    last_update = 0.0
    last_path = None

    # TODO: prompt for location of GTM or use a configuration file?
    gtm_path = "/Users/mschenk/Projects/go/bin"

    def on_post_save_async(self, view):
        self.record(view, view.file_name())

    def on_modified_async(self, view):
        self.record(view, view.file_name())

    def on_selection_modified_async(self, view):
        self.record(view, view.file_name())

    def on_activated_async(self, view):
        self.record(view, view.file_name())

    def record(self, view, path):

        if path and (
            path != GTM.last_path or
            time.time() - GTM.last_update > GTM.update_interval ):

            GTM.last_update = time.time()
            GTM.last_path = path

            cmd = "{0}/gtm record {1}".format(GTM.gtm_path, path)
            view.window().run_command('exec', {'cmd': shlex.split(cmd)})
