import requests
from r_token import token
import json
import pytest

APIKey = "798377D353A00F08DEEEDFDD15371D26507BDAE527B87A0B7E2B52137B52369DB6CC9437D32E5071"
APISecret = "642CC7F5ED204D0253795EEE5937DD41A07D50DC1B1E9A0FCE7E6175A79D649DF4772509EB63430A"
token_url = "http://httwmsopenwebapi.haituotong.com/"
tk = token(APIKey, APISecret, token_url)
print(tk)
url = "http://httwmsopenwebapi.haituotong.com/api/OpenWebApi/DF_CreateOutOrder?token=" + tk
print(url)

OutOrderCode = ""
UserCode = "TEST01"
CountryCode = "US"
WarehouseCode = "USDB"
DeliveryCompany = "USPS"
UserCustomeNumber = ""
Consignee = "JamesKinnard"
ConsigneeTelephone = "+1 7704557737"
ConsigneeAddress = "633 Rancho De Oro"
ZipCode = "30533"
ConsigneeAddress2 = ""
ConsigneeCountryName = ""
State = "Georgia"
City = "Dahlonega"
Remark = ""
SKU = 'GPE004-3P-C3'
count = '1'

data = {
    "OutOrderCode": OutOrderCode,
    "UserCode": UserCode,
    "CountryCode": CountryCode,
    "WarehouseCode": WarehouseCode,
    "DeliveryCompany": DeliveryCompany,
    "UserCustomeNumber": UserCustomeNumber,
    "Consignee": Consignee,
    "ConsigneeTelephone": ConsigneeTelephone,
    "ConsigneeAddress": ConsigneeAddress,
    "ZipCode": ZipCode,
    "ConsigneeAddress2": ConsigneeAddress2,
    "ConsigneeCountryName": ConsigneeCountryName,
    "State": State,
    "City": City,
    "Remark": Remark,
    "DetailList": [
        {
            "SKU": SKU,
            "SendAmount": count
        }]
}

r = requests.post(url, json=data)
print(r.json())

