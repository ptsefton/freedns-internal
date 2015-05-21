# freedns-internal

This is a python script to set your IP address at freedns.agfraid.org to an *internal* IP address. 

Why would you want to do such a thing? 

I was working with a Rasberry Pi computer with no monitor or keyboard, and I wanted to be able to locate it when it connected to my work or home network so I could SSH into it, or hit its web service, from the *same* network. This script does not give you the external IP address of your network, but there are lots of options for doing that at the freedns site.

## How to use

*  Check out this repository
*  Sign up for an account at freedns.afraid.org
*  Get your secret key:
   *  Visit this page [https://freedns.afraid.org/dynamic/]:https://freedns.afraid.org/dynamic/
   *  Click ```Direct URL```
      Look in your browser address bar, it will be like ```https://freedns.afraid.org/dynamic/update.php?your-key-will-be-here```
   *  Copy the secret key, which is the part of the URL after the ```?```
*  Edit[.freedns_secret](.freedns_secret) to add your secret key
*  Set up a cron job to run [set-freedns-internal-ip.py](./set-freedns-internal-ip.py) at some suitable interval - I do it once a minute
