#!/usr/bin/python
# run python -c 'import lang; lang.c()' 
# replace <python3_base> with the other function names
from os import system



def python3_base():
	try:
		system('cd')
		system('wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh')
		system('bash Miniconda3-latest-Linux-x86_64.sh')
	except Exception as e:
		print(e)

def jupyter_lab():
	try:
		system('conda install -c conda-forge jupyterlab')
	#only if running locally
	#system('conda install jupyterlab')
	#system('jupyterhub --generate-config')
	except Exception as e:
		print(e)

def jupyter_hub():
	return

def c():
	try:
		system('pip install jupyter-c-kernel')
		system('install_c_kernel')
	except Exception as e:
		print(e)

def ruby():
	try:	
		system('sudo apt install libtool libffi-dev ruby ruby-dev make libzmq3-dev libczmq-dev')
		system('cd && git clone https://github.com/zeromq/czmq')
		system('cd csmq && ./autogen.sh && ./configure && sudo make && sudo make install')
		system('gem install cztop iruby && iruby register --force')
	except Exception as e:
		print(e)

def cpp():
	# C++ 11,14,17
	try:	
		system('conda install -c conda-forge cling')
	except Exception as e:
		print(e)

def bash():
	try:
		system('pip install bash_kernel && python -m bash_kernel.install')
	except Exception as e:
		print(e)


