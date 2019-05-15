#!/usr/bin/env python3
import psutil
import os

m = []
m = psutil.virtual_memory()
print("% used: ", m[2])

if (m[2]>50):
	os.system('firefox')
else:
	os.system('chrome')
