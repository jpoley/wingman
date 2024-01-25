package main

import (
	"crypto/tls"
	"fmt"
	"net"
	"time"
)

func main() {
	cidr := "192.168.0.0/24"
	secondFunction := func(ip net.IP) {
		// DNS lookup
		names, err := net.LookupAddr(ip.String())
		if err != nil {
			fmt.Println("DNS lookup failed:", err)
			return
		}

		// Print result
		fmt.Println("DNS lookup result for", ip.String(), ":", names)

		thirdFunction(names[0])
	}

	ip, ipNet, err := net.ParseCIDR(cidr)
	if err != nil {
		fmt.Println("Invalid CIDR range:", err)
		return
	}

	for ip := ip.Mask(ipNet.Mask); ipNet.Contains(ip); inc(ip) {
		go func(ip net.IP) {
			address := fmt.Sprintf("%s:443", ip.String())
			conn, err := net.DialTimeout("tcp", address, 2*time.Second)
			if err == nil {
				conn.Close()
				fmt.Println("FOUND")
				secondFunction(ip)
			} else {
				fmt.Println("Trying", address)
			}
		}(ip)
	}

	time.Sleep(5 * time.Second)
}

func thirdFunction(dnsName string) {
	// Connect to the TLS endpoint
	conn, err := tls.Dial("tcp", dnsName+":443", nil)
	if err != nil {
		fmt.Println("TLS connection failed:", err)
		return
	}
	defer conn.Close()

	// Get the certificate
	cert := conn.ConnectionState().PeerCertificates[0]

	// Print certificate expiration
	fmt.Println("Certificate expiration:", cert.NotAfter)

}

func inc(ip net.IP) {
	for j := len(ip) - 1; j >= 0; j-- {
		ip[j]++
		if ip[j] > 0 {
			break
		}
	}
}
