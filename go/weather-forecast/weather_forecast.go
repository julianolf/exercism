// Package weather implements utility routines for Goblinocus forecasting.
package weather

// CurrentCondition stores current weather condition.
var CurrentCondition string

// CurrentLocation stores current city name.
var CurrentLocation string

// Forecast returns a formated string for the given city and weather.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
