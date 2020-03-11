#!/usr/local/bin/python3


import cgi

form = cgi.FieldStorage()

name = form.getvalue('name')


colors = [line.rstrip('\n') for line in open('color.txt')]


if name in colors:
  print("""
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <title>Hello!</title>
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      
      <!-- import the webpage's stylesheet -->
      <link rel="stylesheet" href="/style.css">
      
      <!-- import the webpage's javascript file -->
      <script src="/script.js" defer></script>
    </head>  
    <body>
      
      <h1>Hello, """+name+"""!</h1>
      
      </body>
  </html>
  """)
else:
  print("""
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <title>Hello!</title>
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      
      <!-- import the webpage's stylesheet -->
      <link rel="stylesheet" href="/style.css">
      
      <!-- import the webpage's javascript file -->
      <script src="/script.js" defer></script>
    </head>  
    <body>
      
      <h1>Hello, """+name+"""  is no color!</h1>
      
      </body>
  </html>
  """)

print(colors)