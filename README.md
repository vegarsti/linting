# Intro to linting and code formatting

Etymology: Lint is the small dot of wool on your wool sweater. The process of removing it is linting!

Good communication is made a lot easier by consistent language. Similarly, programming in a project is made easier when all contributors and all code follow the same style. [PEP8](https://www.python.org/dev/peps/pep-0008/) is a style guide for Python. It lists many best practices and norms, or rules, which the Python "inventors" think we should follow. We don't necessarily need to follow exactly these, but we might want to use the same coding style. Getting used to different styles, and switching between these, is tiring. Some people on a given project might use a lot of comments, some use many empty lines between code blocks, others don't, etc.

Some examples of rules in PEP8, which probably many can agree are good practices to follow:

- indentation is not a multiple of four
- no newline at end of file
- do not use bare `except`
- too many blank lines (3)
- comparison to `None` should be `'if cond is None:'`

**In short, the reason we want to use linting is that it saves time!**

Noen argumenter for å bruke linting her: [How Python Linters Will Save Your Large Project](https://jeffknupp.com/blog/2016/12/09/how-python-linters-will-save-your-large-python-project/).

Some of the rules that PyCharm tells us about our code (with the squiggly lines) are PEP8 rules.

## Flake8

Flake8 is a code linter which enforces PEP8, meaning we can run it to analyze our code, and we get told what rules it breaks. Some of these rules are only stylistic others are about actual code logic, that is, errors. Examples (some from [here](http://flake8.pycqa.org/en/latest/user/error-codes.html)):

- line too long
- local variable `x` is assigned to but never used
- module imported but unused
- a break statement outside of a while or for loop
- redefinition of unused name from line N

### Installation

Install it systemwide, so make sure you're not in a virtual environment. In your terminal, first run `deactivate` to do this, and then install flake8 with `pip install flake8`.

### Flake8 in the terminal

We can run Flake8 on a file or a folder, and it tells us what we break in PEP8. We do this by

```
flake8 <path to file/folder>
```

You can overrule, or downright ignore, some rules in PEP8. You can also change the default value of some. Dette kan du gjøre ved å enten sende det inn som parameter i kommandoen eller lagre det i en config-fil. Hirarkiet som bestemmer hvilken verdi som blir satt er: 

1. Parameter i kommandoen 
2. Config-fil i prosjekt-mappen
3. Global config-fil

Config-filen må hete `.flake8` og vi foreslår som ligger i dette repoet som standard. 


### Flake8 in PyCharm

You can also run Flake8 through PyCharm:

1. Install Flake8 (see above)
2. Find where Flake8 is installed: `which flake8`
3. Preferences -> Tools -> External Tools -> + (add) `+`
4. Fill in like this: ![Imgur](https://i.imgur.com/Y8YMDQb.png)
  > *Name*: `Flake8 - file` (a single file) or `Flake8 - folder` (a folder)\
  > *Program*: _<result from step 2>_\
  > *Arguments*: `--max-line-length 120 $FileDir$/$FileName$` (a single file) or `--max-line-length 120 $FileDir$` (a folder)\
  > *Working directory*: `$ProjectFileDir$`
  
#### To use
1. Right click on a file or folder you want to run Flake8 on
2. Click on External tools -> Flake 8 - file / Flake 8 - folder
3. PEP8 violations will be listed in the terminal, and with clickable links to the offending code line


## Black

>[Black](https://github.com/ambv/black) is the uncompromising Python code formatter.

Black is a program we can run on code files, and it simply changes these files such that they enforce (some of the) rules from PEP8. The file is formatted by Black (_"blackened"_) by doing `black file` in the terminal.

One of the pros of using Black, from their Github page, is

>Black makes code review faster by producing the smallest diffs possible.

By consistently using Black on a project we will get small diffs,
so only what is "actually" changed will show up.

### Installation

Black requires Python 3.6. We want to install this systemwide, so make sure you're not in a virtual environment. In your terminal, first run `deactivate` to do this. On a Mac, in the terminal, do

```
brew install python3
pip3 install black
```

Not quite sure how do this in Ubuntu, ask Ruben.

### Exercise!

Run `black post-black.py`, and then `git diff post-black.py`, to see the differences in formatting.

### Black in PyCharm

Note that you need to have PyCharm Professional, not Community Edition.

1. Install Black (se over)
2. Locate Black with `which black` (`where black` on Windows)
3. Preferences -> Tools -> File Watchers -> + (add) `<custom>`
4. Fill in like here: ![settings](https://i.imgur.com/UsuFDXm.png)
5. Press OK -> Apply -> OK

(If not on a Mac you probably need to change `/usr/local/bin/black` to the result from 2.)

Now Black will format your file when you press Save!

### Git hooks

You can set up hooks on git to make Flake8 run to check if you are allowed to commit or push. It will stop you from pushing/commiting code with violations, which is nice since the CircleCI build might break, but this would take longer to noticed. You set up a git hook like this:

1. Copy the file `pre-commit` to `~/.git/hook-templates/pre-commit
```
mkdir ~/.git/hook-templates
cp pre-commmit ~/.git/hook-templates/pre-commit
```
2. Make the file executable: 
```
chmod +x ~/.git/hook-templates/pre-commit
```
3. Add the hook to all new and excisting projects: 
```
git config --global core.hooksPath  ~/.git/hook-templates
```