# yorick: a project skeleton / template / boilerplate tool

*Yorick is a work in progress. Many of the features described here are not yet complete.* Currently, only the basics of the `construct` and `create-skeleton` commands work.

Whenever you start a programming project (or a book, or anything you do that involves files on a computer), you often end up doing the same initial steps, without much variation.

Yorick allows you to automate this by creating "skeletons" - templates that you can "construct" to create a boilerplate project. In the process of constructing, a skeleton can prompt the user for variables (project name, for instance), and have those variables substituted appropriately into the skeleton.

A collection of skeletons for different types of projects is called a "closet". Yorick automatically gives you a default closet to keep all of your own skeletons in, and the ability to add other people's closets alongside it. You can keep your closet to yourself or open it up to the world on GitHub (a bit like dotfiles).

## Installation

1. You need to have Python installed. (If you're not a Python programmer, don't worry, you can create and use yorick skeletons without writing a single line of Python.)
	- If you use Linux or OS X, you probably already have it. Run `python --version` to make sure it's version 2.7 - if not, upgrade.
2. Run `pip install yorick`. (If you don't have `pip`, run `easy_install pip` first.)

## Usage

### Constructing a project from a skeleton

Projects are constructed using the `yorick construct` command.

```
$ yorick construct example
Enter a name for your project.
project_name> spam
Constructing... Done.

$ find .
./spam/
./spam/__init__.py
./README.md

$ cat README.md
# spam

Insert a readme for spam here.
```

Instead of being prompted for variables interactively, you can specify them on the command line.

```
$ yorick construct example project_name=spam
Constructing... Done.
```

By default, skeletons are taken from the folder `~/.yorick/__default__/`, called the default closet. (So, the `example` skeleton would be at `~/.yorick/__default__/example/`.)

To construct a skeleton from a different closet, use the form `yorick construct <closet>.<skeleton-name>`. To construct a skeleton that is somewhere other than one of the closets in your `.yorick` directory, use the `-p` flag to specify a path to it, for example `yorick construct -p ~/blah/myskeleton`.

### Creating a skeleton

Use the `yorick create-skeleton` command to create a new skeleton.

```
$ yorick create-skeleton
Enter a name for your skeleton.
skeleton_name> eggs
Constructing... Done.
You can now edit your skeleton at ~/.yorick/__default__/eggs/
```

#### Configuration Files and Variables

Open the `config.yml` file in the `-yorick-meta` directory. Here, you'll see two entries:

- The `description`. Fairly self-explanatory.
- The `variables`. A list of variables that the user is prompted for when they construct a skeleton.

#### File names

When a skeleton is constructed, all of the files in the skeleton get processed.

- Files or folders that end in `.yorick-literal` have that text removed from their file name, and their file names aren't processed further.
- Files or folders that have a variable name surrounded by curly braces (e.g. `{name}.py`) have that variable substituted in (e.g. `my_awesome_project.py`).
- Files or folders that have doubled up curly braces (`{{` or `}}`) have them converted to single curly braces (`{` or `}`).
	- Note that having a single curly brace in a filename will cause an error, unless it is part of a variable substitution. So a file that should be output as `a{b.ext` *must* be named `a{{b.ext` in the template.
- Folders called `-yorick-meta` will be ignored, as this is the name of the folder that holds Yorick skeleton metadata.
	- If you need a `-yorick-meta` folder in your output (as the skeleton that builds Yorick skeletons does), use the `.yorick-literal` extension.
	
#### File Contents

### Installing somebody else's closet

Closets are shared as Git repositories or tarballs, and added with the `yorick install-closet` command. They can be updated with the `yorick update-closets` command.

```
$ yorick install-closet --git http://github.com/adambrenecki/yorick-closet abre
Waiting on VCS... Done.
You can now install a skeleton from this closet by running 'yorick construct abre.<skeleton-name>'

$ yorick update-closets
Updating abre... Done.
```

## To Do

- Pre- and post-construction scripts
	- In-skeleton
	- Global
	
## License

Copyright &copy; 2012 Adam Brenecki

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.