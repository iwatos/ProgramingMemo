# コメント
"""
複数行の
コメント
"""


def use_variable():
    a = 1  # 整数
    b = 1.1  # 少数
    c = "String"  # 文字列
    # 複数行文字列
    d = """　
    String\tString\n
    String
    """
    c = True  # 　真偽値
    print(a, b, c, d, c)

    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a % b)
    print(a ** b)
    print(a // b)

    print(True and False)
    print(True or False)
    print(not True)

    a += b
    print(a)

    c = "hello"
    print(c + c)
    print(c * 3)
    print(f"{c} world!")

    # 配列
    lists = [40, 50, "aaa"]
    print(lists[0])  # 参照
    print(len(lists))  # 長さ
    socres.appened(100)  # 追加
    lists += ["bbb", "ccc"]  # 追加
    lists.insert(2, 60)  # 挿入
    del lists[0]  # 削除
    lists.pop(0)  # 削除
    lists.remove("ccc")  # 最初の一致する値を削除
    lists.extend([0, 1, 2])  # 後ろに結合
    print("aaa" in lists)  # 要素の検索(True/False)
    lists.index("bbb")  # 要素位置検索
    lists.count("aaa")  # 指定要素が入っている数
    print(lists.sort())  # ソート
    print(lists.reverse())  # 逆順
    for num in lists:  # 要素の取得
        print(num)

    # タプル
    tuples = (50, "apple", 32.5)  # タプルでは値を書き換えられない
    tuples0 = (1, )  # 値が一つだけのタプル
    tuples1 = tuples + (0, 1, 2)  # 要素の追加
    tuples2 = tuples[0:2:1]  # 要素の削除
    print(tuples1 == tuples2)  # 比較
    print(1 in tuples)  # 要素の検索
    for num in tuple_sample:  # 要素の取得
        print(num)

    # セット
    sets = {1, 3, 5, 8, 2}  # 順番を持たず重複した要素はない
    sets.add(4)  # 追加
    sets.remove(5)  # 削除
    sets.clear()  # すべての要素を削除
    sets1 = {3, 5, 4, 9}  # 重複を許さない
    sets2 = {1, 3, 7, 9}  # 重複を許さない
    print(sets1 | sets1)  # 和集合
    print(sets1 & sets1)  # 積集合
    print(sets1 - sets1)  # 差集合
    for item in sets:
        print(item)

    # 辞書型
    dicts = {"apple": 1, "orange": 2, "banana": 3}
    print(dicts["apple"])  # 参照
    dicts["orange"] = 5  # 置き換え
    print("orange" in dicts.keys())  # 検索　キー
    print("3" in dicts.values())  # 検索　値
    dicts["mango"] = 10  # 追加 (すでに存在する場合は書き換え)
    dicts.setdefault("peach", 4)  # 追加 (すでに存在する場合は書き換えずに値を返す)
    dicts.pop("orange")  # 削除
    dicts.clear()  # 全要素を削除
    print(sorted(dicts.items))  # ソート結果をリスト型で返す
    for key in dicts.keys():
        print(key)
    for value in dicts.values():
        print(item)
    for key, value in dicts.items:
        print(key, value)


def use_if():
    """
    演算子	結果
    x < y	xがyより小さければTrue
    x <= y	xがyより小さいか等しければTrue
    x > y	xがyより大きければTrue
    x >= y	xがyより大きいか等しければTrue
    x == y	xとyの値が等しければTrue
    x != y	xとyの値が等しくなければTrue
    x is y	xとyが同じオブジェクトであればTrue
    x is not y	xとyが同じオブジェクトでなければTrue
    x in y	xがyに含まれていればTrue
    x not in y	xがyに含まれていなければTrue
    """
    score = 70
    if score > 80:
        print("Great!")
    elif score > 60:
        print("Good!")
    else:
        print("So So!")

    print("Great!" if score > 80 else "so so! ..")


def use_while():
    for i in range(0, 10):
        print(i)

    i = 0
    name = "endo"
    while i < 10:
        print(i)
        i += 1

# 関数ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー


def say_endo(name="endo", age=23):  # デフォルト値を設定
    print("Hi! {0} age({1})".format(name, age))


"""
say_endo()
say_endo("steave")
say_endo(age=18, name="Takahashi")
"""


def use_pass():
    pass


"""
print(use_pass)  # "None"
"""

msg = "Hello Global!"  # グローバル変数


def say_hi():
    # globaを付ける事で関数内で書き換え可能となる。
    global msg
    masg = "change global 2 local "
    print(msg)  # グローバル変数を参照できる。


def div(a, b):  # 例外処理
    try:
        # 0除算
        print(a/b)
    # 例外発生時の処理
    except ZeroDivisionError:
        print("not by zaro")
    # 例外が発生しなかった時の処理
    else:
        print("no exception!")
    # 例外が発生しようが、しないようが最期に実行に実行して欲しい処理を記述する
    finally:
        print("-- end -- 処理が終わりました")


def myfunc(x): return x*2


"""
print(myfunc(2))
print(myfunc(4))
"""

# クラスーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー


class User:
    # selfはこのクラスから作られるインスタンスを指します。
    def __init__(self, name):
        # インスタンス変数
        self.name = name

    @classmethod  # (デコレーター)
    def show_info(cls):
        print("{0}:instances".format(cls.count))
        self.__name = name  # クラス外からアクセスしない様に明示的に宣言する。

    # インスタンスメソッド(インデントは上に合わせる!)
    def say_hi(self):
        print("hi! {0}".format(self.__name))


class AdminUser(User):  # 継承
    def __init__(self, name, age):
        """
        親クラス(Userの)__init__ メソッド
        (コンストラクタ)で
        name を初期化する処理がすでに存在するので、
        それをサブクラス(AdminUser)の中でも再利用を
        する為にsuper()を使う。
        """
        # これを呼び出す事で`self.name`が使える。
        # つまりここは、親クラスのself.nameと同じ場所を参照している。
        super().__init__(name)

        self.age = age

        # 親クラスのプロパティを書き換える前。
        print("子クラスでsuper()を使った親クラスのプロパティ呼び出すされるnameは{0}".format(self.name))

        # 親クラスのプロパティを書き換える。
        self.name = "Endo"
        print("子クラスで親クラスのプロパティを書き換えた後に呼び出されるname>は{}".format(self.name))

    # インスタンスメソッド
    def say_hello(self):
        print("Hello!! {0} age:{1}".format(self.name, self.age))
