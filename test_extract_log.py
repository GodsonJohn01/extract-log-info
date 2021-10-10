import pytest
from extract_log import Systemlog


sl = Systemlog()

@pytest.fixture
def log_data_1():
    """
    This is the log data for test case 1
    """
    return 'SAC:0|Sacumen|CAAS|2021.2.0|3|MALICIOUS|High|cat=C2 cs1Label=subcat cs1=DNS_TUNNELING cs2Label=vueUrls cs2=https://aws-dev.sacdev.io/alerts?filter=alertId%3D%3D81650 cs3Label=Tags cs3=USA,Finance cs4Label=Url cs4=https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=9739323 cn1Label=severityScore cn1=900 msg=Malicious activity was reported in CAAS\= A threat intelligence rule has been automatically created in DAAS. dhost=bad.com dst=1.1.1.1'


@pytest.fixture
def log_data_2():
    """
    This is the log data for test case 2
    """
    return 'SAC:0|Sacumen|CAAS|2021.2.0|3|MALICIOUS|High|cat=C5 cs1Label=subcat cs1=DNS_TUNNELING cs2Label=vueUrls cs2=https://aws-dev.sacdev.io/alerts?filter=alertId%3D%3D70077 cs3Label=Tags cs3=USA,Finance cs4Label=Url cs4=https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=3200111 cn1Label=severityScore cn1=700 msg=Malicious activity was reported in CAAS\= A threat intelligence rule has been automatically created in DAAS. dhost=bad.com dst=1.1.2.3'


def test_read_log_1(log_data_1):
    """
    Test case for the read_log method
    """
    data_1 = sl.read_log()
    assert data_1 == log_data_1


def test_parse_log_1(log_data_1, log_data_2):
    """
    Test case for the parse_log method with two different data sets
    """
    data_1 = sl.parse_log(log_data_1)
    data_2 = sl.parse_log(log_data_2)
    assert data_1 == {
        'cat': 'C2',
        'cs1Label': 'subcat',
        'cs1': 'DNS_TUNNELING',
        'cs2Label': 'vueUrls',
        'cs3Label': 'Tags',
        'cs3': 'USA,Finance',
        'cs4Label': 'Url',
        'cs4': 'https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=9739323',
        'cn1Label': 'severityScore',
        'cn1': 900,
        'msg': 'Malicious activity was reported in CAAS\\= A threat intelligence rule has been automatically created in DAAS',
        'dhost': 'bad.com',
        'dst': '1.1.1.1',
    }

    assert data_2 == {
        'cat': 'C5',
        'cs1Label': 'subcat',
        'cs1': 'DNS_TUNNELING',
        'cs2Label': 'vueUrls',
        'cs3Label': 'Tags',
        'cs3': 'USA,Finance',
        'cs4Label': 'Url',
        'cs4': 'https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=3200111',
        'cn1Label': 'severityScore',
        'cn1': 700,
        'msg': 'Malicious activity was reported in CAAS\\= A threat intelligence rule has been automatically created in DAAS',
        'dhost': 'bad.com',
        'dst': '1.1.2.3',
    }
