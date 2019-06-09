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
	end
end
end
