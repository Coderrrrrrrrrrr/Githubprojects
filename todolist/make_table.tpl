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
<input type="button" name="save" value="刷新">
<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/jquery@3.2.1/dist/jquery.min.js"></script>
