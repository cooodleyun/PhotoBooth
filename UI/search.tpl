<html>
<title>photo booth-search</title>
<body>
<div style="text-align:center" >
<font color=blue >
<h1> PHOTO BOOTH </h1>
</font>
<form action="/login" method=get>	
         question :
             <select name=select size=1 >
              <option value="1"> 나이는 어떻게 됨? </option>
              <option value="2"> 사는 곳은 ? </option>
              <option value="3"> 취미는 뭐에요 ? </option>
              </select></br>
         answer: <input name="janswer" type="text" /></br>
<table>
</form>
<form action="/login" method="delete">
  <input value="back" type="submit"/>
</form>
<form action="/pass" method="post">
  <input value="OK" type="submit"/>
</form>
</table>
</div>
</body>
</html>