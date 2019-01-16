## Install miniconda3

#### When prompted install to /opt/miniconda3

    bash miniconda.sh

    chmod ugo+w /opt/miniconda3

## Install jupyter lab and hub

    sudo conda install jupyterlab jupyterhub

## C++ - must install first 

    sudo conda install xeus-cling notebook -c QuantStack -c conda-forge

## C (gcc)

    sudo pip install jupyter-c-kernel
    
    sudo install_c_kernel

## Ruby 

    sudo apt install libtool libffi-dev ruby ruby-dev make libzmq3-dev libczmq-dev

    ./autogen.sh && ./configure && sudo make && sudo make install
    
    sudo gem install cztop iruby sciruby-full
    
    sudo iruby register --force

## Lua

    sudo apt install lua5.3

    sudo pip install ilua

## Golang

    sudo conda install -c conda-forge jupyter_contrib_nbextensions

    wget https://dl.google.com/go/go1.11.4.linux-amd64.tar.gz
    
    sudo tar -C /opt -xzf go1.11.4.linux-amd64.tar.gz
    
    go get -u github.com/gopherdata/gophernotes

    sudo cp $GO_PATH/go/src/github.com/gopherdata/gophernotes/kernel/* /opt/miniconda3/share/jupyter/kernels/gophernotes

## Bash

    sudo pip install bash_kernel

    sudo python -m bash_kernel.install

## Powershell

    sudo apt install curl gnupg apt-transport-https\n

    curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -\n

    sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-debian-stretch-prod stretch main" > /etc/apt/sources.list.d/microsoft.list'\n

    sudo apt update
    
    sudo apt install powershell
    
    sudo pip install powershell_kernel
    
    sudo python -m powershell_kernel.install

### Make it so miniconda3 and the kernels can be used systemwide

    chmod -R ugo+w /opt/miniconda3

### Make sure all your kernels are installed. 

    jupyter kernelspec list


## Juptyer Extension Installation

    conda install -c conda-forge jupyter_contrib_nbextensions

    conda install -c conda-forge jupyter_nbextensions_configurator


## Generate SSL certs

    openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout jlcert.pem -out jlcert.pem

## Systemd Service 

    sudo cp jupyterlab.server /usr/lib/systemd/system/.
    
    sudo systemctl daemon-reload

    sudo systemctl enable jupyterlab.service

    sudo systemctl start jupyterlab.service
