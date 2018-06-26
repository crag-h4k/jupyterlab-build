# JupyterLab and Jupyter Hub Install

## Install JupyterLab and JupyterHub with a bunch of additional languages

example: 
	python -c 'import lang; lang.python3_base()' #replace <python3_base> with the other function names

	jupyter_lab()

	python3_base()

	jupyter_hub()

	c()

	ruby()

	cpp()

	bash()

####  to install jupyter-lab and all above languages 
	<python2 install.py>
## System Service Installation

#### save jupyterlab.service at 

	/usr/lib/systemd/system/jupyterlab.service


#### Enable service 

	sudo systemctl enable jupyterlab.service

#### Reload services

	sudo systemctl daemon-reload

#### Restart JupyterLab

	sudo systemctl restart jupyterlab.service

#### Check Status of JupyterLab

	sudo systemctl status jupyterlab.service

