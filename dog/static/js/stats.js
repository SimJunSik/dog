var mq = window.matchMedia( "(max-width: 780px)" );
if (mq.matches) {
    // window width is at less than 780px
}
else {
    // window width is greater than 780px
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

                var w = $(window).width();

                //alert(w);

                /*  scroll 값  */
                var height = $(document).scrollTop();


                //alert(w);

                if(w > 500){

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
                }


                if(w < 500){
                    if(height > 100){
                        $('.top').css({
                                '-webkit-transform' : 'translate(0%, -50%)',
                                '-ms-transform' : 'translate(0%, -50%)',
                                '-moz-transform' : 'translate(0%, -50%)',
                                '-o-transform' : 'translate(0%, -50%)',
                                'transform' : 'translate(0%, -50%)'
                            });
                    }

                    if(height < 100){
                        $('.top').css({
                                '-webkit-transform' : 'translate(0%, 0%)',
                                '-ms-transform' : 'translate(0%, 0%)',
                                '-moz-transform' : 'translate(0%, 0%)',
                                '-o-transform' : 'translate(0%, 0%)',
                                'transform' : 'translate(0%, 0%)'
                            });
                    }
                }
});

function log(str){
    //$('#tmp').text(str);
}
