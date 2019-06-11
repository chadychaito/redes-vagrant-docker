# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

Vagrant.configure(2) do |config|
 	config.vm.define "containerservidor" do |containerservidor|

		containerservidor.vm.box = "ubuntu/bionic64"
		containerservidor.vm.network "forwarded_port", guest: 9000, host: 9002
		containerservidor.vm.network "private_network", ip: "192.168.50.2"
		containerservidor.vm.hostname = "containerservidor"
		containerservidor.vm.provider "virtualbox" do |vb|
				vb.memory = "4096"
				vb.name = "containerservidor"
		end
		containerservidor.vm.provision "shell", privileged: "false", inline: <<-SHELL
			sudo apt -y install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
			curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
			sudo apt-key fingerprint 0EBFCD88
			sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
			sudo apt update
			sudo apt install -y python3
			sudo apt install -y python3-pip
			sudo pip install flask
			sudo apt -y install docker-ce docker-ce-cli containerd.io
			sudo systemctl enable docker
			sudo gpasswd -a "${USER}" docker
			git clone https://github.com/chadychaito/redes-vagrant-docker.git
			sudo docker swarm init --advertise-addr 192.168.50.2:2377 | sed 5!d > /vagrant/token.sh
			sudo docker build -t server 
			sudo docker network create -d overlay --subnet 10.0.10.0/24 ClusterNet
			docker service create --name webservice1 --network ClusterNet --replicas 3 -p 5001:80 francois/apache-hostnames
			sudo systemctl start docker
		SHELL

	end

	config.vm.define "containercliente" do |containercliente|
		containercliente.vm.box = "ubuntu/bionic64"
		#containercliente.vm.network "public_network"
		containercliente.vm.network "private_network", ip: "192.168.50.3"
		containercliente.vm.hostname = "containercliente"
		containercliente.vm.provider "virtualbox" do |vb|
				vb.memory = "2048"
				vb.name = "containercliente"
		end
		containercliente.vm.provision "shell", privileged: "false", inline: <<-SHELL
			sudo apt -y install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
			curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
			sudo apt-key fingerprint 0EBFCD88
			sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
			sudo apt update
			sudo apt install -y python3
			sudo apt -y install docker-ce docker-ce-cli containerd.io
			#sudo systemctl enable docker

			git clone https://github.com/chadychaito/redes-vagrant-docker.git

			cd redes-vagrant-docker/container-server
			chmod +x /vagrant/token.sh
			bash /vagrant/token.sh
			sudo docker build -t client .

			sudo systemctl start docker

		SHELL
	end
end
