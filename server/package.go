package server

import (
	"errors"

	crc "git.barfuss.email/jan/crc16"
	"github.com/LeRoid-hub/updog/notify"
	"github.com/LeRoid-hub/updog/services"
)

type Package struct {
	server   *Server
	services *services.Services
	notifier *notify.Notifier
	crc      uint16
}

func (p *Package) serialize() (payload []byte, err error) {
	payload = make([]byte, 0)
	return payload, nil
}

func (p *Package) deserialize() {

}

func (p *Package) Encrypt() (payload []byte, err error) {
	payload, err = p.serialize()
	if err != nil {
		return nil, err
	}

	check := crc.Calculate([]byte(payload))

	payload = append(payload, byte(check))

	return payload, nil
}

func (p *Package) Decrypt(payload []byte) error {
	check := crc.Calculate([]byte(payload))
	if check != uint16(payload[len(payload)-2]) {
		return errors.New("checksum failed")
	}

	p.deserialize()
	return nil
}
