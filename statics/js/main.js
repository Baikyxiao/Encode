function add_public_key(){
    ff = document.getElementById("data").getAttribute("value")
    if (ff == "Json"){
        check();
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