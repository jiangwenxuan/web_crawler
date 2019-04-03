import requests
import http.cookiejar as cookielib

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename = 'cookies')

try:
    session.cookies.load(ignore_discard = True)
except:
    print("cookie can't load")

def isLogin():
    url = "http://www.santostang.com/wp-admin/profile.php"
    login_code = session.get(url, headers = headers, allow_redirects = False).status_code
    if login_code == 200:
        return True
    else:
        return False

def login(secret, account):
    post_url = 'http://www.santostang.com/wp-login.php'
    postdata = {
        'pwd': secret,
        'log': account,
        'rememberme': 'true',
        'redirect_to': 'http://www.santostang.com/wp-admin',
        'testcookie': 1,
    }
    try:
        login_page = session.post(post_url, data = postdata, headers = headers)
        login_code = login_page.text
        print(login_page.status_code)
    except:
        pass
    session.cookies.save()

if __name__ == '__main__':
    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    headers = {
        'Host': 'www.santostang.com',
        'Origin': 'http://www.santostang.com',
        'Referer': 'http://www.santostang.com/wp-login.php',
        'User-Agent': agent
    }
    if isLogin():
        print('you have login')
    else:
        login('a12345', 'test')