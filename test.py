import pyupbit

access = "kTmCUTN0ClwOlG7tbSRHAicU9V63TFzDYenzqrBx"          # 본인 값으로 변경
secret = "v83os6aZzmHNprO3emqnhKtubxZpnZsTiU266ulP"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-ETH"))    # KRW-ETH 조회
print(upbit.get_balance("KRW-MANA"))    # KRW-MANA 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회