"""
ぐるなびのレストラン検索APIを使って
「Freeword検索」← 入力として受け取る
     ↓
次の形式で必要な情報を出力する
「店舗名」、URL、路線名、駅名、 徒歩○分
"""
import os
from search_restaurant import search_restaurant


def main():
    access_key = os.environ['KEY_ID']

    free_word = input('検索ワードを入力してください(例:店名やジャンルなど) > ')
    result_number = input('何件表示しますか？(1~100まで) > ')
    search_restaurant(access_key, free_word, result_number)



if __name__ == '__main__':
    main()
