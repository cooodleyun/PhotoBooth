<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<title> photo booth </title>
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
      <h2>Login</h2>
      <p>Please insert your credentials:</p>
<table>
      <form action="login" method="post" name="login">
          Username : <input type="text" name="username" />
          password : <input type="password" name="password" />
          <button type="submit" > OK </button>
      </form>
</table>
<table>
	<form action="join_btn" method="post" name="join">
		<button type="submit" > JOIN </button>
	</form>
	<form action="reset_passwd" method="post" name="reset_passwd">
		<button type="submit" > SEARCH </button>
	</form>
</table>
 </div>
  <br style="clear: left;" />
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
</body>
</html>