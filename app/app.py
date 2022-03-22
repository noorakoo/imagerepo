from tkinter.ttk import Style
from typing import List, Dict
from flask import Flask, request
import mysql.connector
import json

app = Flask(__name__)
DB_conf = { 'user': 'root', 'password': 'root', 'host': 'db',
            'port': '3306', 'database': 'imagerepo' }

def test_table():
   connection = mysql.connector.connect(**DB_conf)
   cursor = connection.cursor()
   cursor.execute('SELECT * FROM images')
   results = [c for c in cursor]
   cursor.close()
   connection.close()
   return results

def add_item(link, title, descript):
   connection = mysql.connector.connect(**DB_conf)
   cursor = connection.cursor()
   request = f"INSERT INTO images (link, title, descript) VALUES ('{link}', '{title}', '{descript}');"
   cursor.execute(request)
   connection.commit()
   cursor.close()
   connection.close()
   return request

@app.route('/add')
def add():
   link = request.args.get("link", "", str)
   title = request.args.get("title", "", str)
   descript = request.args.get("descript", "", str)
   S =  "<!DOCTYPE html>\n"
   S += "<html>\n"
   S += "   <head>\n"
   S += "      <title>Added an image</title>\n"
   S += style()
   S += "   </head>\n"
   S += "   <body>\n"
   S += "      <h1>Added an image</h1>\n"
   if link != "" and title != "" and descript != "":
      S += add_item(link, title, descript)
   S += "      <button><a href='/'>Back</a></button>\n"
   S += "   </body>\n"
   S += "</html>\n"
   return S

def delete_items(title):
   connection = mysql.connector.connect(**DB_conf)
   cursor = connection.cursor()
   request = f"DELETE FROM images WHERE title = '{title}';"
   cursor.execute(request)
   connection.commit()
   cursor.close()
   connection.close()
   return request

@app.route('/delete')
def delete():
   title = request.args.get("title", "", str)
   S =  "<!DOCTYPE html>\n"
   S += "<html>\n"
   S += "   <head>\n"
   S += "      <title>Deleted an image</title>\n"
   S += style()
   S += "   </head>\n"
   S += "   <body>\n"
   S += "      <h1>Deleted an image</h1>\n"
   if title != "":
      S += delete_items(title)
   S += "      <button><a href='/'>Back</a></button>\n"
   S += "   </body>\n"
   S += "</html>\n"
   return S

@app.route('/')
def index():
   S = "<!DOCTYPE html>\n"
   S += "<html>\n"
   S += "   <head>\n"
   S += "      <meta charset='utf-8'>\n"
   S += "      <title>Images list</title>\n"
   S += "      <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n"
   S += style()
   S += "   </head>\n"
   S += "   <body>\n"
   S += "      <h1>Images list</h1>\n"
   S += "      <table>"
   S += "      <form action='/delete'>\n"
   S += f"     <tr>\n"
   S += f"        <th>Title</th>\n"
   S += f"        <th>Link</th>\n"
   S += f"        <th>Description</th>\n"
   S += f"     </tr>\n"
   for (title, link, descript) in test_table():
      S += f"     <tr>\n"
      S += f"        <td>{title}</td>\n"
      S += f"        <td><a target='_blank' href='{link}'>{title} link</a></td>\n"
      S += f"        <td>{descript}</td>\n"
      S += f"        <td><input type='radio' value={title} name='title'</td>\n"
      S += f"     </tr>\n"
   S += "        <tr><td><button type='submit'>Delete</button></td></tr>\n"
   S += "      </form>\n"
   S += "      </table>"
   S += "      <br>"
   S += "      <form action='/add'>\n"
   S += "        <input size='20' type='text' name='title' placeholder='title...'/>\n"
   S += "        <input size='20' type='text' name='link' placeholder='link...'/>\n"
   S += "        <input size='20' type='text' name='descript' placeholder='description...'/>\n"
   S += "        <button type='submit'>Add</button>\n"
   S += "      </form>\n"
   S += "   </body>\n"
   S += "</html>\n"
   return S

def style():
    S  = "<style>\n"
    S += "   body {width: 80%; align-content: center; margin: 0 auto; padding: 15px; background-color: #F4EEE9; color: #3A4E4F; font-family: Arial, Helvetica, sans-serif;}\n"
    S += "   th {background-color: #8CACA2;}"
    S += "   td {padding-right: 20px;}"
    S += "   a {color: #3A4E4F;}"
    S += "   a:hover {color: #8C9C8C; text-decoration: none;}"
    S += "</style>\n"
    return S

if __name__ == '__main__':
    app.run(host='0.0.0.0')
