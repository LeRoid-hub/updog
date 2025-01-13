package services

type Service interface {
	Execute(message string) error
}

type Services struct {
	Services []Service
}
