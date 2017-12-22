window.onload = function () {
    $(".page").each(function () {
        // 개별적으로 Wheel 이벤트 적용
        $(this).on("mousewheel DOMMouseScroll", function (e) {
            e.preventDefault();
            var delta = 0;
            if (!event) event = window.event;
            if (event.wheelDelta) {
                delta = event.wheelDelta / 120;
                if (window.opera) delta = -delta;
            } else if (event.detail) delta = -event.detail / 3;
            var moveTop = null;
                                
           
                                    // alert("!!!!");

            // 마우스휠을 위에서 아래로
            if (delta < 0) {
                
                if ($(this).next() != undefined) {
                    var tmp=$(this).offset().top;
                    moveTop = $(this).next().offset().top;
                    if (moveTop==0){
                        moveTop=tmp;
                    }
                    console.log(delta)

                }

            // 마우스휠을 아래에서 위로
            } else {
                if($(document).scrollTop()<800){
                    moveTop=0;
                }
                else if ($(this).prev() != undefined) {
                    moveTop = $(this).prev().offset().top;
                }
            }
            // 화면 이동 0.8초(800)
            $("html,body").stop().animate({
                scrollTop: moveTop + 'px'
            }, {
                duration: 300, complete: function () {
                }
            });
        });
    });
}

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("topBtn").style.display = "block";
    } else {
        document.getElementById("topBtn").style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    return $("html, body").animate({scrollTop:0},900),!1; // For Chrome, Safari and Opera 
    document.documentElement.scrollTop = 0; // For IE and Firefox
}



var flag1=0;
var flag3=0;

$(window).scroll(function () {

    /*  scroll 값  */
    var height = $(document).scrollTop();

    /*  scroll 값 확인용 함수호출  */
    log(height);


    /*  상단 고정 메뉴바 이벤트  */
                if(height > 100){
                    if(flag3==0){
                        $('.top').css("background-color", "#B5996D");
                        $('.top_logo_img').attr("src", "../../static/img/logo_txt_white.png");
                        //$('.top_logo_txt').animate({fontSize: '1.3rem'}, "fast");
                        $('.menu').css("color", "#ffffff");
                        
                        $('.top_logo').animate({
                            marginLeft : '10%',
                        });

                        $('.top_nav').animate({
                            marginLeft : '80%',
                            marginTop : '-2%'
                        });

                        $('.top').animate({
                            height : '3vw',
                        });

                        $('.top_nav').css({
                            /*
                            '-webkit-transform' : 'translate(-50%, 0%)',
                            '-ms-transform' : 'translate(-50%, 0%)',
                            '-moz-transform' : 'translate(-50%, 0%)',
                            '-o-transform' : 'translate(-50%, 0%)',
                            'transform' : 'translate(-50%, 0%)'
                            */
                        });
                        
                        flag3=1;
                    }
                }

                if(height < 100){
                    if(flag3==1){
                        $('.top').css("background-color", "white");
                        $('.top_logo_img').attr("src", "../../static/img/logo_txt_color.png");
                        //$('.top_logo_txt').animate({fontSize: '1rem'}, "fast");
                        $('.menu').css("color", "#B5996D");
                        

                        $('.top_logo').animate({
                            marginLeft : '50%',
                        });

                        $('.top_nav').animate({
                            marginLeft: '50%',
                            marginTop : '-0%'
                        });

                        $('.top').animate({
                            height : '5vw',
                        });

                        $('.top_nav').css({
                            '-webkit-transform' : 'translate(-50%, 0%)',
                            '-ms-transform' : 'translate(-50%, 0%)',
                            '-moz-transform' : 'translate(-50%, 0%)',
                            '-o-transform' : 'translate(-50%, 0%)',
                            'transform' : 'translate(-50%, 0%)'
                        });
                        flag3=0;
                    }
                }
});

function log(str){
    $('#tmp').text(str);
}

var flag_img1=0;
var flag_img2=0;
var flag_img3=0;
var flag_img4=0;



$(document).ready(function(){
    $("#showTruth1").click(function(){
        if(flag_img1==0){
            flag_img1=1;
            $("#stat_img1_2").css("visibility", "visible");
            $("#stat_img1_1").css("opacity", "0.5");
            $(".page").css("background-color", "#242424");
           
        }
        else{
            flag_img1=0;
            $("#stat_img1_2").css("visibility", "hidden");
            $("#stat_img1_1").css("opacity", "1"); 
            $(".page").css("background-color", "#F7F1E6");
    }
    });

    $("#showTruth2").click(function(){
        if(flag_img2==0){
            flag_img2=1;
            $("#stat_img2_2").css("visibility", "visible");
            $("#stat_img2_1").css("opacity", "0.5");
            $(".page").css("background-color", "#242424");
           
        }
        else{
            flag_img2=0;
            $("#stat_img2_2").css("visibility", "hidden");
            $("#stat_img2_1").css("opacity", "1"); 
            $(".page").css("background-color", "#F7F1E6");
    }
    });

    $("#showTruth3").click(function(){
        if(flag_img3==0){
            flag_img3=1;
            $("#stat_img3_2").css("visibility", "visible");
            $("#stat_img3_1").css("opacity", "0.5");
            $(".page").css("background-color", "#242424");
           
        }
        else{
            flag_img3=0;
            $("#stat_img3_2").css("visibility", "hidden");
            $("#stat_img3_1").css("opacity", "1"); 
            $(".page").css("background-color", "#F7F1E6");
    }
    });


    $("#showTruth4").click(function(){
        if(flag_img4==0){
            flag_img4=1;
            $("#stat_img4_2").css("visibility", "visible");
            $("#stat_img4_1").css("opacity", "0.5");
            $(".page").css("background-color", "#242424");
           
        }
        else{
            flag_img4=0;
            $("#stat_img4_2").css("visibility", "hidden");
            $("#stat_img4_1").css("opacity", "1"); 
            $(".page").css("background-color", "#FFF5E6");
    }
    });
});