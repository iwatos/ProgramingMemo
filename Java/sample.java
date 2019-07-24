import java.util.Date;

//プログラムのコンパイル　javac Sample.java
//プログラムの実行　java Sample
public class Main {

    public static void main(String[] args) {
        System.out.println("Hello World!");


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
        int[] array = { 0, 1, 2, 3, 4 };



        // 結合
        String join = "aaa" + "bbb";

        // 分割
        String[] record = "aaa,bbb,ccc".split( "," );

        // 長さ
        int length = "abcdef".length();

        // 切り出し
        "abcd".substring( 0, 2 );   // abc

        // 検索
        int result = "abcd".indexOf( "cd" ); // 見つかった場合はその位置、見つからなかった場合は-1が返る
    }
}
