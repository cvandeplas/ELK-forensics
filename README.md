ELK-forensics
=============

ELK configuration files for Forensic Analysts and Incident Handlers.

For more information, screenshots and HOWTO's read:

* [Setting up a single ELK node in 20 minutes](http://christophe.vandeplas.com/2014/06/setting-up-single-node-elk-in-20-minutes.html)
* [Mactime magic with ELK](http://christophe.vandeplas.com/2014/06/mactime-magic-with-elk.html)
* [BlueCoat Proxy log search and analytics](http://christophe.vandeplas.com/2014/07/bluecoat-proxy-log-search-and-analytics.html)
* http://christophe.vandeplas.com/search/label/elk


How to use
==========

     apt-get install git-core
     git clone https://github.com/cvandeplas/ELK-forensics

That will create a directory - ELK-forensics - holding the configuration files.

 - Open your Kibana web interface
 - Right upper corner, Load -> Advanced -> Browse
 - Load the desired json template(s)
 - Copy the .conf file to your /etc/logstash/conf.d directory
 - Restart the logstash service
 - Feed your logs

Do not hesitate to contribute !
All feedback is appreciated !

Thanks 
Christophe

License
=======
* License: AGPL v3 - http://www.gnu.org/copyleft/gpl.html 
* Copyright: Christophe Vandeplas <christophe@vandeplas.com>
