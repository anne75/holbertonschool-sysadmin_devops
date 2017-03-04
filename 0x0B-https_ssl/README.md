## Install https on the load balancer

For this project, we built on our previous installation of Haproxy to add let's encrypt.
Mainly followed a Digital Ocean tutorial.  
However, this tutorial does not redirect with a 301 code but uses the default 302.  
And secondly, it redirects all traffic comming to the IP, not the www subdomain. If ever I need it in the future, it looks like it could be done (see http://stackoverflow.com/questions/13227544/haproxy-redirecting-http-to-https-ssl )
