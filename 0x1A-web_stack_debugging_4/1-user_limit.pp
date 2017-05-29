# grant user holberton better max open files limits
$command1 = 's@holberton hard nofile 5@* hard nofile 1024@'
$command2 = 's@holberton soft nofile 4@* soft nofile 1024@'

exec {'change limits for user in /etc/security/limits.conf':
  command => "sed -i \"${command1}; ${command2}\" /etc/security/limits.conf",
  path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
}
