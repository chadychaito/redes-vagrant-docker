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

			cd redes-vagrant-docker/container-server
			sudo docker swarm init --advertise-addr 192.168.50.2:2377 | sed 5!d > /vagrant/token.sh
			sudo docker network create -d overlay --subnet 10.0.10.0/24 ClusterNet
			docker service create -d --name webservice1 --network ClusterNet --replicas 3 -p 5001:80 server

			echo "##                    ##"
			echo "## SUBINDO PROMETHEUS ##"
			echo "##                    ##"

			cd ../prometheus

			sudo docker build -t my-prometheus .
			sudo docker run -p 9091:9091 --restart=always --detach=true --name=prometheus my-prometheus

			echo "##               ##"
			echo "## SUBINDO MONGO ##"
			echo "##               ##"

			cd ../vm-monitoring

			sudo docker pull mongo 
			sudo docker run -it -d --restart=always --detach=true --name=mongo mongo

			echo "##                 ##"
			echo "## SUBINDO APP3.PY ##"
			echo "##                 ##"

			sudo docker build -t app3 .
			sudo docker run -d -p 5000:5000 --restart=always --detach=true --name=app3 app3

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
			cd redes-vagrant-docker/container-client
			chmod +x /vagrant/token.sh
			bash /vagrant/token.sh

			echo "##                  ##"
			echo "## SUBINDO SERVIDOR ##"
			echo "##                  ##"
			echo "-- servidor em desenvolvimento --\n"

			echo "##                 ##"
			echo "## SUBINDO CLIENTE ##"
			echo "##                 ##"
			echo "-- cliente em desenvolvimento --\n"

		SHELL
	end
end
