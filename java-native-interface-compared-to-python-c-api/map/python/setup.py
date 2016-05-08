# 
# Create dict (Python version)
# 
# Copyright (c) 2016 Project Nayuki
# All rights reserved. Contact Nayuki for licensing.
# https://www.nayuki.io/page/java-native-interface-compared-to-python-c-api
# 

import distutils.core


distutils.core.setup(
	ext_modules = [
		distutils.core.Extension(
			"createdict_native",
			sources = ["createdict_native.c"]
		)
	]
)
