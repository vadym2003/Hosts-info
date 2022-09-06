import socket
import geocoder
import whois

fo = open("HostsData.txt", "w")

print('\033[1;32;40mEnter Domain Names \nTo quit enter - esc')
print('\033[1;37;40m')

while(True):
    try:
        server_name = str(input())
        server_info = whois.whois(server_name)
    except Exception:
        print('\033[1;31;40mThe domain cannot be reached\nTry another domain')
        print('\033[1;37;40m')        
        continue
    else:
        if(server_name != 'esc'):
            server_ip = socket.gethostbyname(server_name)
            server_loc = geocoder.ip(server_ip)
        
            out = server_name+', '+str(server_info.registrar)+', '+server_loc.city+', '+str(server_info.creation_date)+', '+str(server_info.expiration_date)+'\n'
            fo.write(out)
        else:
            break
    
fo.close()
    