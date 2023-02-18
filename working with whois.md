# This document explore various usage of the WHOIS and DNS tool
-----------------------------------------------------------
WHOIS Protocol                                             |
-----------------------------------------------------------
whois.afrinic.net  --> Africa  
whois.aspnic.net   --> Asia Pacific, India, China and Australia  
whois.arin.net     --> US and Canada  
whois.lacnic.net   --> Mexico and Latin America  
whois.ripe.net     --> Europe, Greenland, Russian and Middle East  
-----------------------------------------------------------
---------------------------
DNS Reconnaissance Tools  |  
---------------------------
nslookup  
dig   
Nmap DNS  
NSE Scripts   Zone transfer  
DNSRecon   include wordlist for DNS brute force, advanced feature include DNSSEC and mDNS   support.
Metasploit DNS functionality found in information gathering auxiliary modules, including reverse brute force.  

DIG Synthax and Options  

-t any --->  lookup all records  
-t mx  --->  lookup mail record only  
-t axfr--->  attempts a zone transfer  

-x <IP addres­s> ---> Simplified PTR (reverse) lookup  
 <IP addres­s>.i­n-­add­r.arpa PTR ---> PTR record search in old days  
dig @10.1­.30.8 versio­n.bind chaos txt ---> Query the namese­rver's version of BIND  


 ------
| NMAP |  
 ------

dns-zo­ne-­tra­nsfer  
DNS zone transfer  
dns-brute  
DNS brute force, useful for CNAME discovery   
 -sL <IP range> | grep \)  
Reverse DNS scan  
To use an custom word list: nmap --scri­pt=­<script name> <do­mai­n> (optional)  --scri­pt-­arg­s=d­ns-­bru­te.h­os­tli­st=­<path to file.t­xt>  

 ----------
| DNSRecon |  
 ----------
   
 -h --help --> Show this help mesasge and exit  
 -d --domain <do­mai­n> --> Domain to Target for enumer­ation  
 -r --range <IP range> --> IP Range for reverse lookup brute force  
 -n --name­_server <na­me> --> Domain server to use  
 -D --dict­ionary <fi­le> --> Dictionary file to use for brute force  
 -t --type <ty­pes> --> Specify the type of enumer­ation to perform  
 -a --> Perform AXFR with standard enumer­ation  
 -s --> Reverse Look-up for IPv4 ranges in SPF Records  
 -g --> Perform Google enumer­ation  
 -w --> Do deep whois analysis and reverse look-up  
 -z --> Performs a DNSSEC Zone Walk  

Usage: dnsrec­on.py <op­tio­ns>  

 ------------
| Metasploit |
 ------------

auxili­ary­/ga­the­r/d­ns_­bru­teforce  
Performs a brute force dictionary DNS scan  
auxili­ary­/ga­the­r/d­ns_­cac­he_­scraper  
Queries DNS cache for previously resolved names  
auxili­ary­/ga­the­r/d­ns_info  
Gathers general DNS inform­ation  
auxili­ary­/ga­the­r/d­ns_­rev­ers­e_l­ookup  
Performs a reverse DNS (PTR) scan of a netblock, replicates DNSRecon's reverse brute force  
auxili­ary­/ga­the­r/d­ns_­srv­_enum  
Enumerates SRV (Server) records 

---------
recon-ng |    
----------
by default no module is installed. Use  
marketplace search --> to search for various module  

