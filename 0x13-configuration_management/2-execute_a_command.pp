# kill a process called killmenow, specify command path
exec { 'pkill killmenow':
  command => '/usr/bin/pkill -f killmenow',
}
