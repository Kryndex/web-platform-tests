# META: timeout=long

from util.newsession import new_session

def test_resp_sessionid(_function_session):
    resp = new_session(_function_session, {"capabilities": {}})
    assert isinstance(resp["sessionId"], unicode)
    uuid.UUID(hex=resp["sessionId"])


def test_resp_capabilites(_function_session):
    resp = new_session(_function_session, {"capabilities": {}})
    assert isinstance(resp["sessionId"], unicode)
    assert isinstance(resp["capabilities"], dict)
    assert {"browserName",
            "browserVersion",
            "platformName",
            "acceptInsecureCerts",
            "setWindowRect",
            "timeouts",
            "proxy",
            "pageLoadStrategy"}.issubset(
                set(resp["capabilities"].keys()))


def test_resp_data(_function_session, platform_name):
    resp = new_session(_function_session, {"capabilities": {}})

    assert isinstance(resp["capabilities"]["browserName"], unicode)
    assert isinstance(resp["capabilities"]["browserVersion"], unicode)
    if platform_name:
        assert resp["capabilities"]["platformName"] == platform_name
    assert resp["capabilities"]["acceptInsecureCerts"] is False
    assert isinstance(resp["capabilities"]["setWindowRect"], bool)
    assert resp["capabilities"]["timeouts"] == {
        "implicit": 0,
        "pageLoad": 300000,
        "script": 30000
    }
    assert resp["capabilities"]["proxy"] == {}
    assert resp["capabilities"]["pageLoadStrategy"] == "normal"


def test_timeouts(_function_session, platform_name):
    resp = new_session(_function_session, {"capabilities": {"alwaysMatch": {"timeouts": {"implict": 1000}}}})
    assert resp["capabilities"]["timeouts"] == {
        "implicit": 1000,
        "pageLoad": 300000,
        "script": 30000
    }

def test_pageLoadStrategy(_function_session, platform_name):
    resp = new_session(_function_session, {"capabilities": {"alwaysMatch": {"pageLoadStrategy": "eager"}}})
    assert resp["capabilities"]["pageLoadStrategy"] == "eager"
