<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<title> photo booth - password reset</title>
<head>
<style>
#back {
background-image:url(pink.jpg);
}
<meta content="text/html; charset=utf-8" http-equiv="content-type"
</style>
<body id="back">
<div style="text-align:center" >
<font color=black>
<h1> PHOTO BOOTH </h1>
</font>
<div class="box">
      <h2>Password reset</h2>
      <p>Please insert your credentials:</p>
      <form action="reset_password" method="post" name="password_reset">
          <input type="text" name="username" value="username"/>
          <input type="text" name="email_address" value="email address"/>

          <br/><br/>
          <button type="submit" > OK </button>
      </form>
          <form action="login" method="Post">
	    <button type="submit" > Cancel </button>

      </form>
      <br />
  </div>
</body>