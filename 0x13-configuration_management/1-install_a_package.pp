#install puppet-lint, ensure version fails
package { 'puppet-lint':
  ensure   => 'latest',
  provider => 'gem',
}
