Yorick skeleton reference
=========================

Skeleton Properties
-------------------

These are the properties that go in ``-yorick-meta/config.yml``.

- ``id`` - A UUID for the skeleton. This should be generated for you by ``yorick create-skeleton``, and you shouldn't change it unless you're creating a new skeleton by copying a different one.
- ``description`` - A description for the skeleton.
- ``variables`` - A dictionary of variables, as specified in the Variable Properties section below.
- ``excluded_files`` - A list of files to skip over completely in the generation process.

Variable Properties
-------------------

- ``prompt`` - The text to present to the user when asking for the value of this variable. If this value is omitted, the user won't be prompted at all, and the only way to provide a value for this variable will be on the command line.
- ``default`` - The default value to use if one isn't given. If this is omitted, the variable will be mandatory.
- ``type`` - The type of value this variable will store. Valid types are ``string`` (the default), ``integer``, ``decimal`` and ``boolean``.

File Names
----------

When the skeleton is built, the name of each file and directory is processed according to a set of rules. (Note that these rules apply to files **and** directories.)

- If a filename contains a variable name surrounded in curly brackets, it is replaced with that variable's value.
	- Curly brackets around anything that isn't a valid variable name will cause an error. 
- If a filename contains doubled-up curly brackets, they are replaced with single curly brackets.
	- Filenames with unmatched curly brackets will cause an error unless they're doubled-up.
- If a file's entire name is ``-yorick-meta``, it is skipped over. (The reason for this, as we saw previously, is that metadata for your skeleton is stored in this directory.)
- If a filename ends with ``.yorick-literal``, that bit is removed from the file name. The file name is then not processed any further, so none of the other rules on this list apply to it. (This is useful for filenames that would otherwise have special meaning to Yorick (e.g. with curly braces) or to other programs like Git (eg a ``.gitignore`` that is part of the template)
- Finally, if a filename ends with ``.yorick-<something>`` (where ``<something>`` is anything other than ``literal``), it is processed as described in the following section, and that part of the filename is removed. Unlike ``.yorick-literal``, the rest of the rules in this list do apply.

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
``name.py.yorick-j2``                  ``name.py`` (file contents processed with ``j2`` engine)
``{name}.py.yorick-t``                 ``spam.py`` (file contents processed with ``t`` engine)
``{name}.py.yorick-t.yorick-literal``  ``{name}.py.yorick-t`` (file contents copied verbatim)
====================================== ===================


File Contents
-------------

Hooks
-------

Hooks allow you to write code to perform arbitrary tasks at certain events in Yorick's execution cycle.

Python
``````

Python hooks should be implemented within the file ``-yorick-meta/hooks.py``, as functions with the hook name as the function name.

Hooks should raise ``yorick.hooks.HookError`` on error.

For example, the following ``hooks.py`` checks that the ``banana`` variable starts with the letter ``B``:

::
    from yorick.hooks import HookError

    def pre_construct(vars):
        if not vars['banana'].startswith('B'):
            raise HookError("`banana` must start with `B`")
        return vars

Shell
`````

Shell hooks are executable files placed within the ``-yorick-meta/hooks/`` directory. For instance, to run a hook on the ``pre-construct`` event, place it at ``-yorick-meta/hooks/pre-construct``. An optional file extension is also allowed.

Hooks must terminate with a nonzero return code on error. In such a case, Yorick will display the hook's standard output to the user.

Hooks can be written in any scripting language. On Mac OS X and Linux, they will be run with ``sh``; on Windows, with their filetype's default handler. For this reason, it is recommended that they be named with the appropriate extension **and** contain an appropriate shebang line. (For example, a Ruby pre-construct hook should be named ``pre-construct.rb`` and begin like ``#!/usr/bin/env ruby``).

Hook List
`````````

- ``pre-construct`` - Run before the skeleton is constructed. Can perform validation on the variables, or other such tasks.
  - Python: Takes a dictionary of the variables and their values. Must return that dictionary, which may be modified.
  - Shell: Takes a JSON-formatted object of the variables and their values on standard input. Must output a JSON-formatted object of variables and their values, optionally modified.
- ``post-construct`` - Run after the skeleton is constructed. Can perform post-construction clean-up or other such tasks.
  - Python: Takes a dictionary of the variables and their values. Return value ignored.
  - Shell: Takes a JSON-formatted object of the variables and their values on standard input. Output ignored.
