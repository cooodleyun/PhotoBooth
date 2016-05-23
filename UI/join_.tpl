<html>
<title>photo booth-join</title>
<body>
<div style="text-align:center" >
<font color=blue >
<h1> PHOTO BOOTH </h1>
</font>
<h2> 회원가입 </h2>
<table>
<form action="/login" method="post">
	  id: <input name="username" type="text" />
</form>
	<form action="/login" method="delete">
	     <input value="ID check" type="submit"/>
	</form>
</table>	
<form action="/login" method="post">
	  Password: <input name="password" type="text" /></br>
	  Password: <input name="repassword" type="text" /></br>
	  E-mail: <input name="email" type="text" /></br>
          question :
             <select name=select size=1 >
              <option value="1"> 나이는 어떻게 됨? </option>
              <option value="2"> 사는 곳은 ? </option>
              <option value="3"> 취미는 뭐에요 ? </option>
              </select></br>
          answer: <input name="anwwer" type="text" /></br>
	</form>
<table>
	<form action="/login" method="delete">
	     <input value="back" type="submit"/>
	</form>
	<form action="/joinOk" method="get">
	     <input value="join" type="submit"/>
	</form>
</table>
</div>
</body>
</html>

