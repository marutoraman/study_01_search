
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

import csv
# 検索ソース
with open('source.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"])
### yoneya 書き込み値は固定値ではなく、source関数内で追記されたrowの値を書き込むようにします
### このままですと、ＣＳＶ書き込み、ＣＳＶ読み込みののちにsearch関数が呼び出されるため
### search関数内にＣＳＶ書き込み、読み込みの処理を含めるようにお願いします。
### CSV読み込みで読み込んだ値は、rowに格納するようにします

### 検索ツール

with open('source.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

# print(source)

def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    print(word in row)

    if word in row:
        print('います')
    else:
        row.append(word)
        print('いません。追加します。')

    print(row)

    print("{}が見つかりした".format(word))

if __name__ == "__main__":
    search()

# 現時点で試行錯誤中です↓
# with open('source.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(word)
    





