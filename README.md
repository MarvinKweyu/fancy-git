[![Bash Shell](https://badges.frapsoft.com/bash/v1/bash.png?v=103)](https://github.com/diogocavilha/fancy-git)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://github.com/diogocavilha/fancy-git/blob/master/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![made-with-bash](https://img.shields.io/badge/Made%20with-Bash-1f425f.svg)](https://www.gnu.org/software/bash/)
[![GitHub forks](https://img.shields.io/github/forks/diogocavilha/fancy-git.svg)](https://gitHub.com/diogocavilha/fancy-git/)
[![GitHub stars](https://img.shields.io/github/stars/diogocavilha/fancy-git.svg)](https://GitHub.com/diogocavilha/fancy-git/stargazers/)
[![GitHub contributors](https://img.shields.io/github/contributors/diogocavilha/fancy-git.svg)](https://gitHub.com/diogocavilha/fancy-git/graphs/contributors/)

![logo](https://github.com/diogocavilha/fancy-git/blob/master/images/logo.png)

That's a prompt changer to show a few cool git informations about your repository on terminal.
You can choose among predefined styles and enjoy all the aliases it provides you.

Feel free for contributing, pull requests and issues are always welcome! ;)
Know how to contribute [here](https://github.com/diogocavilha/fancy-git#contributing-rocket)

:bookmark: [You can check out the changelog here](https://github.com/diogocavilha/fancy-git/blob/master/CHANGELOG.md)

## Installing (Linux and MAC OS)
```sh
curl -sS https://raw.githubusercontent.com/diogocavilha/fancy-git/master/install.sh | sh
```

## Uninstalling (Linux and MAC OS)
```sh
curl -sS https://raw.githubusercontent.com/diogocavilha/fancy-git/master/uninstall.sh | sh
```

## After installing

1. Change your terminal font to "SourceCodePro+Powerline+Awesome+Regular". (It's necessary for rendering the icons properly)
2. Restart your terminal.

If you can't find the font, it's still possible to install it manually by running `fancygit configure-fonts` or even installing the ttf file placed at `~/.fancy-git/fonts/SourceCodePro+Powerline+Awesome+Regular.ttf`.

## Git suggested colors

You can type the command `fancygit --colors` to check out the color scheme config. This command will just show you an output like the example below:

```bash
git config --global color.ui true

git config --global color.diff.meta "yellow bold"
git config --global color.diff.old "red bold"
git config --global color.diff.new "green bold"
git config --global color.status.added "green bold"
git config --global color.status.changed "yellow"
git config --global color.status.untracked "cyan"
```

Just type `fancygit --colors-set` if you want to apply that color scheme config.

I suggest you to use this scheme color because fancygit will paint the background branch or showing icon colors, most of the time, according to the current repo status.
You can run the command: `fancygit --colors` in order to see those suggested colors.

You can always run a `fancygit --help` to check out the possibilities ;)

## Overview

As a picture is worth a thousand words...

![001](https://github.com/diogocavilha/fancy-git/blob/master/images/default_001.png)
![002](https://github.com/diogocavilha/fancy-git/blob/master/images/default_002.png)
![003](https://github.com/diogocavilha/fancy-git/blob/master/images/default_003.png)
![004](https://github.com/diogocavilha/fancy-git/blob/master/images/default_004.png)
![005](https://github.com/diogocavilha/fancy-git/blob/master/images/default_005.png)
![006](https://github.com/diogocavilha/fancy-git/blob/master/images/default_006.png)
![007](https://github.com/diogocavilha/fancy-git/blob/master/images/default_007.png)

## Working on a Python virtual environment?

![python_venv](https://github.com/diogocavilha/fancy-git/blob/master/images/python_venv.png)

> You can type `fancygit -h` or `fancygit --help` for more information.

## Styles :art:

If you don't want to be too "fancy" (as I don't), you can choose using the **simple style**.
In order to change to the **simple style** you can type `fancygit simple`. And if you want to return to the **default style** (colored), you can type `fancygit default`.

There are a bit of styles you can choose from. Here you have a list of available styles and their corresponding command.

> You can type `fancygit -h` or `fancygit --help` for more information.

`fancygit simple`
![Simple](https://github.com/diogocavilha/fancy-git/blob/master/images/styles/simple.png)

`fancygit simple-double-line`
![Simple Double Line](https://github.com/diogocavilha/fancy-git/blob/master/images/styles/simple-double-line.png)

`fancygit human`
![Human](https://github.com/diogocavilha/fancy-git/blob/master/images/styles/human.png)

`fancygit human-dark`
![Human Dark](https://github.com/diogocavilha/fancy-git/blob/master/images/styles/human-dark.png)

`fancygit default`
![Default](https://github.com/diogocavilha/fancy-git/blob/master/images/styles/default.png)

`fancygit double-line`
![Double Line](https://github.com/diogocavilha/fancy-git/blob/master/images/styles/double-line.png)

`fancygit dark`
![Dark](https://github.com/diogocavilha/fancy-git/blob/master/images/styles/dark.png)

`fancygit dark-double-line`
![Dark Double Line](https://github.com/diogocavilha/fancy-git/blob/master/images/styles/dark-double-line.png)

`fancygit light`
![Light](https://github.com/diogocavilha/fancy-git/blob/master/images/styles/light.png)

`fancygit light-double-line`
![Light Double Line](https://github.com/diogocavilha/fancy-git/blob/master/images/styles/light-double-line.png)

## Commands

| Command                     | Description
| --------------------------- | ---------------------------------------------------------
| fancygit -h, --help         | Show this help.
| fancygit -v, --version      | Show the fancygit version.
| fancygit update             | Update fancygit code with the latest release from github.
| fancygit configure-fonts    | Install font in order to render icons properly. This font is good if you are using some of these styles: `default`, `double-line`, `dark`, `dark-double-line`, `light`, `light-double-line`.
| fancygit --colors           | Show suggested colors config in an easy way to copy and paste to apply them.
| fancygit --colors-set       | Apply the suggested colors configuration.
| fancygit simple             | Change prompt to the simple style.
| fancygit simple-double-line | Change prompt to the simple style in double line.
| fancygit default            | Change prompt to the default (colored) style. (This is the fallback style).
| fancygit double-line        | Change prompt to the default (colored) style in double line.
| fancygit human              | Change prompt to the human readable style.
| fancygit human-dark         | Change prompt to the human readable style.
| fancygit dark               | Change prompt to the dark style.
| fancygit dark-double-line   | Change prompt to the dark style in double line.
| fancygit light              | Change prompt to the light style.
| fancygit light-double-line  | Change prompt to the light style in double line.

## Aliases

Here we got a list of useful aliases you can use when working. They seem to be not that interesting, but believe me, after getting used to them, your productivity will increase considerably when working with git repos.
For example, what if you could replace `git push origin <branch-name>` for `gpsob`? Much smaller command, isn't it?. That's is possible but what, for goodness sake, means `gpsob`?

Well, here goes a little explanation:

`gps + o + b`

`gps` = `git push`

`o` = `origin`

`b` = `<current-branch-name>`... Yes, it will get the branch you're working on.

Basically, most of the Fancy Git aliases work this way.

| Alias                    | Command                                                                                                                                                | Description
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------
| gs                         | git status                                                                                                                                             | Show git status.
| ga \<file\> [<other_file>] | Add files in order to commit. [file](https://github.com/diogocavilha/fancy-git/blob/master/alias_functions/ga.sh)                                      | Add a file in order to commit.
| gap \<file\>               | Add part of a files in order to commit.                                                                                                                | Add a file in order to commit.
| gaa                        | Add all files in order to commit. [file](https://github.com/diogocavilha/fancy-git/blob/master/alias_functions/gaa.sh)                                 | Add all files in order to commit.
| gd                         | Show changes of a file and suggests to add it. [file](https://github.com/diogocavilha/fancy-git/blob/master/alias_functions/gd.sh)                     | Clear screen and git diff
| gcm                        | git commit                                                                                                                                             | Start committing.
| gcmm "\<message\>"         | git commit -m "\<message\>"                                                                                                                            | Start committing with a message.
| gpl                        | git pull. [file](https://github.com/diogocavilha/fancy-git/blob/master/alias_functions/gpl.sh)                                                         | Git pull.
| gps                        | git push                                                                                                                                               | Git push.
| gplo \<branch-name\>       | git pull origin \<branch-name\> [file](https://github.com/diogocavilha/fancy-git/blob/master/alias_functions/gplo.sh)                                  | Git pull from \<branch-name\> to current local branch.
| gpso \<branch-name\>       | git push origin \<branch-name\>                                                                                                                        | Git push from current local branch to \<branch-name\>.
| gplob                      | Git pull from remote current branch to local current branch. [file](https://github.com/diogocavilha/fancy-git/blob/master/alias_functions/gplob.sh)    | Git pull from remote branch to local branch.
| gpsob                      | Git push from local current branch to remote current branch. [file](https://github.com/diogocavilha/fancy-git/blob/master/alias_functions/gpsob.sh)    | Git push from local branch to remote branch.
| gck \<file\> ...           | git checkout -- \<file\> [file](https://github.com/diogocavilha/fancy-git/blob/master/alias_functions/gck.sh)                                          | Rollback file changes.
| gckb \<branch-name\>       | git checkout \<branch-name\>                                                                                                                           | Switch to a branch.
| gckbt \<branch-name\>      | Switch to a branch with --track option. [file](https://github.com/diogocavilha/fancy-git/blob/master/alias_functions/gckbt.sh)                         | Switch to a branch with --track option.
| gcb \<branch-name\>        | git checkout -b \<branch-name\>                                                                                                                        | Create and switch to the new branch.
| gdb \<branch-name\>        | git branch -D \<branch-name\>                                                                                                                          | Delete a local branch.
| gdbr \<branch-name\>       | git push origin --delete \<branch-name\>                                                                                                               | Delete a remote branch.
| grb \<new-branch-name\>    | Rename a local branch. [file](https://github.com/diogocavilha/fancy-git/blob/master/alias_functions/grb.sh)                                            | Rename current branch (local).
| grba \<new-branch-name\>   | Rename a branch (local and remote). [file](https://github.com/diogocavilha/fancy-git/blob/master/alias_functions/grba.sh)                              | Rename current branch (local and remote).
| gl                         | git log                                                                                                                                                | Show git log.
| glp                        | Show pretty git log. [file](https://github.com/diogocavilha/fancy-git/blob/master/alias_functions/glp.sh)                                              | Show pretty git log.
| gdof                       | find . -name "*.orig" \| xargs rm -rf                                                                                                                  | Remove all .orig files from project.
| gfi \<file\>               | git update-index --assume-unchanged \<file\>                                                                                                           | Force git to ignore a file.
| gurl                       | Show git repository URL. [file](https://github.com/diogocavilha/fancy-git/blob/master/alias_functions/gurl.sh)                                         | Show git repository URL.
| guser                      | Show git user information. [file](https://github.com/diogocavilha/fancy-git/blob/master/alias_functions/guser.sh)                                      | Show git user information.
| gst                        | git stash                                                                                                                                              | Create new stash with default message.
| gstl                       | git stash list                                                                                                                                         | List all stashes.
| gstm                       | git stash save "\<message\>"                                                                                                                           | Create new stash with custom message.
| gstw                       | git stash show \<stash_id\> [file](https://github.com/diogocavilha/fancy-git/blob/master/alias_functions/gstw.sh)                                      | Show stash diffs.
| gsta                       | git stash apply \<stash_id\> [file](https://github.com/diogocavilha/fancy-git/blob/master/alias_functions/gsta.sh)                                     | Apply stash.
| gstd                       | git stash drop \<stash_id\> [file](https://github.com/diogocavilha/fancy-git/blob/master/alias_functions/gstd.sh)                                      | Drop specific stash.
| gg "\<message\>"           | git add --all && git commit -m "\<message\>" && git push [file](https://github.com/diogocavilha/fancy-git/blob/master/alias_functions/gg.sh)           | Add all changes, then commit and push them.
| gu \<file\> [<other_file>] | git reset HEAD \<file\>                                                                                                                                | Remove files from staging area.
| pve                       | [file](https://github.com/diogocavilha/fancy-git/blob/master/alias_functions/pve.sh)                                                                  | Show the current Python virtual environment name.

## Troubleshooting :pick:

Maybe you could face an [issue](https://bugs.kde.org/show_bug.cgi?id=272443) related to icons rendering when using `Konsole` on version `18.12.1`.
An idea here is to update the `Konsole` to its latest version. So the problem might be solved ;)

# Contributing :rocket:

- Give this project a star =D
- Fork the project.
- Create a branch in order to implement your changes. (`git checkout -b your-branch-name`).
- Send a Pull Request.

---

*If you have any problem on setting up the fancy-git, contact me at [diogocavilha@gmail.com](mailto:diogocavilha@gmail.com) or simply create an issue [here](https://github.com/diogocavilha/fancy-git/issues). I'll be happy to help you.*

[![Donate_with_PayPal](https://github.com/diogocavilha/fancy-git/blob/master/images/buymeacoffee.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=QFCN8W7PRX696&lc=BR&item_name=diogocavilha%2fFancyGit&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_SM%2egif%3aNonHosted)
