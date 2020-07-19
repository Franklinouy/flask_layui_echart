layui.use(['table', "jquery"], function () {
    var $ = layui.$,
        table = layui.table;

    //第一个实例
    table.render({
        elem: '#demo'
        , url: '/query_all' //数据接口
        , toolbar: '#demo'
        , page: true //开启分页
        , id: "studentTable"
        , limit: [10]
        , limits: [10, 20, 50, 100]
        , cols: [[ //表头
            {field: 'name', title: '姓名', width: 400}
            , {field: 'age', title: '年龄', width: 400}
            , {field: 'url', title: '网址', width: 400}
        ]],
    });

    $("#search").click(function () {
        var content = $("#content").val()
        console.log(content)
        if (content !== "") {
            table.reload('studentTable', {
                url: '/query_all'
                , method: 'post'
                , where: {content: content} //设定异步数据接口的额外参数
                , page: {
                    curr: 1 //重新从第 1 页开始
                }
            })
        } else {
            table.reload('studentTable', {
                url: '/query_all'
                , method: 'post'
                , where: {content: ""} //设定异步数据接口的额外参数
                , page: {
                    curr: 1 //重新从第 1 页开始
                }
            })
        }

    })

});