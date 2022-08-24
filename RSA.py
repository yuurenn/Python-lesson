

from Crypto.PublicKey import RSA
 
# 秘密鍵の生成
private_key = RSA.generate(1024)
with open('private.pem', 'w') as f:
    f.write(private_key.export_key().decode('utf-8'))
 
# 秘密鍵に基づいて公開鍵を生成
public_key = private_key.publickey()
with open('public.pem', 'w') as f:
    f.write(public_key.export_key().decode('utf-8'))


# # pemロード
# with open('private.pem', 'br') as f:
#     private_pem = f.read()
#     private_key = RSA.import_key(private_pem)
 
# with open('public.pem', 'br') as f:
#     public_pem = f.read()
#     public_key = RSA.import_key(public_pem)


