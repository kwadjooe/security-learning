### - IP QUERIES 

---
    addr  ---> Display IP Addresses and property information (abbreviation of address)  

    ip addr  --->  Show information for all addresses  

    ip addr show dev eth0  ---> Display information only for device eth0  

    link  --->  Manage and display the state of all network interfaces

    ip link  --->  Show information for all interfaces  

    ip link show dev eth0  --->  Display information only for device eth0  

    ip -s link  --->  Display interface statistics  

    route  --->  Display and alter the routing table   

    ip route  --->  List all of the route entries in the kernel   

    maddr   --->  Manage and display multicast IP addresses  

    ip maddr  --->  Display multicast information for all devices  

    ip maddr show dev eth0  --->  Display multicast information for device eth0  

    neigh  --->  Show neighbour objects; this is also known as the ARP table for IPv4  

    ip neigh  --->  Display neighbour objects  

    ip neigh show dev eth0  --->  Show the ARP cache for device eth0  

    help  --->   Display a list of commands and arguments for each subcommand  

    ip help  --->   Display ip commands and arguments  

    ip addr help  --->   Display address commands and arguments  

    ip link help  --->   Display link commands and arguments  

    ip neigh help  --->  Display neighbour commands and arguments  
---

#### – FILE PERMISSIONS
Linux chmod example
        PERMISSION      EXAMPLE

         U   G   W
        rwx rwx rwx     chmod 777 filename
        rwx rwx r-x     chmod 775 filename
        rwx r-x r-x     chmod 755 filename
        rw- rw- r--     chmod 664 filename
        rw- r-- r--     chmod 644 filename

#### NOTE: Use 777 with caution !

        LEGEND
        U = User
        G = Group
        W = World

        r = Read
        w = write
        x = execute
        - = no access your **content** *here*

