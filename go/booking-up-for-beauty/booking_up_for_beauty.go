package booking

import "time"

// Schedule returns a time.Time from a string containing a date.
func Schedule(date string) time.Time {
	const layout = "1/2/2006 15:04:05"
	t, _ := time.Parse(layout, date)
	return t
}

// HasPassed returns whether a date has passed.
func HasPassed(date string) bool {
	const layout = "January 2, 2006 15:04:05"
	t, _ := time.Parse(layout, date)
	return time.Now().After(t)
}

// IsAfternoonAppointment returns whether a time is in the afternoon.
func IsAfternoonAppointment(date string) bool {
	const layout = "Monday, January 2, 2006 15:04:05"
	t, _ := time.Parse(layout, date)
	h := t.Hour()
	return h >= 12 && h <= 18
}

// Description returns a formatted string of the appointment time.
func Description(date string) string {
	const layout = "Monday, January 2, 2006, at 15:04."
	t := Schedule(date)
	return "You have an appointment on " + t.Format(layout)
}

// AnniversaryDate returns a Time with this year's anniversary.
func AnniversaryDate() time.Time {
	y, _, _ := time.Now().Date()
	return time.Date(y, time.September, 15, 0, 0, 0, 0, time.UTC)
}
