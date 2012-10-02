from setuptools import setup
import os

setup(name='yorick',
	version='0.1pre',
	description='a project skeleton / template / boilerplate tool',
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
