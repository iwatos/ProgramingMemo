<%-- Created by IntelliJ IDEA. --%>
<%@ page contentType="text/html;charset=UTF-8" language="java" pageEncoding="UTF-8" %>

<!DOCTYPE html>
<html>
  <head>
    <title>タイトル</title>
  </head>
  <body>
    <h1>タイトル</h1>

    <%-- form Login.javaへポスト--%>
    <form action="Login" method="post"/>
    ユーザ名； <input type="text" name="name"><br>
    ユーザ名； <input type="password" name="pass"><br>
    <input type="submit" value="ログイン">

  </body>
</html>