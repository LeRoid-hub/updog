package notify

// Notify is an interface for sending notifications
type Notify interface {
	Send(message string)
}

type Notifier struct {
	notifier []Notify
}

// SendNotification sends a notification
func SendNotification(n Notify, message string) {
	n.Send(message)
}

func (n *Notifier) AddNotifier(notify Notify) {
	n.notifier = append(n.notifier, notify)
}

func (n *Notifier) RemoveNotifier(notify Notify) {
	var newNotifier []Notify
	for _, notifier := range n.notifier {
		if notifier != notify {
			newNotifier = append(newNotifier, notifier)
		}
	}
	n.notifier = newNotifier
}

func (n *Notifier) SendNotification(message string) {
	for _, notifier := range n.notifier {
		notifier.Send(message)
	}
}
