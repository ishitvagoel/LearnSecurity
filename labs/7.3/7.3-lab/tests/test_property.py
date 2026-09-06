import hashlib
import hmac

LAB_SECRET = "lab-secret"
LAB_BODY = "body"


def test_missing_signature_is_rejected(impl):
    assert impl.accept("", LAB_BODY, LAB_SECRET) is False


def test_wrong_signature_is_rejected(impl):
    assert impl.accept("0" * 64, LAB_BODY, LAB_SECRET) is False


def test_matching_signature_is_accepted(impl):
    sig = hmac.new(LAB_SECRET.encode(), LAB_BODY.encode(), hashlib.sha256).hexdigest()
    assert impl.accept(sig, LAB_BODY, LAB_SECRET) is True
