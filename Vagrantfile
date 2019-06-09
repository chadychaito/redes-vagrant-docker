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
  	#containerservidor.vm.network "public_network", bridge: "ens3"
  	containerservidor.vm.network "private_network", ip: "192.168.50.2"
	containerservidor.vm.hostname = "containerservidor"
  	containerservidor.vm.provider "virtualbox" do |vb|
      		vb.memory = "4096"
    	  	vb.name = "containerservidor"
  	end
	containerservidor.vm.provision "shell" do |s|
		s.inline = "sudo apt update"
        s.inline = "sudo apt -y upgrade"
		s.inline = "sudo apt -y install apt-transport-https ca-certificates curl gnupg-agent software-properties-common"
		s.inline = "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -"
		s.inline = "sudo apt-key fingerprint 0EBFCD88"
		s.inline = 'sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"'
		s.inline = "sudo apt update"
		s.inline = "sudo apt -y install docker-ce docker-ce-cli containerd.io"
		s.inline = "sudo systemctl start docker"
		s.inline = "sudo systemctl enable docker"
		s.inline = "sudo gpasswd -a "${USER}" docker"
	end
end

config.vm.define "containercliente" do |containercliente|

 	containercliente.vm.box = "ubuntu/bionic64"
  	#containercliente.vm.network "public_network"
  	containercliente.vm.network "private_network", ip: "192.168.50.3"
	containercliente.vm.hostname = "containercliente"
  	containercliente.vm.provider "virtualbox" do |vb|
      		vb.memory = "1500"
    	  	vb.name = "containercliente"
  	end
	containercliente.vm.provision "shell" do |s|
        s.inline = "sudo apt update"
        s.inline = "sudo apt -y upgrade"
		s.inline = "sudo apt -y install apt-transport-https ca-certificates curl gnupg-agent software-properties-common"
		s.inline = "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -"
		s.inline = "sudo apt-key fingerprint 0EBFCD88"
		s.inline = 'sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"'
		s.inline = "sudo apt update"
		s.inline = "sudo apt -y install docker-ce docker-ce-cli containerd.io"
		s.inline = "sudo systemctl start docker"
		s.inline = "sudo systemctl enable docker"
		s.inline = "sudo gpasswd -a "${USER}" docker"
	end
end
end
