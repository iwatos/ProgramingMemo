import java.util.*;

//プログラムのコンパイル　javac Sample.java
//プログラムの実行　java Sample
class Main {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}

//文法
class Grammer {

    //データ型
    void dataType() {
        // int(整数)型
        int num = 1;

        // char(文字)型
        char c = 'a';

        // float(単精度浮動小数点)型
        float fValue = 1.234f;

        // double(倍精度浮動小数点)型
        double dValue = 1.234;

        // boolean(論理)型
        boolean flag = true;

        // String型
        String s = "String";

        // Date型
        Date d = new Date();

        // 配列型
        int[] intArray = {0, 1, 2, 3, 4};
        double[] doubleArray = new double[10];
        String[] stringArray = {"Sunday", "Monday", "Tuesday"};

        //final変数　あとで代入できない
        final int FNUM = 0;
        //FNUM = 1;
    }

    void Syntax() {
        //for
        for (int i = 0; i <= 5; i++) {

        }

        //if
        if (true) {

        } else if (true) {

        } else {

        }

        //while
        while (true) {

        }

        //do-while
        do {

        } while (true);

        //三項演算子
        print(1 >= 100 ? true : false);

        //switch
        int a = 1;
        switch (a) {
            case 0:
                break;
            case 1:
                break;
            case 2:
                break;
            default:
                break;
        }

        //break
        sample:
        for (int i = 0; i <= 5; i++) {
            if (true) {
                break sample;//forループ中止
            }
        }

        //continue
        for (int i = 0; i <= 5; i++) {
            if (true) {
                break;//後の処理をスキップして次のループへ
            }
        }


    }

    void collectionFramework() {
        //リスト
        List<integer> list = new ArrayList();
        list.add(1);//追加
        list.get(0);//参照

        //セット
        Set<Integer> set = new HashSet<integer>();
        set.add(1);//追加
        set.add(1);//重複した値は入らない
        set.get(0);//参照

        //map
        Map<String, Integer> map = new HashMap<String, Integer>();
        map.put("一番", 0);//追加
        map.put("一番", 1);//追加 同じキーは上書き
        map.put("二番", 2);
        map.get("一番");//1

        //拡張for
        for (int num : list) {
            System.out.println(num);
        }
        list.foreach(System.out::println);
    }

    void method() {
        // 結合
        String join = "aaa" + "bbb";

        // 分割
        String[] record = "aaa,bbb,ccc".split(",");

        // 長さ
        int length = "abcdef".length();

        // 切り出し
        "abcd".substring(0, 2);   // abc

        // 検索
        int result = "abcd".indexOf("cd"); // 見つかった場合はその位置、見つからなかった場合は-1が返る
    }
}

//class
//final:サブクラス作成不可
//abstract:インスタンス生成不可
class Sample {
    //メンバ変数
    int a;
    private int b;
    static int c;//各インスタンス間で共有

    //コンストラクタ
    Sample() {
        a = 1;
        b = 2;
    }

    //クラスメソッド
    void hello() {
        System.out.println("HelloWorld!");
        this.a = 0;//自分自身を指す
    }
}

class ExtendedSample extends Sample {
    //オーバーライド
    void hello() {
        super.hello();//継承元のhello()を実行;
       System.out.println("HelloWorldExtended!");
    }

    //オーバーロード
    void hello(int num) {
       System.out.println("HelloWorldExtended!" + num);
    }
}

//インターフェース
interface Greeting {
    void greet();//インタフェース内ではヘッダー定義のみ
}

class ExInterface implements Greeting {
    public void greet() {
        System.out.println("こんにちは");
    }
}

//例外
class ExeptionSample implements Greeting {
    public void tryCatch() throws Exception {
        try {
            throw new Exception();
        } catch (Exception e) {
            System.err.println(e.getMessage());
        } finally {

        }
    }
}