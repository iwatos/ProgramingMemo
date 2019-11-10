<%--
  Created by IntelliJ IDEA.
  User: owner
  Date: 2019-08-09
  Time: 19:05
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" pageEncoding="UTF-8" %>
<%@ page import="model.User,model.Mutter,java.util.List" %>
<%
    User loginUser = (User) session.getAttribute("loginUser");
    List<Mutter> mutterList = (List<Mutter>) application.getAttribute("mutterList");
    String errorMsg = (String) request.getAttribute("errorMsg");
%>
<html>
<head>
    <title>どこつぶ</title>
</head>
<body>
<h1>どこつぶメイン</h1>
<p>
    <%= loginUser.getName() %>さん、ログイン中
    <a href="/docoTsubu/Logout/">ログアウト</a>
</p>
<p><a href="/docoTsubu/Main">更新</a></p>
<form action="/docoTsubu/Main" method="post">
    <input type="text" name="text">
    <input type="submit" value="つぶやく">
</form>
®
<% if (errorMsg != null) { %>
<p><%= errorMsg %></p>
<% } %>

<% for (Mutter mutter : mutterList) { %>
<p><%= mutter.getUserName() %>:<%= mutter.getText() %>
</p>
<% } %>



</body>
</html>
