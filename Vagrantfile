# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  #Configurando container server
  config.vm.define "container_server" do |container_server|
   	container_server.vm.box = "ubuntu/bionic64"
   	container_server.vm.network "forwarded_port", guest: 9000, host: 9001
    #container_server.vm.network "public_network", bridge: "ens3"
    container_server.vm.network "private_network", ip: "192.168.50.2"
  	container_server.vm.hostname = "container_server"
  	container_server.vm.provider "virtualbox" do |vb|
  		vb.memory = "1024"
	  	vb.name = "container_server"
  	end
  	container_server.vm.provision "shell" do |s|
  		#s.inline = "sudo apt update"
      #s.inline = "sudo apt -y upgrade"
  	end
    container_server.vm.provision :docker do |docker|
      docker.build_image '/vagrant/.', args: '-t dockerfile_server'
      docker.run 'dockerfile_server'
    end
  end
  #Configurando container cliente
  config.vm.define "container_client" do |container_client|

   	container_client.vm.box = "ubuntu/bionic64"
    #container_client.vm.network "public_network"
    container_client.vm.network "private_network", ip: "192.168.50.3"
  	container_client.vm.hostname = "container_client"
  	container_client.vm.provider "virtualbox" do |vb|
  		vb.memory = "1024"
	  	vb.name = "container_client"
  	end
  	container_client.vm.provision "shell" do |s|
      #s.inline = "sudo apt update"
      #s.inline = "sudo apt -y upgrade"
  	end
    container_server.vm.provision :docker do |docker|
      docker.build_image '/vagrant/.', args: '-t dockerfile_client'
      docker.run 'dockerfile_client'
    end
  end
end
