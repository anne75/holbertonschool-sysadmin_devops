# The default configuration file for mginx only allows 15 max open files
# this triggers errors when the server receives too many requests
exec {'change limit from 15 to 1024 in /etc/default/nginx':
  command => 'sed -i "s@ULIMIT=\"-n 15\"@ULIMIT=\"-n 1024\"@" /etc/default/nginx && /etc/init.d/nginx restart',
}