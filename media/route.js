$(document).ready(function(){
    $(".next-btn").on('click',function(e){
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/users/register/validateForm1",
            data: {
                email:$('#email').val(),
                username:$('#username').val(),
                pswd:$('#pswd').val(),
                csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(data){
                console.log(data['no_account'][0])
                if(data['no_account'][0]==='true'){
                $('.data1').animate({right:'450px',opacity:'0'},'fast')
                $('.server-message').addClass('success')
                $('.server-message').html("Email validated")
                $('.server-message').animate({top:'-5px',opacity:'1'},'fast')
                setTimeout(function(){
                    $('.server-message').animate({top:'-5px',opacity:'0'},'fast')
                },1500)
                $('.data2').animate({left:'20px'})
                $('.data1').html('')
            }
            else{
                $('.data1').animate({top:'-10vh'},'fast')
                $('.data1').animate({top:'0vh'},'fast')
                $('.server-message').addClass('critical')
                $('.server-message').html("Email already exist")
                $('.server-message').animate({top:'-5px',opacity:'1'},'fast')
                setTimeout(function(){
                    $('.server-message').animate({top:'-85px',opacity:'0'},'fast')
                },1500)
            }
            },
            error:function(data){
                $('.data1').animate({top:'-10vh'},'fast')
                $('.data1').animate({top:'0vh'},'fast')
                $('.server-message').addClass('critical')
                $('.server-message').html("Server Error"+data.status)
                $('.server-message').animate({top:'-5px',opacity:'1'},'fast')
                setTimeout(function(){
                    $('.server-message').animate({top:'-85px',opacity:'0'},'fast')
                },1500)
            }
        });
    })
})



$(document).ready(function(){
    $(".form2").on('submit',function(e){
    
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/users/register/done",
            data: {
                acc_type:$('.acc_type').find(":selected").text(),
                bio:$('#my-bio').val(),
                dob:$('#date-ob').val(),
                ques:$('#ques').find(":selected").text(),
                ans:$('#ans').val(),
                csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken][1]').val()
                
            },
            success: function(data){
                if(data==='created'){
                    $('.data2').html(`<h1>loading...</h1>`)
                    $('.data2').animate({right:'450px',opacity:'0'},'fast')
                    $('.server-message').addClass('success')
                    $('.server-message').html("Account created")
                    $('.server-message').animate({top:'-5px',opacity:'1'},'fast')
                    setTimeout(function(){
                        $('.server-message').animate({top:'-5px',opacity:'0'},'fast')
                    },1500)
                    $('.data3').animate({left:'20px'})
            }
            else{
            console.log(data)
            $('.data2').animate({top:'-10vh'},'fast')
            $('.data2').animate({top:'5vh'},'fast')
            $('.server-message').removeClass('success')
            $('.server-message').addClass('critical')
            $('.server-message').html("Not created problem with data")
            $('.server-message').animate({top:'-5px',opacity:'1'},'fast')
            setTimeout(function(){
                $('.server-message').animate({top:'-85px',opacity:'0'},'fast')
            },1500)
            }
            },
            error:function(data){
            $('.data2').animate({top:'-10vh'},'fast')
            $('.data2').animate({top:'5vh'},'fast')
            $('.server-message').removeClass('success')
            $('.server-message').addClass('critical')
            $('.server-message').html("Server Error"+data.status)
            $('.server-message').animate({top:'-5px',opacity:'1'},'fast')
            setTimeout(function(){
                $('.server-message').animate({top:'-85px',opacity:'0'},'fast')
            },1500)
            }
        });
    })
})


$(document).ready(function(){
    $(".sub-btn").on('click',function(e){
        let datsa= {
            insta:$('#insta').val(),
            twitter:$('#twitter').val(),
            twitch:$('#twitch').val(),
            facebook:$('#fb').val(),
            youtube:$('#yt').val(),
            snapchat:$('#snap').val(),
            phone:$('#phoneno').val(),
            gmail:$('#gmail').val(),
            ds:$('#dscod').val(),
            telegram:$('#telegram').val(),
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
        }
        console.log(datsa),
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/users/register/socialDone/",
            data: {
                insta:$('#insta').val(),
                twitter:$('#twitter').val(),
                twitch:$('#twitch').val(),
                facebook:$('#fb').val(),
                youtube:$('#yt').val(),
                snapchat:$('#snap').val(),
                phone:$('#phoneno').val(),
                gmail:$('#gmail').val(),
                ds:$('#ds').val(),
                telegram:$('#tele').val(),
                csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
            },
            
            success: function(data){
                if(data==='created'){
                    location.reload()
            }
            else{
            $('.data2').animate({top:'-10vh'},'fast')
            $('.data2').animate({top:'5vh'},'fast')
            $('.server-message').removeClass('success')
            $('.server-message').addClass('critical')
            $('.server-message').html("Server error"+data.status)
            $('.server-message').animate({top:'-5px',opacity:'1'},'fast')
            setTimeout(function(){
                $('.server-message').animate({top:'-85px',opacity:'0'},'fast')
            },1500)
            }
            },
            error:function(data){
            $('.data2').animate({top:'-10vh'},'fast')
            $('.data2').animate({top:'5vh'},'fast')
            $('.server-message').removeClass('success')
            $('.server-message').addClass('critical')
            $('.server-message').html("Server Error"+data.status)
            $('.server-message').animate({top:'-5px',opacity:'1'},'fast')
            setTimeout(function(){
                $('.server-message').animate({top:'-85px',opacity:'0'},'fast')
            },1500)
            }
        });
    })
})


$(document).ready(function(){
    $(".login").on('click',function(e){
        e.preventDefault;
        let status_d;
        status_d = true;
        if(status_d==true){
            $('.data1').animate({right:'450px',opacity:'0'},'fast')
            $('.data4').animate({left:'10px'})
        }
        else{
            $('.data2').animate({top:'-10vh'},'fast')
            $('.data2').animate({top:'5vh'},'fast')
            $('.server-message').removeClass('success')
            $('.server-message').addClass('critical')
            $('.server-message').html("Problem occured")
            $('.server-message').animate({top:'-5px',opacity:'1'},'fast')
            setTimeout(function(){
                $('.server-message').animate({top:'-85px',opacity:'0'},'fast')
            },1500)
        }
    })
})

$(document).ready(function(){
    $(".login-btn").on('click',function(e){
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/users/login/",
            data: {
                username:$('#log-username').val(),
                password:$('#log-pswd').val(),
                csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(data){
                if(data==='success'){
                    $('.forms').animate({opacity:'0'},'fast')
                    $('.server-message').addClass('success')
                    $('.server-message').html("Login successfull")
                    $('.server-message').animate({top:'-5px',opacity:'1'},'fast')
                    setTimeout(function(){
                        $('.server-message').animate({top:'-5px',opacity:'0'},'fast')
                    },1500)
                    location.reload();
            }
            else{
            $('.data3').animate({top:'-10vh'},'fast')
            $('.data3').animate({top:'5vh'},'fast')
            $('.server-message').removeClass('success')
            $('.server-message').addClass('critical')
            $('.server-message').html("Username or password invalid")
            $('.server-message').animate({top:'-5px',opacity:'1'},'fast')
            setTimeout(function(){
                $('.server-message').animate({top:'-85px',opacity:'0'},'fast')
            },1500)
            }
            },
            error:function(data){
            $('.data3').animate({top:'-10vh'},'fast')
            $('.data3').animate({top:'5vh'},'fast')
            $('.server-message').removeClass('success')
            $('.server-message').addClass('critical')
            $('.server-message').html("Server Error"+data.status)
            $('.server-message').animate({top:'-5px',opacity:'1'},'fast')
            setTimeout(function(){
                $('.server-message').animate({top:'-85px',opacity:'0'},'fast')
            },1500)
            }
        });
    })
})

function readyJs(){
    alert("js loaded succesfully!")
}
readyJs()