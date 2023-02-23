## Working with Network Mapper (NMAP)  

    man nmap  ---> will display the Manual for NMAP  

    nmap -n -sn <Subnet IP>   ---> ARP Scan for a particular subnet without name resolution  (Passive Scan)

    nmap -sT -p1-1000 -Tinsane <Subnet IP>  ---> Connect Scan for the first 1000 ports (Active Scan)

    nmap -sT <IP Addr>  ---> TCP Connect Scan on a Single Host

    nmap -sV -P0 <IP Addr> ---> Get the version without Pinging the Host

    nmap -V -iR 10000 -Pn -p 80   ---> Generate random IP Addr and scan for port 80  


## Banner Grabbing  

Active Banner Grabbing  ---> Sending traffic to the system and analysing responses to deduce the version information   

    telnet <IP Addr> 22  ---> will give us a clue about the version of SSH running   
    telnet example.com 80  ---> will show great information  
    nc example.com 80 ---> Using Netcat to get information  
    nmap -sV --script=banner -p 80 example.com  

***info***  
{Escape character is "^]"  and quit to exit telnet}  

Passive Banner Grabbing  ---> Determine Application and Version information from source such Packet Captures  



## Countermeasures

-- Set false banners (Security through Obscurity)       

    Apache configure Apache2.conf:  
        ServerSignature Off <Don't display server version on error page or generated pages>  
        ServerTokens Prod  <Return Only "Apache" in the server header>  
    
    Apache mod_headers:  
        set Server "LionOs 1.2"  
    
    IIS:  
        IIS Lockdown Wizard - https://microsoft.com  
        Disable unnecessary services  
    



## Useful Linux Commands for Admin
cat /etc/services ---> to display various services running on a linux box  
grep 515 /etc/services