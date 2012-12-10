from setuptools import setup, find_packages
import subprocess
from yorick import __version__

def get_long_desc():
	"""Use Pandoc to convert the readme to ReST for the PyPI."""
	try:
		return subprocess.check_output(['pandoc', '-f', 'markdown', '-t', 'rst', 'README.md'])
	except:
		print "WARNING: The long readme wasn't converted properly"

setup(name='yorick',
	version=__version__,
	description='a project skeleton / template / boilerplate tool',
	long_description=get_long_desc(),
	author='Adam Brenecki',
	author_email='adam@brenecki.id.au',
	url='https://github.com/adambrenecki/yorick',
	packages=find_packages(),
	include_package_data=True,
	setup_requires=[
		'setuptools_git>=0.3',
	],
	install_requires=[
		'pyyaml',
		'jinja2',
	],
	entry_points = {
    'console_scripts':
        ['yorick = yorick.cli:app.run'],
	},
	classifiers = [
		'Development Status :: 2 - Pre-Alpha',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Topic :: Software Development :: Build Tools',
		'Topic :: Software Development :: Pre-processors',
	]
)
