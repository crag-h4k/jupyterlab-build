# JupyterLab and Jupyter Hub Install

## Install JupyterLab and JupyterHub with a bunch of additional languages

### run <python -c 'import lang; lang.python3_base()'>


#### replace <python3_base> with the other function names

jupyter_lab()

python3_base()

jupyter_hub()

c()

ruby()

cpp()

bash()


#### <python3 install.py> to install jupyter-lab and all above languages 

## System Service Installation

#### save jupyterlab.service at 

/usr/lib/systemd/system/jupyterlab.service


#### Enable service 

sudo systemctl enable jupyter.service

#### Reload services

sudo systemctl daemon-reload

#### Restart JupyterLab

sudo systemctl start jupyterlab.service

#### Check Status of JupyterLab

sudo systemctl start jupyterlab.service


