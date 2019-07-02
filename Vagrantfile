# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

Vagrant.configure(2) do |config|
 	config.vm.define "containermaster" do |containermaster|

		containermaster.vm.box = "ubuntu/bionic64"
		containermaster.vm.network "forwarded_port", guest: 9000, host: 9001
		containermaster.vm.network "private_network", ip: "192.168.50.2"
		containermaster.vm.hostname = "containermaster"
		containermaster.vm.provider "virtualbox" do |vb|
				vb.memory = "4096"
				vb.name = "containermaster"
		end
		containermaster.vm.provision "shell", privileged: "false", inline: <<-SHELL
			echo "##           ##"
			echo "## INICIANDO ##"
			echo "##   MASTER  ##"

			sudo apt -y install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
			curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -	
			sudo apt-key fingerprint 0EBFCD88			
			sudo add-apt-repository -y "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"			
			sudo apt update		
			sudo apt install -y python3			
			sudo DEBIAN_FRONTEND=noninteractive apt install -y python3-pip		
			sudo pip3 install -y flask		
			sudo apt -y install docker-ce docker-ce-cli containerd.io		
			sudo systemctl start docker
			
			git clone https://github.com/chadychaito/redes-vagrant-docker.git
			
			echo "##                  ##"
			echo "## INICIANDO DOCKER ##"
			echo "##                  ##"

			cd redes-vagrant-docker/
			sudo docker swarm init --advertise-addr 192.168.50.2:2377 | sed 5!d > /vagrant/token.sh
			sudo docker network create -d overlay --subnet 10.0.10.0/24 ClusterNet

			echo "##                    ##"
			echo "## SUBINDO PROMETHEUS ##"
			echo "##                    ##"

			cd prometheus

			sudo docker build -t my-prometheus .
			sudo docker run -p 9091:9091 --restart=always --detach=true --name=prometheus my-prometheus
			sudo docker run -d --restart=always --net="host" --pid="host" --publish=9100:9100 --detach=true --name=node-exporter -v "/:/host:ro,rslave" quay.io/prometheus/node-exporter --path.rootfs /host
			sudo docker run --restart=always --volume=/:/rootfs:ro --volume=/var/run:/var/run:ro --volume=/sys:/sys:ro --volume=/var/lib/docker/:/var/lib/docker:ro --volume=/dev/disk/:/dev/disk:ro --publish=8080:8080 --detach=true --name=cadvisor google/cadvisor:latest

			echo "##                 ##"
			echo "## SUBINDO APP2.PY ##"
			echo "##                 ##"

			cd ../container-monitoring

			sudo docker build -t app2 .
			sudo docker run -d -v /var/run/docker.sock:/var/run/docker.sock app2

			echo "##                 ##"
			echo "## SUBINDO APP3.PY ##"
			echo "##                 ##"

			cd ../vm-monitoring

			sudo docker build -t app3 .
			sudo docker run -d -v --restart=always --detach=true --name=app3 app3

		SHELL

	end
	config.vm.define "containerworker" do |containerworker|
		containerworker.vm.box = "ubuntu/bionic64"
		containerworker.vm.network "private_network", ip: "192.168.50.3"
		containerworker.vm.hostname = "containerworker"
		containerworker.vm.provider "virtualbox" do |vb|
				vb.memory = "2048"
				vb.name = "containerworker"
		end
		containerworker.vm.provision "shell", privileged: "false", inline: <<-SHELL
			echo "##           ##"
			echo "## INICIANDO ##"
			echo "##   WORKER  ##"

			sudo apt -y install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
			curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
			sudo apt-key fingerprint 0EBFCD88
			sudo add-apt-repository -y "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
			sudo apt update
			sudo apt install -y python3
			sudo DEBIAN_FRONTEND=noninteractive apt install -y python3-pip
			sudo pip3 install docker
			sudo apt -y install docker-ce docker-ce-cli containerd.io
			sudo systemctl start docker
			#sudo systemctl enable docker
			git clone https://github.com/chadychaito/redes-vagrant-docker.git
			cd redes-vagrant-docker/
			chmod +x /vagrant/token.sh
			bash /vagrant/token.sh

			echo "##               ##"
			echo "## SUBINDO MONGO ##"
			echo "##               ##"

			sudo docker pull mongo 
			sudo docker run -it -d -p 27017:27017 --restart=always --detach=true --name=mongo mongo
			sudo docker run -it -d -p 27018:27018 --restart=always --detach=true --name=mongo2 mongo

			echo "##                  ##"
			echo "## SUBINDO SERVIDOR ##"
			echo "##                  ##"
			
			cd cliente-servidor/servidor

			sudo docker build -t servidor .
			sudo docker run -d -v /var/run/docker.sock:/var/run/docker.sock servidor

			echo "##                 ##"
			echo "## SUBINDO CLIENTE ##"
			echo "##                 ##"
			
			cd ../cliente

			sudo docker build -t cliente .
			sudo docker run -d -v /var/run/docker.sock:/var/run/docker.sock cliente	

			echo "##                 ##"
			echo "## SUBINDO APP2.PY ##"
			echo "##                 ##"

			cd ../../container-monitoring

			sudo docker build -t app2 .
			sudo docker run -d -v /var/run/docker.sock:/var/run/docker.sock app2

			echo "##                 ##"
			echo "## SUBINDO APP3.PY ##"
			echo "##                 ##"

			cd ../vm-monitoring

			sudo docker build -t app3 .
			sudo docker run -d -v --restart=always --detach=true --name=app3 app3		

		SHELL
	end
end
