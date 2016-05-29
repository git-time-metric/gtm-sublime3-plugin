import shlex
import sublime
import sublime_plugin
import sys
import time
import os

def find_gtm(gtm):
    # Adapted from https://gist.github.com/4368898
    # Public domain code by anatoly techtonik <techtonik@gmail.com>
    # AKA Linux `which` and Windows `where`

    path = os.environ['PATH']
    extlist = ['']
    if sys.platform == 'win32':
        pathext = os.environ['PATHEXT'].lower().split(os.pathsep)
        (base, ext) = os.path.splitext(gtm)
        if ext.lower() not in pathext:
            extlist = pathext
    else:
        # add in the typical brew executable path
        path = path + ':/usr/local/bin:/usr/local/sbin'

    for ext in extlist:
        execname = gtm + ext
        if os.path.isfile(execname):
            return execname
        else:
            paths = path.split(os.pathsep)
            for p in paths:
                f = os.path.join(p, execname)
                if os.path.isfile(f):
                    return f

    return None

class GTM(sublime_plugin.EventListener):
    update_interval = 30
    last_update = 0.0
    last_path = None

    # TODO: how to handle if gtm not found?
    gtm_path = find_gtm('gtm')

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

            cmd = "{0} record {1}".format(GTM.gtm_path, path)
            view.window().run_command('exec', {'cmd': shlex.split(cmd)})
