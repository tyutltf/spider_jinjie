
import requests

headers={
    'Cookie':'__cdnuid=cbe5fb6dad23643a24bc7bcd68880d41; PHPSESSID=vvhvpub26dg4oghpg0k4hkapm1; jieqiUserInfo=jieqiUserId%3D27793%2CjieqiUserUname%3D%D3%EA%D0%F9%C1%B5i%2CjieqiUserName%3D%D3%EA%D0%F9%C1%B5i%2CjieqiUserGroup%3D3%2CjieqiUserGroupName%3D%C6%D5%CD%A8%BB%E1%D4%B1%2CjieqiUserVip%3D0%2CjieqiUserHonorId%3D%2CjieqiUserHonor%3D%D0%C2%CA%D6%C9%CF%C2%B7%2CjieqiUserUname_un%3D%26%23x96E8%3B%26%23x8F69%3B%26%23x604B%3Bi%2CjieqiUserName_un%3D%26%23x96E8%3B%26%23x8F69%3B%26%23x604B%3Bi%2CjieqiUserHonor_un%3D%26%23x65B0%3B%26%23x624B%3B%26%23x4E0A%3B%26%23x8DEF%3B%2CjieqiUserGroupName_un%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserLogin%3D1543903297; jieqiVisitInfo=jieqiUserLogin%3D1543903297%2CjieqiUserId%3D27793',
    'Host':'www.6mao.com',
    'User-Agent':"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5"
}

r=requests.get('http://www.6mao.com',headers=headers)
r.encoding='gbk'
print(r.text)