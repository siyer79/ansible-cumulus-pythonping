#Vagrant.configure(2) do |config|
#  config.vm.box = "cumulus-vx-3.0.0" end

Vagrant.configure(2) do |config|

   config.vm.box = "cumulus-vx-3.0.0"

   
##### DEFINE VM for playserver #####
   config.vm.define "playserver" do |device|
     device.vm.hostname = "playserver"
     device.vm.network "private_network", ip: "192.168.118.1/24"
     
     device.vm.provider "virtualbox" do |v|
       v.name = "playserver"
       v.memory = 512
     end

   end

##### DEFINE VM for switch01 #####
   config.vm.define "switch01" do |device|
     device.vm.hostname = "switch01"
     device.vm.network "private_network", ip: "192.168.118.100/24"

     device.vm.provider "virtualbox" do |v|
       v.name = "switch01"
       v.memory = 512
     end

   end

##### DEFINE VM for switch02 #####
   config.vm.define "switch02" do |device|
     device.vm.hostname = "switch02"
     device.vm.network "private_network", ip: "192.168.119.100/24"

     device.vm.provider "virtualbox" do |v|
       v.name = "switch02"
       v.memory = 512
     end

   end


   config.vm.provision "ansible" do |ansible|
     ansible.verbose = "vvv"
     ansible.playbook = "test-playbook.yml"
   end


end



