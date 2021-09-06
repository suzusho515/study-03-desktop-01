import pandas as pd
import eel

### デスクトップアプリ作成課題
def kimetsu_search(csv_read, csv_write, word):
    # 検索対象取得
    df=pd.read_csv(r"{}".format(csv_read))
    source=list(df["name"])

    #検索Wordが入力されているか確認
    if word == "":
        raise ValueError("検索Wordが不正です")

    # 検索
    if word in source:
        print("『{}』はあります".format(word))
        eel.view_log_js("『{}』が見つかりました".format(word))
    else:
        print("『{}』はありません".format(word))
        eel.view_log_js("『{}』はいません".format(word))
        eel.view_log_js("『{}』を追加します".format(word))
        # 追加
        #add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        #if add_flg=="1":
        source.append(word)
    
    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    #読込用更新
    df.to_csv("./{}".format(csv_read),encoding="utf_8-sig")
    #保存用更新
    df.to_csv(csv_write,encoding="utf_8-sig")
    print(source)
