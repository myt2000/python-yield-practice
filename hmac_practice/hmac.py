from hmac import new

def hmac_key():
    key1 = new(0x01011, msg="检测代码")
    print(key1)

if __name__ == "__main__":
    hmac_key()