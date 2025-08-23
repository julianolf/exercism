package BookingUpForBeauty;

use v5.38;

use Time::Piece;
use Readonly;

use Exporter ('import');
our @EXPORT_OK = ('appointment_has_passed', 'is_afternoon_appointment', 'describe_appointment');

my $STRPTIME_FORMAT = '%Y-%m-%d' . 'T' . '%H:%M:%S';
Readonly::Scalar $STRPTIME_FORMAT => $STRPTIME_FORMAT;

sub _parse_datetime ($date_string) {
    return Time::Piece->strptime($date_string, $STRPTIME_FORMAT);
}

sub appointment_has_passed ($date_string) {
    my $time = _parse_datetime($date_string);
    my $now = localtime;
    return $time < $now;
}

sub is_afternoon_appointment ($date_string) {
    my $time = _parse_datetime($date_string);
    return $time->hour >= 12 && $time->hour < 18;
}

sub describe_appointment ($date_string) {
    my $time = _parse_datetime($date_string);
    my $date = $time->mdy("/");
    my $hour = $time->hour == 0 ? 12 : $time->hour % 12;
    my $minute = $time->min;
    my $xm = $time->hour < 12 ? 'AM' : 'PM';

    return sprintf('You have an appointment on %s %d:%02d %s', $date, $hour, $minute, $xm);
}
