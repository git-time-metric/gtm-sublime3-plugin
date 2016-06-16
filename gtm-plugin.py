import sublime
import sublime_plugin
import sys
import time
import os
import subprocess

def find_gtm_path():
    if sys.platform == 'win32':
        exe = 'gtm.exe'
        default_path = ""
        path_sep = ";"
    else:
        exe = 'gtm'
        default_path = "/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin/"
        path_sep = ":"

    env_path = set(os.environ['PATH'].split(path_sep))
    paths = env_path.union(set(default_path.split(path_sep)))

    if os.path.isfile(exe):
        return exe
    else:
        for p in paths:
            f = os.path.join(p, exe)
            if os.path.isfile(f):
                return f

    return None

class GTM(sublime_plugin.EventListener):
    update_interval = 30
    last_update = 0.0
    last_path = None

    gtm_path = find_gtm_path()
    
    if not gtm_path:
       print("Unable to find the 'gtm' executable")
       print("Please makes sure it is installed and accesible via your path")

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

            cmd = '{0} record "{1}"'.format(GTM.gtm_path, path)
            return_code = subprocess.call(cmd, shell=True)

            if return_code != 0:
                print("Unable to run 'gtm' command")
                print("Please makes sure it is installed and accesible via your path")
