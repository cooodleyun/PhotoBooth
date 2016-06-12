<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<title> photo booth - password change</title>
<head>
<body bgcolor="mistyrose">
<div style="text-align:center" >
<font color=black>
<h1> PHOTO BOOTH </h1>
</font>
<div class="box">
    <h2>Password change</h2>
    <p>Please insert your new password:</p>
    <form action="/change_password" method="post">
        <input type="password" name="password" />
        <input type="hidden" name="reset_code" value="{{reset_code}}" />

        <br/><br/>
        <button type="submit" > OK </button>
       <form action="login" method="post">
	<button type="submit" > Cancel </button>
 </form>
    </form>
    <br />
</div>
</body>
<style>
div {
    color: #777;
    margin: auto;
    width: 20em;
    text-align: center;
}
input {
    background: #f8f8f8;
    border: 1px solid #777;
    margin: auto;
}
input:hover { background: #fefefe}
</style>
