## Deploy a static website
This project actually resides in another [repository](../../AirBnB_v2).  
The configuration is [here](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/288/aribnb_diagram_0.jpg?cache=off).  

We used `fabric` module in python a a bit of bash scripting to archive the website and then deploy it on a web server.

_________________
**Reading**
<ul>
<li><a href="https://www.digitalocean.com/community/tutorials/how-to-use-fabric-to-automate-administration-tasks-and-deployments">How to use Fabric</a></li>
<li><a href="http://www.pythonforbeginners.com/systems-programming/how-to-use-fabric-in-python">How to use Fabric in Python</a></li>
<li><a href="http://docs.fabfile.org/en/1.13/usage/fab.html#command-line-options">Fabric and command line options</a></li>
<li><a href="https://intranet.hbtn.io/concepts/43">CI/CD concept page</a></li>
<li><a href="http://nginx.org/en/docs/beginners_guide.html">Nginx configuration for beginners</a></li>
<li><a href="https://blog.heitorsilva.com/en/nginx/diferenca-entre-root-e-alias-do-nginx/">Difference between root and alias on NGINX</a></li>
<li><a href="http://stackoverflow.com/questions/10631933/nginx-static-file-serving-confusion-with-root-alias">Again root and alias</a></li>
</ul>

<p>For  references:</p>

<ul>
<li><a href="https://github.com/mathiasertl/fabric">Fabric for Python 3</a></li>
<li><a href="http://www.fabfile.org">Fabric Documentation</a></li>
</ul>

Install `fabric` in python3:    
```
$ pip3 uninstall Fabric
$ sudo apt-get install libffi-dev
$ sudo apt-get install libssl-dev
$ sudo apt-get install python3.4-dev
$ sudo apt-get install libpython3-dev
$ pip3 install pyparsing
$ pip3 install appdirs
$ pip3 install Fabric3
```
