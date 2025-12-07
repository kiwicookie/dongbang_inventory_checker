

import requests

def main():
    url = "https://script.google.com/macros/library/d/1fqi15CDx13K4hhiKujgl8qvOirVo5dHFaZ6k2zI6B8FZCcNSOqc4Gvrk/3"
    url = "https://script.google.com/macros/s/AKfycbzEmQCq9q3thtV3pYI4PaGXig_UNfaI2Sj9XBJkHkRbGAYGERH5XzoHYdy7c-uSPk5WgA/exec"
    url = "https://script.google.com/macros/s/AKfycby5oH9VQRxlse6ey-rJ4DfpkaggXsCBWZNhpuBAVHlIDEEJf1bet-uzx5Br8u1lyDs4gQ/exec"
    url = "https://script.google.com/macros/s/AKfycbzSrTKeJBjDARK5JRo3-SCBtacVqLDcxZufiOfiFL_c70mZrD6I00hCxtt6g1SatwngcA/exec"
    url = "https://script.google.com/macros/s/AKfycbxQFTeOYQsrrVorgYrPdEzmn4Jdeuoa_gRnHlpwmVMgXLi_mZHwx0VAzXf8UjMKUQsyHg/exec"
    url = "https://script.google.com/macros/s/AKfycbzG16FAztc1_uz10UBjaZSSwyKsZ35XAWjbnTtoRXYZCkCIPN8cOpwGwXv0RWXJtG7TQQ/exec"
    url = "https://script.google.com/macros/s/AKfycbxeLzA4GWBys3boMif4LzIw6g-AtF_0BaOHODUZOd-hOV6lnkOriULNXIaOZc_ZXstsMQ/exec"
    url = "https://script.google.com/macros/s/AKfycbwkBcJIZQNuapp-mGsBQfuhUfZGSXSJElmbooLqQpdTqeMxKttSDK8HDwGZVz_DNh0Efg/exec"
    url = "https://script.google.com/macros/s/AKfycbyW-GY71LVlpcJl4ndqaiFyfFnI1Amq4J6c7A0dM9Adliit3TtV344kyIxaqBZlDVmW/exec"

    data_get = {
        "itemName": "코스모스",
        "itemCode": "1810",
        }
    data = {
  "intent": {
    "id": "35z8xtipvo2wigdxz86fizb9",
    "name": "블록 이름"
  },
  "userRequest": {
    "timezone": "Asia/Seoul",
    "params": {
      "ignoreMe": "true"
    },
    "block": {
      "id": "35z8xtipvo2wigdxz86fizb9",
      "name": "블록 이름"
    },
    "utterance": "발화 내용",
    "lang": "",
    "user": {
      "id": "810402",
      "type": "accountId",
      "properties": {}
    }
  },
  "bot": {
    "id": "68f7a5842c0d3f5ee71cb804",
    "name": "봇 이름"
  },
  "action": {
    "name": "1gey42gtam",
    "clientExtra": "",
    "params": {
      "itemName": "동방 18색사",
      "itemCode": "314"
    },
    "id": "h2egquumizjmr21r4yvquczr",
    "detailParams": {
      "itemName": {
        "origin": "동방 18색사",
        "value": "동방 18색사",
        "groupName": ""
      },
      "itemCode": {
        "origin": "314",
        "value": "314",
        "groupName": ""
      }
    }
  }
}
    # raw_url = f"https://script.google.com/macros/s/AKfycbx9URmeVydFDsaYy5vhnzJMg7MT2juyTB_6bvWi3guwduZZQjofVZPL8rSOfucNdJStsA/exec"
    # url = raw_url + f"?itemName={data_get['itemName']}&itemCode={data_get['itemCode']}&mode=sheets"
    # print(url)
    # response = requests.get(url)


    raw_url = f"https://script.google.com/macros/s/AKfycbzrj4iz6nLoeMnlgK8O3vKLsGNncfhL2XK8C9jvx7Y3Hxe2ieXNKK0A2OeDg2f88a8DUg/exec"
    url = raw_url + f"?itemName=a&itemCode=당근&mode=specific"
    response = requests.get(url)
    # ✅ 결과 출력
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    print(type(response.text))
    print("hi")

    # url = f"https://script.google.com/macros/s/AKfycbxK8U4Yy3j2PNbV5zmq-CDHlsvu8YyFWCt_bOPzWHdmgTVyfgo8Ism-m_r-qfG3jEErxQ/exec"
    # url = f"https://script.google.com/macros/s/AKfycbx8fYflWZKXfqFKZ6J8uegnYauK0ZYfAeobk6CcSxHdd6Iw9HtyvPIMjJFSKZN0dOcUCw/exec"
    # response = requests.post(url, json=data)
    # # ✅ 결과 출력
    # print("Status Code:", response.status_code)
    # print("Response Text:", response.text)
    # print("hi")

if __name__ =="__main__":
    main()