Opening your closets to the world with Git
==========================================

Closets are shared as Git repositories or tar balls, and added with the `yorick install-closet` command. They can be updated with the `yorick update-closets` command.

::

	$ yorick install-closet --git http://github.com/adambrenecki/yorick-closet abre
	Waiting on VCS... Done.
	You can now install a skeleton from this closet by running 'yorick construct abre.<skeleton-name>'
	
	$ yorick update-closets
	Updating abre... Done.
