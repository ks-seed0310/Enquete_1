# ファイル名: enquete_quiz1_v1_1.py
# AI作
import random
import time
import urllib.parse
import webbrowser

def create_url(t1, t2):
    """JavaScript版のcreateURL関数をPythonで再現"""
    mapping = {
        "idKey":    "aZbF1234",
        "tokKey":   "qRtY5678",
        "enKey":    "xLpM9012",
        "tsKey":    "uN1v3456",
        "nonceKey": "H3kL7890",
        "csKey":    "QwEr2468",
        "t1Key":    "T1kL1357",
        "t2Key":    "T2kM8642",
        "dummy1":   "DumA9999",
        "dummy2":   "DumB8888",
        "dummy3":   "XyZq7410",
        "dummy4":   "PqRs8520"
    }

    # ランダム値生成
    id_ = random.randint(0, 1_000_000)
    tok = random.randint(0, 1_000_000_000_000)
    ts = int(time.time() * 1000)  # JSのDate.now()に対応（ミリ秒）
    nonce = random.randint(0, 1_000_000)

    # en計算
    en_val = tok * 7 + id_ * 13 + ts * 3 + nonce * 19

    # チェックサム
    mod = 1_000_003
    cs = (tok % mod + en_val % mod + ts % mod + nonce % mod) % mod

    # URLパラメータ生成
    params = {
        mapping["idKey"]: id_,
        mapping["tokKey"]: tok,
        mapping["enKey"]: en_val,
        mapping["tsKey"]: ts,
        mapping["nonceKey"]: nonce,
        mapping["csKey"]: cs,
        mapping["t1Key"]: urllib.parse.quote(t1),
        mapping["t2Key"]: urllib.parse.quote(t2),
        mapping["dummy1"]: random.randint(100_000_000, 199_999_999),
        mapping["dummy2"]: random.randint(200_000_000, 1_199_999_999),
        mapping["dummy3"]: random.randint(3_000_000_000, 13_999_999_999),
        mapping["dummy4"]: random.randint(400_000, 1_400_000)
    }

    base_url = "https://script.google.com/a/macros/s.kansai.soka.ed.jp/s/AKfycbyQqyXeUulnOfWELACWtVGxDk9Bg4W1OGHfFXb_ilyUKohs-kenZvw0mdGnh4HMVDZ35Q/exec"
    query = "&".join([f"{k}={v}" for k, v in params.items()])
    return f"{base_url}?{query}"


def main():
    print("=== Quiz1.v1.1 協力のお願い送信フォーム (Python版) ===\n")
    t1 = input("回答1つ目を入力: ")
    t2 = input("回答2つ目を入力: ")

    # 特定入力チェック
    if t1 == "/*pages" and t2 == "sheets*/":
        url = "https://docs.google.com/spreadsheets/d/1BMIcg1YAQGO8ZmbFtn6xaZxK-l3oT3ie4ChvL0Z5RXY/edit"
    else:
        url = create_url(t1, t2)

    print("\n5秒後にURLを開きます。")
    for i in range(4, 0, -1):
        print(f"{i}秒後に移動します...")
        time.sleep(1)

    print("\nURLを開きます:", url)
    webbrowser.open(url)


if __name__ == "__main__":
    main()
