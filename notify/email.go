package notify

import (
	"fmt"

	"gopkg.in/mail.v2"
)

// Email is a struct that holds the information needed to send an email
// It has a Send method that sends an email with the specified subject and body
// to the specified recipients
type Email struct {
	from       string
	to         []string
	port       int
	smtpServer string
	username   string
	userpass   string
}

// Send sends an email with the specified subject and body
// to the specified recipients
func (e *Email) Send(subject string, body string) {
	// Check if all the required information is provided
	if body == "" || subject == "" || len(e.to) == 0 ||
		e.from == "" || e.smtpServer == "" || e.username == "" ||
		e.userpass == "" || e.port == 0 || body == "" {

		fmt.Println("EMAIL: Missing information")
		return
	}

	// Set the subject and body
	m := mail.NewMessage()
	m.SetHeader("From", e.from)
	m.SetHeader("To", e.to...)
	m.SetHeader("Subject", subject)
	m.SetBody("text/plain", body)

	// Create a new dialer to send the email
	d := mail.NewDialer(e.smtpServer, e.port, e.username, e.userpass)
	d.StartTLSPolicy = mail.MandatoryStartTLS

	// Send the email
	if err := d.DialAndSend(m); err != nil {
		fmt.Println("EMAIL: Error sending email " + err.Error())
	}

}
