<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta content="text/html; charset=utf-8" http-equiv="content-type">
<div class="box">
      <h2>Password reset</h2>
      <p>Please insert your credentials:</p>
      <form action="reset_password" method="post" name="password_reset">
          <input type="text" name="username" value="username"/>
          <input type="text" name="email_address" value="email address"/>

          <br/><br/>
          <button type="submit" > OK </button>
          <form action="login" method="post">
	     <button type="submit" > Cancel </button>
      </form>
      <br />
  </div>
<style>
div {
    color: #777;
    margin: auto;
    width: 20em;
    text-align: center;
}
div#hbox {width: 100%;}
div#hbox div.box {float: left; width: 33%;}
input {
    background: #f8f8f8;
    border: 1px solid #777;
    margin: auto;
}
input:hover { background: #fefefe}
</style>