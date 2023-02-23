## Working with Network Mapper (NMAP)  

nmap -n -sn <Subnet IP>   ---> ARP Scan for a particular subnet without name resolution  (Passive Scan)

nmap -sT -p1-1000 -Tinsane <Subnet IP>  ---> Connect Scan for the first 1000 ports (Active Scan)






## Useful Linux Commands for Admin
cat /etc/services ---> to display various services running on a linux box