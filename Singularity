BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%files
    requirements.txt

%setup
    cp requirements.txt $SINGULARITY_ROOTFS/tmp/

%post
    apt-get install -y software-properties-common
    apt-add-repository ppa:longsleep/golang-backports
    apt-add-repository ppa:ubuntugis/ppa
    apt-add-repository universe
    apt-get update
    apt-get install -y python python-dev python-pip build-essential git openssl golang-go gdal-bin
    pip install --upgrade pip
    pip install --upgrade virtualenv setuptools
    pip install planet google-api-python-client pyCrypto earthengine-api

# Setup Go-Lang Paths
#    echo "export PATH=$PATH:/opt/go/bin" >> ~/.bashrc
#    echo "export GOPATH=/opt/go" >> ~/.bashrc
    export GOPATH=/opt/go

# Install Drive
    go get -u github.com/odeke-em/drive/cmd/drive

# Planet Batch Slack
    git clone https://github.com/samapriya/Planet-Batch-Slack-Pipeline-CLI
    cd Planet-Batch-Slack-Pipeline-CLI
    pip install -r requirements.txt
    python setup.py install

# Planet Clip and Ship
    git clone https://github.com/samapriya/Clip-Ship-Planet-CLI
    cd Clip-Ship-Planet-CLI && pip install -r requirements.txt
    python setup.py install

# Planet Earth Engine CLI included GEE Tools
    git clone https://github.com/samapriya/planet-cyverse
    cd Tools/Planet-GEE-Pipeline-CLI && pip install -r requirements.txt
    python setup.py install

##Install Drive
    go get -u github.com/odeke-em/drive/cmd/drive

%environment
# Setup Go-Lang Paths
    PATH=$PATH:/opt/go/bin
    GOPATH=/opt/go


%labels
    Maintainer Tyson L Swetnam & Sam Roy
    Version v0.3