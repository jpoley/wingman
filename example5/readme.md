write a go applicaiton that can scan an entire CIDR range of IPs and checks for https (port 443) it should print trying, and then FOUND when found, and call second_function

write second_function that will do a dns lookup on the ip address and then pass the code on to a third_function after printing the result

write third function taking a dns name and calling the TLS endpoint and checking what the certificate expiration is on it
