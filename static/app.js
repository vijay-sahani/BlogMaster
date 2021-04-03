$('#toggleBtn').on('click',function(){
    let toggleBtn=document.getElementById('toggleBtn');
    console.log('hi')
    let Text=document.getElementById("extraText");
    if (Text.style.display=='inline'){
        Text.style.display='none';
        toggleBtn.innerHTML='<a>ReadMore</a>';
    }
    else{
        Text.style.display='inline';
        toggleBtn.innerHTML='<a>ReadLess</a>'
    }
});

