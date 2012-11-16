from setuptools import setup
import os
import subprocess

def get_long_desc():
	"""Use Pandoc to convert the readme to ReST for the PyPI."""
	try:
		return subprocess.check_output(['pandoc', '-f', 'markdown', '-t', 'rst', 'README.md'])
	except:
		print "WARNING: The long readme wasn't converted properly"

setup(name='yorick',
	version='0.1pre',
	description='a project skeleton / template / boilerplate tool',
	long_description=get_long_desc(),
	author='Adam Brenecki',
	author_email='adam@brenecki.id.au',
	url='',
	packages=['.'.join(i[0].split(os.sep))
		for i in os.walk('yorick')
		if '__init__.py' in i[2]],
	install_requires=[
		'pyyaml'
	],
	entry_points = {
    'console_scripts':
        ['yorick = yorick.cli:app.run'],
	},
)
