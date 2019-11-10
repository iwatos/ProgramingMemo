<%--
  Created by IntelliJ IDEA.
  User: owner
  Date: 2019-08-09
  Time: 19:05
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" pageEncoding="UTF-8" %>
<%@ page import="model.User" %>
<%
    User loginUser = (User)session.getAttribute("loginUser");
%>
<html>
<head>
    <title>どこつぶ</title>
</head>
<body>
<h1>どこつぶログアウト</h1>
<p>ログアウトしました</p>
<a href="/docoTsubu/">トップへ</a>
</body>
</html>
