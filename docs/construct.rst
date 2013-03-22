Constructing a Yorick skeleton
==============================

Projects are constructed from a skeleton using the `yorick construct` command.

::

	$ yorick construct eggs
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


Instead of being prompted for variables interactively, you can specify them on the command line.

::

	$ yorick construct eggs project_name=spam
	Constructing... Done.
	
Skeletons are stored inside 'closets'. All of your closets are in the ``~/.yorick/`` folder.

By default, skeletons are taken from the 'default closet', which is located at ``~/.yorick/__default__/``. (So, the `eggs` skeleton would be at ``~/.yorick/__default__/eggs/``.)

To construct a skeleton from a different closet, use the form `yorick construct <closet>.<skeleton-name>`. For instance, the command ``yorick construct fred.spam`` would construct the skeleton located at ``~/.yorick/fred/spam/``.

To construct a skeleton that is somewhere other than one of the closets in your `.yorick` directory, use the `-p` flag to specify a path to it, for example `yorick construct -p ~/blah/myskeleton`.
