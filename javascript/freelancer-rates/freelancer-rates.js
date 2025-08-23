// @ts-check
//
// ☝🏽 The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion on the web
// and supported IDEs when implementing this exercise. You don't need to
// understand types, JSDoc, or TypeScript in order to complete this JavaScript
// exercise, and can completely ignore this comment block and directive.

// 👋🏽 Hi again!
//
// A quick reminder about exercise stubs:
//
// 💡 You're allowed to completely clear any stub before you get started. Often
// we recommend using the stub, because they are already set-up correctly to
// work with the tests, which you can find in ./freelancer-rates.spec.js.
//
// 💡 You don't need to write JSDoc comment blocks yourself; it is not expected
// in idiomatic JavaScript, but some companies and style-guides do enforce them.
//
// Get those rates calculated!

/**
 * The number of hours being worked per day.
 */
const HOURLY_RATE = 8;

/**
 * The number of billable days per month.
 */
const BILLABLE_DAYS = 22;

/**
 * The day rate, given a rate per hour
 *
 * @param {number} ratePerHour
 * @returns {number} the rate per day
 */
export function dayRate(ratePerHour) {
  return HOURLY_RATE * ratePerHour;
}

/**
 * The month rate, given a rate per hour
 *
 * @param {number} ratePerHour
 * @returns {number} the rate per month
 */
export function monthRate(ratePerHour) {
  return dayRate(ratePerHour) * BILLABLE_DAYS;
}

/**
 * Calculates the number of days in a budget, rounded down
 *
 * @param {number} budget: the total budget
 * @param {number} ratePerHour: the rate per hour
 * @returns {number} the number of days
 */
export function daysInBudget(budget, ratePerHour) {
  return Math.floor(budget / dayRate(ratePerHour));
}

/**
 * Calculates the month rate with discount, given a rate per hour and the discount
 *
 * @param {number} ratePerHour
 * @param {number} discount: for example 20% written as 0.2
 * @returns {number} the discounted rate
 */
export function monthRateWithDiscount(ratePerHour, discount) {
  let rate = monthRate(ratePerHour);
  let rateDiscount = rate * discount;

  return rate - rateDiscount;
}

/**
 * Calculates the discounted rate for large projects, rounded up
 *
 * @param {number} ratePerHour
 * @param {number} numDays: number of days the project spans
 * @param {number} discount: for example 20% written as 0.2
 * @returns {number} the rounded up discounted rate
 */
export function priceWithMonthlyDiscount(ratePerHour, numDays, discount) {
  let workingMonths = Math.floor(numDays / BILLABLE_DAYS);
  let workingDays = Math.floor(numDays % BILLABLE_DAYS);
  let months = monthRateWithDiscount(ratePerHour, discount) * workingMonths;
  let days = dayRate(ratePerHour) * workingDays;

  return Math.ceil(months + days);
}
