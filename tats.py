#!/usr/bin/env python
"""
Written By Danny Lujan, Feb. 2020
Inspired by an idea from Andre Cherry and the music of Tatsuro Yamashita.

TATS builds common apache rewrite rules with an easy to use menu.
TODO: Make application functional via arguments. 

"""

from string import Template

# Variables
rewrite_engine = "RewriteEngine On"
https = ["RewriteCond %{SERVER_PORT} 80", "https", "http"]
https_template = Template('RewriteRule ^ $https://$www%1%{REQUEST_URI} [L,NE,R=301]')
www = ["RewriteCond %{HTTP_HOST} ^(?:www\.)?(.+)$ [NC]", "www.", "RewriteCond %{HTTP_HOST} ^www\.?(.+)$ [NC]", ""]
olddomain_template = Template("RewriteCond %{HTTP_HOST} ^(.+) $olddomain")  
newdomain_template = Template("RewriteRule ^(.*)$$ $https://$www$newdomain/$$1 [R=301,L]")

# Functions

def menu():
   ans=True
   while ans:
       print ("""
       1.Force HTTPS (generic)
       2.Force www (generic)
       3.Redirect old domain to new
       4.Exit/Quit
       """)
       ans=raw_input("What would you like to do? ")
       if ans=="1":
         force_https()
       elif ans=="2":
         ans_https=raw_input("\n Also force https? (y or n): ")
         force_www(ans_https)
       elif ans=="3":
         print("\n Redirect")
         ans_www=raw_input("\n Also force www? (y or n): ")
         ans_https=raw_input("\n Also force https? (y or n): ")
         redirect(ans_www, ans_https)
       elif ans=="4":
         print("\n Goodbye")
         ans=False
       elif ans !="":
         print("\n Not Valid Choice Try again")


def force_https():
   print ("\n")
   print rewrite_engine
   print https[0]   
   print (https_template.substitute(https = https[1], www = ""))

def force_www(httpsyn):
   if httpsyn == "y":
      https_value=int(1)
   elif httpsyn != "":
      https_value=int(2)

   print ("\n")
   print rewrite_engine
   print www[0]
   print (https_template.substitute(https = https[https_value], www = www[1]))


def redirect(httpsyn, wwwyn):
   olddomain1 = raw_input("Enter the old domain (no www): ")
   newdomain1 = raw_input("Enter the new domain (no www): ")

   if httpsyn == "y":
      https_value=int(1)
   elif httpsyn != "":
      https_value=int(2)

   if wwwyn == "y":
      www_value=int(1)
   elif wwwyn != "":
      www_value=int(4)

   print ("\n")
   print rewrite_engine
   print (olddomain_template.substitute(olddomain = olddomain1))
   print (newdomain_template.substitute(https = https[https_value], www = www[www_value], newdomain = newdomain1))

menu()

