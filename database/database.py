import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yug@0727",
        database="campus_firstaid"
    )


def check_login(username, password, role):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM users
    WHERE username=%s AND password=%s AND role=%s
    """, (username, password, role))

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user


def add_request(username, location, emergency_type, description, contact):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO requests
    (username, location, emergency_type, description, contact)
    VALUES (%s, %s, %s, %s, %s)
    """, (
        username,
        location,
        emergency_type,
        description,
        contact
    ))

    conn.commit()

    cursor.close()
    conn.close()


def get_requests(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, location, emergency_type, status
    FROM requests
    WHERE username=%s
    """, (username,))

    requests = cursor.fetchall()

    cursor.close()
    conn.close()

    return requests


def get_all_requests():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id,
           username,
           location,
           emergency_type,
           description,
           contact,
           status
    FROM requests
    ORDER BY id DESC
    """)

    requests = cursor.fetchall()

    cursor.close()
    conn.close()

    return requests


def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, username, password, role
    FROM users
    ORDER BY id
    """)

    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return users


def add_user(username, password, role):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users(username, password, role)
    VALUES(%s, %s, %s)
    """, (username, password, role))

    conn.commit()

    cursor.close()
    conn.close()


def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM users
    WHERE id=%s
    """, (user_id,))

    conn.commit()

    cursor.close()
    conn.close()

def update_user(user_id, username, password, role):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE users
    SET username=%s,
        password=%s,
        role=%s
    WHERE id=%s
    """, (username, password, role, user_id))

    conn.commit()

    cursor.close()
    conn.close()

def update_request_status(request_id, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE requests
    SET status=%s
    WHERE id=%s
    """, (status, request_id))

    conn.commit()

    cursor.close()
    conn.close()

def total_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total


def total_requests():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM requests")
    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total


def count_status(status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM requests WHERE status=%s",
        (status,)
    )

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total

def get_all_requests_for_report():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id,
           username,
           location,
           emergency_type,
           description,
           contact,
           status
    FROM requests
    ORDER BY id
    """)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data