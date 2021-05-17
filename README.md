# calculating_tax

**This application calculates the amount of income tax one has to pay through a number of tax bands**


## Setup Local Environment

### 1. Installing pipenv
Make sure you’ve got Python & pip
```bash
sudo pip install -U pipenv
```


#### 2. Installing docker
##### Remove old versions of docker
Older versions of Docker were called docker, docker.io, or docker-engine.  
If these are installed, uninstall them:
```bash
sudo apt-get remove docker docker-engine docker.io containerd runc docker-compose
```
It’s OK if apt-get reports that none of these packages are installed.  
The contents of /var/lib/docker/, including images, containers, volumes, and networks, are preserved.  
The Docker CE package is now called docker-ce.

##### Install Docker
Update the apt package index:
```bash
sudo apt update
```
Install packages to allow apt to use a repository over HTTPS:
```bash
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
```
##### Add Docker’s official GPG key
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
##### Set up the repository
Replace value arch= of your correct cpu architecture. Try lscpu in bash for check.  
Available values: amd64(include x86_64), armhf, ppc64el and s390x
```bash
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```
##### Install docker
Update the apt package index.
```bash
sudo apt update
```
Install the latest version of Docker CE and containerd
```bash
sudo apt install docker-ce docker-ce-cli containerd.io
```
Verify that Docker CE is installed correctly by running the hello-world image.
```bash
sudo docker run hello-world
```
This command downloads a test image and runs it in a container.  
When the container runs, it prints an informational message and exits.
In luck case, you must see following lines in text bellow:
```
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

Install latest version of Docker-compose
```bash
sudo apt install jq
VERSION=$(curl --silent https://api.github.com/repos/docker/compose/releases/latest | jq .name -r)
DESTINATION=/usr/local/bin/docker-compose
sudo curl -L https://github.com/docker/compose/releases/download/${VERSION}/docker-compose-$(uname -s)-$(uname -m) -o $DESTINATION
sudo chmod 755 $DESTINATION
```
This commands firstly find the latest version of docker-compose 
via GitHub api using jq(You can read more about jq here:https://stedolan.github.io/jq/).
Then it setup instalation of docker-compose variable. 
Then Download docker-compose and change permissions of downloaded files.

To check instalation of docker-compose check version:
```bash
docker-compose --version
```


### 3. Manage Docker as a non-root user
Create the docker group if is not exist.
```bash
sudo groupadd docker && sudo usermod -aG docker $USER
```
Log out and log back in so that your group membership is re-evaluated.
Verify that you can run docker commands without sudo
```bash
docker run hello-world
```



## Pipenv project commands
Run this commands from the project root dir.  

Start local server   
```bash
docker-compose up --build
```

The server is stopped by the command
```bash
docker-compose down
```

Enter in pipenv project environment
```bash
pipenv shell
```

Install all dependencies
```bash
pipenv install
```

Run tests
```bash
pipenv run test
```
