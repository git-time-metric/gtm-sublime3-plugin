import sublime
import sublime_plugin
import sys
import time
import os
import subprocess
import re

gtm_settings = {}

def find_gtm_path():
    if sys.platform == 'win32':
        exe = 'gtm.exe'
        path_sep = ";"
        pf = os.path.join(os.environ.get("ProgramFiles", ""), "gtm")
        pfx86 = os.path.join(os.environ.get("ProgramFiles(x86)", ""), "gtm")
        default_path = pf + path_sep + pfx86
    else:
        exe = 'gtm'
        path_sep = ":"
        default_path = "/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin/"

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

def plugin_loaded():
    global gtm_settings
    gtm_settings = sublime.load_settings('gtm.sublime-settings')
    gtm_settings.add_on_change('gtm_status_bar', set_status_bar)
    set_status_bar()

def set_status_bar():
    if gtm_settings.get('gtm_status_bar', True):
        GTM.status_option = '--status'
        print("Enabling reporting time in status bar")
    else:
        GTM.status_option = ''
        print("Disabling reporting time in status bar")

class GTM(sublime_plugin.EventListener):
    gtm_ver_req = '>= 1.0.0'

    update_interval = 30
    last_update = 0
    last_path = None
    status_option = ''

    no_gtm_err = ("GTM executable not found.\n\n"
                  "Install GTM and/or update your system path. "
                  "Make sure to restart Sublime after install.\n\n"
                  "See https://github.com/git-time-metric/gtm/blob/master/README.md")

    record_err = ("GTM error saving time.\n\n"
                  "Install GTM and/or update the system path. "
                  "Make sure to restart Sublime after install.\n\n"
                  "See https://github.com/git-time-metric/gtm/blob/master/README.md")

    ver_warn = ("GTM executable is out of date.\n\n"
                "The plug-in may not work properly. "
                "Please install the latest GTM version and restart Sublime.\n\n"
                "See https://github.com/git-time-metric/gtm/blob/master/README.md")

    gtm_path = find_gtm_path()

    if not gtm_path:
        sublime.error_message(no_gtm_err)
    else:
        p = subprocess.Popen('"{0}" verify "{1}"'.format(gtm_path, gtm_ver_req),
                             shell=True,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
        output = p.stdout.read()
        version_ok = 'true' in output.decode('utf-8')
        if not version_ok:
            sublime.error_message(ver_warn)

    def on_post_save_async(self, view):
        self.record(view, view.file_name())

    def on_modified_async(self, view):
        self.record(view, view.file_name())

    def on_selection_modified_async(self, view):
        self.record(view, view.file_name())

    def on_activated_async(self, view):
        self.record(view, view.file_name())

    def record(self, view, path):

        if GTM.gtm_path and path and (
            path != GTM.last_path or
            time.time() - GTM.last_update > GTM.update_interval ):

            GTM.last_update = time.time()
            GTM.last_path = path

            cmd = '"{0}" record {1} "{2}"'.format(GTM.gtm_path,
                                                GTM.status_option,
                                                path)

            try:
                cmd_output = subprocess.check_output(cmd, shell=True)
                if GTM.status_option:
                    view.set_status(
                        "gtm-statusbar",
                        GTM.format_status(cmd_output))
                else:
                    view.erase_status("gtm-statusbar")
            except subprocess.CalledProcessError as e:
                sublime.error_message(GTM.record_err)

    def format_status(t):
        s = t.decode('utf-8').strip()
        if s:
            s = ' '.join(re.sub("\\s*\\d*s\\s*", "", s).split())
        return "[ {0} ]".format(s)
