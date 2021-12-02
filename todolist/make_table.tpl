<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/jquery@3.2.1/dist/jquery.min.js"></script>
<p>这是你接下来要做的事情：</p>
<table border="1">
    %for row in rows:
    <tr>
        %for col in row:
        <td>{{col}}</td>
        %end
    </tr>
    %end
</table>
<input type="button" id="refresh" name="save" value="刷新" onclick=refresh()>
<input type="button" id="addlist" name="save" value="新增" onclick=new_list()>
<input type="text" id="del_num" size="100" maxlength="100">
<input type="button" id="del_fun" name="save" value="删除" onclick="javascript:void(0);">
<script type="text/javascript">
    function refresh(){
        location.href="/todo"
    }
    function new_list(){
        location.href="/new"
    }
    $(function () {//获取表单并跳转
            $("#del_fun").click(function () {
                var key=$("#del_num").val();
                var url="/edit/"+key;
                location.href=url;
            });
        });
</script>