![GTM Logo](https://raw.githubusercontent.com/git-time-metric/gtm-atom-plugin/master/lib/GTMLogo-128.png)
# Sublime Text 3 Git Time Metrics (GTM) plug-in
### Simple, seamless, lightweight time tracking for all your git projects

Git Time Metrics (GTM) is a tool to automatically track time spent reading and working on code that you store in a Git repository. By installing GTM and using supported plug-ins for your favorite editors, you can immediately realize better insight into how you are spending your time and on what files.

# Installation

Installing GTM is a two step process.  First, it's recommended you install the GTM executable that the plug-in integrates with and then install the Sublime 3 GTM plug-in.  Please submit an issue if you have any problems and/or questions.

1. Follow the [Getting Started](https://github.com/git-time-metric/gtm/blob/master/README.md) section to install the GTM executable for your operating system.
2. Install the plug-in via [Package Control](https://packagecontrol.io).

# Features

### Status Bar

In the status bar see your total time spent for in-process work (uncommitted).

![](https://cloud.githubusercontent.com/assets/630550/16570803/e25a7980-4212-11e6-9e7a-a6eff4be118c.png)

This can be disabled by setting `gtm_status_bar: false` in gtm.sublime-settings.

*Note* - the time shown is based on the file's path and the Git repository it belongs to. You can have several files open that belong to different Git repositories. The status bar will display the time for the current file's Git repository.  Also keep in mind, a Git repository must be initialized for time tracking in order to track time.

Consult the [README](https://github.com/git-time-metric/gtm/blob/master/README.md) and [Wiki](https://github.com/git-time-metric/gtm/wiki) for more information.

### Command Line Inteface

Use the command line to report on time logged for your commits.

Here are some examples of insights GTM can provide you.

**Git commits with time spent**
```
> gtm report -total-only -n 3

9361c18 Rename packages
Sun Jun 19 09:56:40 2016 -0500 Michael Schenk  34m 30s

341bd77 Vagrant file for testing on Linux
Sun Jun 19 09:43:47 2016 -0500 Michael Schenk  1h 16m  0s

792ba19 Require a 40 char SHA commit hash
Thu Jun 16 22:28:45 2016 -0500 Michael Schenk  1h  1m  0s
```

**Git commits with detailed time spent by file**

```
> gtm report

b2d16c8 Refactor discovering of paths when recording events
Thu Jun 16 11:08:47 2016 -0500 Michael Schenk

       30m 18s  [m] event/event.go
       12m 31s  [m] event/manager.go
        3m 14s  [m] project/project.go
        1m 12s  [r] .git/COMMIT_EDITMSG
        1m  0s  [r] .git/index
           25s  [r] event/manager_test.go
           20s  [r] metric/manager.go
       49m  0s
```

**Timeline of time spent by day**

```
> gtm report -format timeline -n 3

           0123456789012345678901234
Fri Jun 24 *                              22m  0s
Sat Jun 25 **                          1h 28m  0s
Sun Jun 26 ****                        3h 28m  0s
Mon Jun 27 *                               4m  0s
Tue Jun 28 **                          1h 36m  0s
                                       6h 58m  0s
```

Consult the [README](https://github.com/git-time-metric/gtm/blob/master/README.md) and [Wiki](https://github.com/git-time-metric/gtm/wiki) for more information.
