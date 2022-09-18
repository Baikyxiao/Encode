function add_public_key(){
    ff = document.getElementById("data").getAttribute("value")
    if (ff == "Json"){
        check();
    }               
    else if (ff == "JavaScript"){

        input = document.getElementById("input-text").value
        console.log(input)
        key = document.getElementById("input-center-text").value
        post('../index/',{"input":input,"ff":ff,"key":key});
    }
    else{
        input = document.getElementById("input-text").value
        console.log(input)
        key = document.getElementById("input-center-text").value

        window.location.href = "../index?input=" + input + "&fun=" + ff + "&key=" + key;
    }

}

function fun(str){
    document.getElementById("data").setAttribute("value",str);
    alert("you choice " + str);
}



function post(url, params) { 
    // 创建form元素
    var temp_form = document.createElement("form");
    // 设置form属性
    temp_form .action = url;      
    temp_form .target = "_self";
    temp_form .method = "post";      
    temp_form .style.display = "none";
    // 处理需要传递的参数 
    for (var x in params) { 
        var opt = document.createElement("textarea");      
        opt.name = x;      
        opt.value = params[x];      
        temp_form .appendChild(opt);      
    }      
    document.body.appendChild(temp_form);
    // 提交表单      
    temp_form .submit();     
} 



function check(){
        console.log("##")
    　　var text_value = document.getElementById('input-text').value;
    　　if(text_value == ""){
       　　alert("不能为空");
       　　return false;
    　　} else {
            var res="";
            for(var i=0,j=0,k=0,ii,ele;i<text_value.length;i++)
            {//k:缩进，j:""个数
                ele=text_value.charAt(i);
                if(j%2==0&&ele=="}")
                {
                    k--;
                    for(ii=0;ii<k;ii++) ele="    "+ele;
                    ele="\n"+ele;
                }
                else if(j%2==0&&ele=="{")
                {
                    ele+="\n";
                    k++;
                    for(ii=0;ii<k;ii++) ele+="    ";
                }
                else if(j%2==0&&ele==",")
                {
                    ele+="\n";
                    for(ii=0;ii<k;ii++) ele+="    ";
                }
                else if(ele=="\"") j++;
                res+=ele;
            }
        　　document.getElementById('output-text').value = res;
    　　}
    }