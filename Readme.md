# # iDirScan
* * *

Simple but effective, open to improvement..

```bash
root@ihsan:~/Desktop# python3 iDirScan.py

########################################
#        +-+-+-+-+-+-+-+-+-+-+-+-+     #
#        |*|*|i|D|i|r|S|c|a|n|*|*|     #
#        +-+-+-+-+-+-+-+-+-+-+-+-+     #
#     github.com/ihsansencan/iDirScan  #
#                @IhsanSencan          #
########################################

usage: iDirScan.py [-h] -s site -l file
iDirScan.py: error: the following arguments are required: -s/--site, -l/--list

root@ihsan:~/Desktop# python3 iDirScan.py -s localhost -l common.txt

########################################
#        +-+-+-+-+-+-+-+-+-+-+-+-+     #
#        |*|*|i|D|i|r|S|c|a|n|*|*|     #
#        +-+-+-+-+-+-+-+-+-+-+-+-+     #
#     github.com/ihsansencan/iDirScan  #
#                @IhsanSencan          #
########################################

In total 4614 trying will be done.
*************************
[0] http://localhost/ (Code:200|Size:1111)
[9] http://localhost/.hta (Code:403|Size:1021)
[9] http://localhost/.htaccess (Code:403|Size:1021)
[9] http://localhost/.htpasswd (Code:403|Size:1021)
[281] http://localhost/admin (Code:401|Size:1263)
[814] http://localhost/cgi-bin/ (Code:403|Size:1035)
[2947] http://localhost/phpmyadmin (Code:200|Size:9133)
[4607] http://localhost/ (Code:200|Size:1111)
*************************
It took 0:00:12 seconds in total.
root@ihsan:~/Desktop# 
```