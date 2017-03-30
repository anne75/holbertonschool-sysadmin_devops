## Install https on the load balancer
([image](http://i.imgur.com/FlhGPEK.png))  

For this project, we built on our previous installation of Haproxy to add SSL through let's encrypt.
Mainly followed a [Digital Ocean tutorial](https://www.digitalocean.com/community/tutorials/how-to-secure-haproxy-with-let-s-encrypt-on-ubuntu-14-04).    
However, this tutorial does not redirect with a 301 code but uses the default 302.  
And secondly, it redirects all traffic comming to the IP, not the www subdomain. If ever I need it in the future, it looks like it could be done (see http://stackoverflow.com/questions/13227544/haproxy-redirecting-http-to-https-ssl ).  
Bash commands required: `awk`, `dig`.
___
**Readings**
- [What is HTTPS](https://www.instantssl.com/ssl-certificate-products/https.html)  
- [SSL Termination](https://en.wikipedia.org/wiki/TLS_termination_proxy)
