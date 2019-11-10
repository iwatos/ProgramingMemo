package servlet;

import model.LoginLogic;
import model.User;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;

@WebServlet(urlPatterns = "/Login")//URL指定
public class Login extends HttpServlet {//servletはHttpServletを継承

    private static final long serialversionUID = 1L;//おまじない（他環境で使う場合の識別ID）

    //postリクエスト処理
    protected void doPost(HttpServletRequest request,
                          HttpServletResponse response)
        throws ServletException, IOException {
        request.setCharacterEncoding("UTF-8");

        //フォームの値取得
        String name = request.getParameter("name");
        String pass = request.getParameter("pass");

        //個別処理
        User user = new User(name, pass);
        LoginLogic loginLogic = new LoginLogic();
        boolean isLogin = loginLogic.execute(user);
        if(isLogin){

            //jspでつかう値を格納
            HttpSession session = request.getSession();
            session.setAttribute("loginUser", user);
            
        }

        //指定jspへ送信
        RequestDispatcher dispatcher = request.getRequestDispatcher("/WEB-INF/jsp/loginResult.jsp");
        dispatcher.forward(request, response);

    }
}
