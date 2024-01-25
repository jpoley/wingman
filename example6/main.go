package main

import (
	"crypto/tls"
	"fmt"
	"net/http"
	"time"
)

func checkCertificate(url string) {
	// Disable certificate verification to get all the certificate details
	tr := &http.Transport{
		TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
	}

	client := &http.Client{Transport: tr, Timeout: 10 * time.Second}

	resp, err := client.Get(url)
	if err != nil {
		fmt.Printf("Error connecting to %s: %s\n", url, err)
		return
	}
	defer resp.Body.Close()

	cert := resp.TLS.PeerCertificates[0]
	fmt.Printf("Certificate details for %s:\n", url)
	fmt.Printf("Subject: %s\n", cert.Subject.CommonName)
	fmt.Printf("Issuer: %s\n", cert.Issuer.CommonName)
	fmt.Printf("Expiration: %s\n", cert.NotAfter)
	fmt.Printf("Serial Number: %s\n", cert.SerialNumber)
	fmt.Printf("Signature Algorithm: %s\n", cert.SignatureAlgorithm)
	fmt.Printf("Public Key Algorithm: %s\n", cert.PublicKeyAlgorithm)
}

func main() {
	urls := []string{
		"https://www.google.com",
		"https://www.github.com",
		"https://www.microsoft.com",
		"https://www.apple.com",
		"https://www.amazon.com",
	}

	for _, url := range urls {
		checkCertificate(url)
		fmt.Println()
	}
}
