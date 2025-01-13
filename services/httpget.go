package services

import (
	"fmt"
	"net/http"
	"strings"
)

// HttpGet is a service that sends a GET request to a URL
// It has a URL, headers, and payload
type HttpGet struct {
	url     string
	headers map[string]string
	payload string
}

// NewHttpGet creates a new HttpGet service
// It requires a URL and can take headers and a payload
func (h *HttpGet) buildRequest() (*http.Request, error) {
	req, err := http.NewRequest("GET", h.url, strings.NewReader(h.payload))
	if err != nil {
		fmt.Println("HTTPGET: Error creating request")
		return nil, err
	}

	for k, v := range h.headers {
		req.Header.Set(k, v)
	}

	return req, nil
}

// Execute sends a GET request to the specified URL
func (h *HttpGet) Execute(message string) (err error) {
	req, err := h.buildRequest()
	if err != nil {
		return err
	}

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		fmt.Println("HTTPGET: Error sending request")
		return err
	}

	defer resp.Body.Close()

	return nil
}
