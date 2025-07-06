def ip_to_binary(ip_address):
    # Split the IP address into octets
    octets = ip_address.split('.')
    
    # Convert each octet to binary and format it to 8 bits
    binary_octets = [format(int(octet), '08b') for octet in octets]
    
    # Join the binary octets with dots
    binary_ip = '.'.join(binary_octets)
    
    return binary_ip

# Example IP address
ip = "192.168.5.7"
binary = ip_to_binary(ip)

print(f"IP Address: {ip}")
print(f"Binary: {binary}") 