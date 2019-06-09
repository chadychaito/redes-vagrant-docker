# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

Vagrant.configure(2) do |config|
  config.vm.define "container-servidor" do |container-servidor|

 	container-servidor.vm.box = "ubuntu/bionic64"
 	container-servidor.vm.network "forwarded_port", guest: 9000, host: 9001
  	#container-servidor.vm.network "public_network", bridge: "ens3"
  	container-servidor.vm.network "private_network", ip: "192.168.50.2"
	container-servidor.vm.hostname = "container-servidor"
  	container-servidor.vm.provider "virtualbox" do |vb|
      		vb.memory = "4096"
    	  	vb.name = "container-servidor"
  	end
	container-servidor.vm.provision "shell" do |s|
		s.inline = "sudo apt update"
                s.inline = "sudo apt -y upgrade"
	end
end

config.vm.define "container-cliente" do |container-cliente|

 	container-cliente.vm.box = "ubuntu/bionic64"
  	#container-cliente.vm.network "public_network"
  	container-cliente.vm.network "private_network", ip: "192.168.50.3"
	container-cliente.vm.hostname = "container-cliente"
  	container-cliente.vm.provider "virtualbox" do |vb|
      		vb.memory = "1500"
    	  	vb.name = "container-cliente"
  	end
	container-cliente.vm.provision "shell" do |s|
                s.inline = "sudo apt update"
                s.inline = "sudo apt -y upgrade"
	end
end
end
