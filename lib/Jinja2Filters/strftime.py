# THIS FILE IS PART OF THE CYLC SUITE ENGINE.
# Copyright (C) 2008-2017 NIWA
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Provides a Jinja2 filter for formatting ISO8601 datetime strings."""

from isodatetime.parsers import TimePointParser


def strftime(iso8601_datetime, strftime):
    """Format an iso8601 datetime string using an strftime string.

    Args:
        iso8601_datetime (str): Any valid ISO8601 datetime as a string.
        strftime (str): Any valid strftime string.

    Return:
        The result of applying the strftime to the iso8601_datetime

    Raises:
        ISO8601SyntaxError: In the event of an invalid datetime string.
        StrftimeSyntaxError: In the event of an invalid strftime string.

    Examples:
        >>> strftime('2000-01-01T00Z', '%H')
        '00'
        >>> strftime('2000', '%H')
        '00'
        >>> strftime('2000', '%Y/%m/%d %H:%M:%S')
        '2000/01/01 00:00:00'
        >>> strftime('10661014T08+01', '%z')  # Timezone offset.
        '+0100'
        >>> strftime('10661014T08+01', '%j')  # Day of the year
        '287'
        >>> try:
        ...     strftime('invalid', '%H')  # Invalid datetime.
        ... except Exception as exc:
        ...     print type(exc)
        <class 'isodatetime.parsers.ISO8601SyntaxError'>
        >>> try:
        ...     strftime('2000', '%invalid')  # Invalid strftime
        ... except Exception as exc:
        ...     print type(exc)
        <class 'isodatetime.parser_spec.StrftimeSyntaxError'>
    """
    return TimePointParser().parse(iso8601_datetime).strftime(strftime)
