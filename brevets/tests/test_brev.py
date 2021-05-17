from acp_times import open_time, close_time

import nose
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

#Tests a normal 125km control point on a 200 brevet.
def test_125_200():
    assert open_time(125,200,'2021-01-01T00:00').format('YYYY-MM-DDTHH:mm') == '2021-01-01T03:41'
    assert close_time(125,200,'2021-01-01T00:00').format('YYYY-MM-DDTHH:mm') == '2021-01-01T08:20'

#Tests a short 50km control which uses a seperate algoritihm.
def test_50_600():
    assert open_time(50, 600, '2021-01-01T00:00').format('YYYY-MM-DDTHH:mm') == '2021-01-01T01:28'
    assert close_time(50, 600, '2021-01-01T00:00').format('YYYY-MM-DDTHH:mm') == '2021-01-01T03:30'

#Tests negative distances.
def test_negative():
    assert open_time(-235, 300, '2021-01-01T00:00') == None
    assert close_time(-558, 300, '2021-01-01T00:00') == None

#Tests various control distances which are more than the brevet distance.
def test_over_total():
    assert open_time(215,200,'2021-01-01T00:00').format('YYYY-MM-DDTHH:mm') == '2021-01-01T05:53'
    assert close_time(215, 200, '2021-01-01T00:00').format('YYYY-MM-DDTHH:mm') == '2021-01-01T13:30'
    assert open_time(500, 400, '2021-01-01T00:00').format('YYYY-MM-DDTHH:mm') == '2021-01-01T12:08'
    assert close_time(500, 400, '2021-01-01T00:00').format('YYYY-MM-DDTHH:mm') == '2021-01-02T03:00'
    assert open_time(1050, 1000, '2021-01-01T00:00').format('YYYY-MM-DDTHH:mm') == '2021-01-02T09:05'
    assert close_time(1050, 1000, '2021-01-01T00:00').format('YYYY-MM-DDTHH:mm') == '2021-01-04T03:00'

#Tests a long control distance which uses all four min and max speeds.
def test_910_1000():
    assert open_time(910, 1000, '2021-01-01T00:00').format('YYYY-MM-DDTHH:mm') == '2021-01-02T05:52'
    assert close_time(910, 1000, '2021-01-01T00:00').format('YYYY-MM-DDTHH:mm') == '2021-01-03T19:08'

#Tests rounding of decimial distances
def test_decimils():
    assert open_time(417.4, 600, '2021-01-01T00:00').format('YYYY-MM-DDTHH:mm') == '2021-01-01T12:42'
    assert close_time(417.4, 600, '2021-01-01T00:00').format('YYYY-MM-DDTHH:mm') == '2021-01-02T03:48'
    assert open_time(93.5, 300, '2021-01-01T00:00').format('YYYY-MM-DDTHH:mm') == '2021-01-01T02:46'
    assert close_time(93.5, 300, '2021-01-01T00:00').format('YYYY-MM-DDTHH:mm') == '2021-01-01T06:16'
