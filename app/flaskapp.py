from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():

    import sqlite3
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE increment (d integer)''')
    except Exception as e:
        print('DB already created')

    html = "<h3>Hello!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())


@app.route("/plus")
def plus():
    import sqlite3
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(d) FROM increment');
    current_number = cursor.fetchone();
    if not(current_number):
        current_number = 0;
    else:
        current_number=current_number[0]
    print(current_number);
    new_number = current_number + 1;
    cursor.execute('INSERT INTO increment VALUES (?)',(new_number,))
    conn.commit()
    html = f"<h2>Previous number: {current_number}</h2><h3>New number: {new_number}</h3>"
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
