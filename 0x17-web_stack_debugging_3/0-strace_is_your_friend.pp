# Create manifest that fix termintion of phpp.

exec { 'fix_wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/loca/bin/:/bin/'
}
