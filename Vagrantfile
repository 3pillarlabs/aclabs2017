# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
  config.vm.synced_folder ".", "/vagrant_data"
  config.vm.synced_folder "#{ENV['HOME']}/ssh", "/ssh"
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y python-virtualenv git emacs vim
    sudo su - ubuntu -c 'virtualenv -p $(which python3) $HOME/venv'
    sudo su - ubuntu -c '$HOME/venv/bin/pip install django'
  SHELL
end
