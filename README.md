<div align="center"><img src="https://cloud.githubusercontent.com/assets/630550/19619834/43c460dc-9835-11e6-8652-1c8fff91cf02.png" alt="GTM Logo" height="115" width="275"></div>
<div align="center">Git Time Metric</div>

### Sublime Text 3 Git Time Metrics (GTM) plug-in

#### Simple, seamless, lightweight time tracking for all your git projects

Git Time Metrics (GTM) is a tool to automatically track time spent reading and working on code that you store in a Git repository. By installing GTM and using supported plug-ins for your favorite editors, you can immediately realize better insight into how you are spending your time and on what files.

# Installation

Installing GTM is a two step process.  First, it's recommended you install the GTM executable that the plug-in integrates with and then install the Sublime 3 GTM plug-in.  Please submit an issue if you have any problems and/or questions.

1. Follow the [Getting Started](https://github.com/git-time-metric/gtm/blob/master/README.md) section to install the GTM executable for your operating system.
2. Install the plug-in via [Package Control](https://packagecontrol.io).

**Note** - to enable time tracking for a Git repository, you need to initialize it with `gtm init` otherwise it will be ignored by GTM. This is done via the command line.
```
> cd /path/to/your/project
> gtm init
```

Consult the [README](https://github.com/git-time-metric/gtm/blob/master/README.md) and [Wiki](https://github.com/git-time-metric/gtm/wiki) for more information.

# Features

### Status Bar

In the status bar see your total time spent for in-process work (uncommitted).

![](https://cloud.githubusercontent.com/assets/630550/19831548/21fef6c2-9dd2-11e6-9cf4-7510135eb94a.png)

This can be disabled by setting `gtm_status_bar: false` in gtm.sublime-settings.

**Note** - the time shown is based on the file's path and the Git repository it belongs to. You can have several files open that belong to different Git repositories. The status bar will display the time for the current file's Git repository.  Also keep in mind, a Git repository must be initialized for time tracking in order to track time.

### Command Line Interface

Use the command line to report on time logged for your commits.

Here are some examples of insights GTM can provide you.

##### $ gtm report -last-month

![](https://cloud.githubusercontent.com/assets/630550/21582250/8a03f9dc-d015-11e6-8f77-548ef7314bf7.png)

##### $ gtm report -last-month -format summary

![](https://cloud.githubusercontent.com/assets/630550/21582252/8f85b738-d015-11e6-8c70-beed7e7b3254.png)

##### $ gtm report -last-month -format timeline-hours

![](https://cloud.githubusercontent.com/assets/630550/21582253/91f6226e-d015-11e6-897c-6042111e6a6a.png)

GTM is automatic, seamless and lightweight.  There is no need to remember to start and stop timers.  It runs on occasion to capture activity triggered by your editor.  The time metrics are stored locally with the git repository as [Git notes](https://git-scm.com/docs/git-notes) and can be pushed to the remote repository.

# Support

To report a bug, please submit an issue on the [GitHub Page](https://github.com/git-time-metric/gtm-sublime3-plugin/issues)

Consult the [README](https://github.com/git-time-metric/gtm/blob/master/README.md) and [Wiki](https://github.com/git-time-metric/gtm/wiki) for more information.
