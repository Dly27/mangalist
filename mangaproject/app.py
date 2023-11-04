from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def display_manga_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('manga.db')
    cursor = conn.cursor()

    # Retrieve data from the "manga" table
    cursor.execute('SELECT * FROM manga')
    data = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Render an HTML template and pass the data to it
    return render_template('mangalibrary.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
