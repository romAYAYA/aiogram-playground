import sqlite3 as sq

db = sq.connect("tg.db")
cur = db.cursor()


async def db_start():
    cur.execute(
        "CREATE TABLE IF NOT EXISTS tickets"
        "(t_id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "direction TEXT, "
        "fly_date TEXT, "
        "price TEXT)"
    )
    db.commit()


async def cmd_start_db(user_id):
    user = cur.execute('SELECT * FROM accounts WHERE tg_id == {key}'.format(key=user_id)).fetchone()
    if not user:
        cur.execute('INSERT INTO accounts (tg_id) VALUES ({key})'.format(key=user_id))
        db.commit()













