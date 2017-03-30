## First Steps with puppet
In this project we were introduced to [configuration management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management), and one of the tools to help in this task: [puppet](https://docs.puppet.com/puppet/3.5/type.html#file).  
Our tasks were to:  
0- create a file.  
1- install a package.  
2- execute a command.  

_____
**Install puppet**  
This is how puppet was installed on ubuntu trusty. It is an older version of puppet(3.4.3).
wget https://apt.puppetlabs.com/puppetlabs-release-trusty.deb
sudo dpkg -i puppetlabs-release-trusty.deb
sudo apt-get update
