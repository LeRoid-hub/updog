package notify

import (
	b64 "encoding/base64"
	"fmt"
	"net/http"
	"net/url"
	"strings"
)

// Ntfy is a struct that holds the URL, token, username, and password for a notification
// It has a Send method that sends a message to the specified URL
type Ntfy struct {
	url      string
	token    string
	username string
	password string
}

// Sends a message to the specified URL
// If a token is provided, it will be used as the Authorization header
// If a username and password are provided, they will be used for basic auth
// If neither are provided, the message will be sent as the request body
func (n *Ntfy) Send(message string) {
	_, err := url.ParseRequestURI(n.url)
	if err != nil {
		fmt.Println("NTFY: Invalid URL")
		return
	}

	if message == "" {
		fmt.Println("NTFY: Empty message")
		return
	}

	if n.token != "" {
		n.sendToken(message)
	} else if n.username != "" && n.password != "" {
		n.sendUserPass(message)
	} else {
		n.sendUrl(message)
	}

}

func (n *Ntfy) sendToken(message string) {
	req, err := http.NewRequest("POST", n.url, strings.NewReader(message))
	if err != nil {
		fmt.Println("NTFY: Error creating request")
		return
	}

	req.Header.Set("Authorization", "Bearer "+n.token)
	http.DefaultClient.Do(req)
}

func (n *Ntfy) sendUserPass(message string) {
	auth := b64.StdEncoding.EncodeToString([]byte(n.username + ":" + n.password))
	auth = "Basic " + auth

	req, err := http.NewRequest("POST", n.url, strings.NewReader(message))
	if err != nil {
		fmt.Println("NTFY: Error creating request")
		return
	}

	req.Header.Set("Authorization", auth)
	http.DefaultClient.Do(req)
}

func (n *Ntfy) sendUrl(message string) {
	req, err := http.NewRequest("POST", n.url, strings.NewReader(message))
	if err != nil {
		fmt.Println("NTFY: Error creating request")
		return
	}

	http.DefaultClient.Do(req)
}
