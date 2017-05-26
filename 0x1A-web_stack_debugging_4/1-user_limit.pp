# grant user holberton better max open files limits

exec {'change limits for user in /etc/security/limits.conf':
  command =>'sed -i "s@holberton hard nofile 5@holberton hard nofile 1024@;\
s@holberton soft nofile 4@holberton soft nofile 1024@" /etc/security/limits.conf',
  path    =>['/bin', '/sbin', '/usr/bin', '/usr/sbin'],
}
