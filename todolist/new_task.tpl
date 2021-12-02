<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/jquery@3.2.1/dist/jquery.min.js"></script>
<p>添加一个你接下来要做的计划：</p>
<form action="/new" method="get">
    <input type="text" size="100" maxlength="100" name="task">
    <input type="submit" name="save" value="提交">
</form>

<input type="button" id="refresh" name="save" value="回到计划清单" onclick=refresh()>
<script type="text/javascript">
    function refresh(){
        location.href="/todo"
    }
</script>