from setuptools import setup, find_packages
import sys, os

version = '0.1.1'

setup(
	name='ckanext-openafrica',
	version=version,
	description="CKAN extension for Open Africa.",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='David Lemayian',
	author_email='david@openinstitute.com',
	url='http://africaopendata.org',
	license='MIT Open Licence.',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.openafrica'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
	[ckan.plugins]
	# Add plugins here, eg
	# myplugin=ckanext.openafrica:PluginClass
	openafrica=ckanext.openafrica.plugin:OpenAfricaPlugin
	""",
)
