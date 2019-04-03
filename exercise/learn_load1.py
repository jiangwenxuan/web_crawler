import requests
session = requests.session()

post_url = 'http://www.santostang.com/wp-login.php'
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
headers = {
    "Host": "www.santostang.com",
    "Origin": "http://www.santostang.com",
    "Referer": "http://www.santostang.com/wp-login.php",
    'User-Agent': agent
}
postdata = {
    'pwd': 'a12345',
    'log': 'test',
    'rememberme': 'forever',
    'redirect_to': 'http://www.santostang.com/wp-admin',
    'testcookie': 1,
}
login_page = session.post(post_url, data = postdata, headers = headers)
print(login_page.status_code)
session.cookies.save()