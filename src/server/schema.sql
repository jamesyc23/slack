CREATE TABLE IF NOT EXISTS channels (channel_id INTEGER, name VARCHAR(255));
CREATE TABLE IF NOT EXISTS memberships (channel_id INTEGER, user_id INTEGER);
CREATE TABLE IF NOT EXISTS messages (channel_id INTEGER, user_id INTEGER, tstamp INTEGER, contents TEXT);
