import sqlite3
import random
import time

def get_new_cid():
    r = random.randint(0, 2**31)
    return r

def create_channel(name):
    conn = sqlite3.connect('slack.db')
    c = conn.cursor()
    
    cid = get_new_cid()
    channel_value = (cid, name)
    c.execute("INSERT INTO channels (channel_id, name) VALUES (?, ?)", channel_value)

    conn.commit()
    conn.close()

    return cid

def list_channels():
    conn = sqlite3.connect('slack.db')
    c = conn.cursor()
    
    channels = [row for row in c.execute('SELECT * FROM channels')]

    conn.commit()
    conn.close()

    return channels

def add_user_to_channel(cid, uid):
    conn = sqlite3.connect('slack.db')
    c = conn.cursor()
    
    membership_value = (cid, uid)
    c.execute("INSERT INTO memberships (channel_id, user_id) VALUES (?, ?)", membership_value)

    conn.commit()
    conn.close()

def get_channels_for_user(uid):
    conn = sqlite3.connect('slack.db')
    c = conn.cursor()
    
    query = """SELECT M.channel_id, C.name
        FROM memberships M INNER JOIN channels C
        ON M.channel_id = C.channel_id
        WHERE user_id=?"""

    params = (uid, )
    cids = [row for row in c.execute(query, params)]

    conn.commit()
    conn.close()

    return cids

def send_message(cid, uid, contents):
    conn = sqlite3.connect('slack.db')
    c = conn.cursor()
    
    message_value = (cid, uid, int(time.time()), contents)
    c.execute("INSERT INTO messages (channel_id, user_id, tstamp, contents) VALUES (?, ?, ?, ?)", message_value)

    conn.commit()
    conn.close()

def get_messages(cid, num_recent=100):
    conn = sqlite3.connect('slack.db')
    c = conn.cursor()
    
    params = (cid, num_recent)
    messages = [msg for msg in c.execute("SELECT user_id, tstamp, contents FROM messages WHERE channel_id=? ORDER BY tstamp DESC LIMIT ?;", params)]

    conn.commit()
    conn.close()

    return messages

# Alex's pay: 6.25 + 20 + 3.75 + 20 + 7.5