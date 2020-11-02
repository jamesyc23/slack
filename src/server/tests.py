import pytest
import db

def test_create_channel():
    cid_A = db.create_channel("A")
    assert (cid_A, "A") in db.list_channels(), "created channel not found."

def test_add_user_to_channel():
    cid_B = db.create_channel("B")
    db.add_user_to_channel(cid_B, 10)
    assert (cid_B, "B") in db.get_channels_for_user(10), "added user not found"

def test_send_message():
    db.send_message(100, 101, "Test Message.")
    
    msg = db.get_messages(100, 1)[0]
    assert msg[0] == 101 and msg[2] == "Test Message."