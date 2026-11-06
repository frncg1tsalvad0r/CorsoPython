import sys
import stdlibrsedg.stdio as stdio

year = int(sys.argv[1])
is_leap_year = (year % 4 == 0)
is_leap_year = is_leap_year and ((year % 100) != 0)
is_leap_year = is_leap_year or ((year % 400) == 0)

stdio.writeln(is_leap_year)