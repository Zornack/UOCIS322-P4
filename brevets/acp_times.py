"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    maxToTwohundred = 34
    maxToFourhundred = 32
    maxToSixhundred = 30
    maxToOnethousand = 28

    if control_dist_km < 0:
        return None

    control_dist_km = round(control_dist_km)

    if control_dist_km > brevet_dist_km:
        control_dist_km = brevet_dist_km

    h = 0
    m = 0

    if control_dist_km > 600:
        above = control_dist_km - 600
        remainder = above % maxToOnethousand
        h = h + ( above - remainder) / maxToOnethousand
        m = m + ((remainder / maxToOnethousand) * 60)
        control_dist_km = control_dist_km - above
    if control_dist_km > 400:
        above = control_dist_km - 400
        remainder = above % maxToSixhundred
        h = h + (above - remainder) / maxToSixhundred
        m = m + ((remainder / maxToSixhundred) * 60)
        control_dist_km = control_dist_km - above
    if control_dist_km > 200:
        above = control_dist_km - 200
        remainder = above % maxToFourhundred
        h = h + (above - remainder) / maxToFourhundred
        m = m + ((remainder / maxToFourhundred) * 60)
        control_dist_km = control_dist_km - above
    if control_dist_km <= 200:
        remainder = control_dist_km % maxToTwohundred
        h = h + (control_dist_km - remainder) / maxToTwohundred
        m = m + ((remainder / maxToTwohundred) * 60)

    m = round(m)

    return arrow.get(brevet_start_time).shift(hours=+h, minutes=+m)


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """

    minToTwohundred = 15
    minToFourhundred = 15
    minToSixhundred = 15
    minToOnethousand = 11.428

    control_dist_km = round(control_dist_km)

    h = 0
    m = 0

    if control_dist_km < 0:
        return None

    if control_dist_km <= 60:
        remainder = control_dist_km % 20
        h = h + (control_dist_km - remainder) / 20 + 1
        m = m + round((remainder / 20) * 60)
        return arrow.get(brevet_start_time).shift(hours=+h, minutes=+m)

    if control_dist_km >= brevet_dist_km:
        if brevet_dist_km == 1000:
            h = 75
        if brevet_dist_km == 600:
            h = 40
        if brevet_dist_km == 400:
            h = 27
        if brevet_dist_km == 300:
            h = 20
        if brevet_dist_km == 200:
            h = 13
            m = 30
        return arrow.get(brevet_start_time).shift(hours=+h, minutes=+m)

    if control_dist_km > 600:
        above = control_dist_km - 600
        remainder = above % minToOnethousand
        h = h + (above - remainder) / minToOnethousand
        m = m + round((remainder / minToOnethousand) * 60)
        control_dist_km = control_dist_km - above
    if control_dist_km > 400:
        above = control_dist_km - 400
        remainder = above % minToSixhundred
        h = h + (above - remainder) / minToSixhundred
        m = m + round((remainder / minToSixhundred) * 60)
        control_dist_km = control_dist_km - above
    if control_dist_km > 200:
        above = control_dist_km - 200
        remainder = above % minToFourhundred
        h = h + (above - remainder) / minToFourhundred
        m = m + round((remainder / minToFourhundred) * 60)
        control_dist_km = control_dist_km - above
    if control_dist_km <= 200:
        remainder = control_dist_km % minToTwohundred
        h = h + (control_dist_km - remainder) / minToTwohundred
        m = m + round((remainder / minToTwohundred) * 60)

    m = round(m)

    return arrow.get(brevet_start_time).shift(hours=+h, minutes=+m)
