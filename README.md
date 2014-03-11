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

These are just usage examples to show you what the command line interface looks like. If you want to dive in, check out the docs on [ReadTheDocs](https://yorick.readthedocs.org/).

### Create a new skeleton

```
$ yorick create-skeleton eggs
Constructing... Done.
You can now edit your skeleton at ~/.yorick/__default__/eggs/

$ my-favorite-editor ~/.yorick/__default__/eggs/
```

### Construct a project from a skeleton

```
$ yorick construct eggs
Enter a name for your project.
project_name> spam
Constructing... Done.

$ tree .
├── spam
│   └── __init__.py
└── README.md

$ cat README.md
# spam

Insert a readme for spam here.
```

### Share your skeletons with the world

```
$ cd ~/.yorick/__default__
$ git init .
$ git add .
$ git commit -m "Initial commit"
$ git origin add master https://github.com/joe/closet.git
$ git push -u origin master
```

### Install closets from other people...

```
$ yorick install-closet fred https://github.com/fred/closet.git
Closet cloned to ~/.yorick/fred/

$ yorick update-closet fred
Updating... fred was already up to date.
```

### ...and use their skeletons

```
$ yorick construct fred.more_eggs
Enter a name for your project.
project_name> spam
Constructing... Done.
```

## To Do

- Pre- and post-construction scripts
	- In-skeleton
	- Global