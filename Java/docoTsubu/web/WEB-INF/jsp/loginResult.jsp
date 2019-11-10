<%--
  Created by IntelliJ IDEA.
  User: owner
  Date: 2019-08-08
  Time: 21:08
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" pageEncoding="UTF-8" %>
<%@ page import="model.User" %>
<%
    User loginUser = (User) session.getAttribute("loginUser");
%>

<html>
<head>
    <title>どこつぶ</title>
</head>
<body>
    <h1>どこつぶログイン</h1>
    <% if(loginUser != null) { %>
    <p>ログインに成功しました</p>
    <p>ようこそ<%= loginUser.getName()%>さん</p>
    <a href="/docoTsubu/Main">つぶやき投稿、閲覧へ</a>
    <% } else { %>
    <p>ログインに失敗しました</p>
    <a href="/docoTsubu">TOPへ</a>
    <% } %>
</body>
</html>
