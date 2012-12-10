Writing a Yorick skeleton
=========================

Use the ``yorick create-skeleton`` command to create a new skeleton. In this example, we'll create a skeleton called ``eggs``.

::

	$ yorick create-skeleton
	Enter a name for your skeleton.
	skeleton_name> eggs
	Constructing... Done.
	You can now edit your skeleton at ~/.yorick/__default__/eggs/
	
Go ahead and open that directory in your favourite text editor.

Configuration Files and Variables
---------------------------------

Open the file ``-yorick-meta/config.yml``.

.. todo::

	finish this

File names
----------

When the skeleton is built, the name of each file and directory is processed according to a set of rules. (Note that these rules apply to files **and** directories.)

- If a filename contains a variable name surrounded in curly brackets, it is replaced with that variable's value.
	- Curly brackets around anything that isn't a valid variable name will cause an error. 
- If a filename contains doubled-up curly brackets, they are replaced with single curly brackets.
	- Filenames with unmatched curly brackets will cause an error unless they're doubled-up.
- If a file's entire name is ``-yorick-meta``, it is skipped over. (The reason for this, as we saw previously, is that metadata for your skeleton is stored in this directory.)
- If a filename ends with ``.yorick-literal``, that bit is removed from the file name. The file name is then not processed any further, so none of the other rules on this list apply to it.

If we had a skeleton with one variable called ``name``, and we constructed it setting its value to ``spam``, here's how files or directories in the skeleton would be processed:

====================================== ===================
Name of file/directory in skeleton     Name of output file
====================================== ===================
``{name}.py``                          ``spam.py``
``{name}.py.yorick-literal``           ``{name}.py``
``{{name}}.py``                        ``{name}.py``
``{blah}.py``                          Error
``{.rst``                              Error
``{.rst.yorick-literal``               ``{.rst``
``{{.rst``                             ``{.rst``
``-yorick-meta`` (directory)           directory is skipped over
``-yorick-meta.yorick-literal``        ``-yorick-meta``
``eggs.yorick-literal``                ``eggs``
``eggs.yorick-literal.yorick-literal`` ``eggs.yorick-literal``
====================================== ===================


File Contents
-------------
