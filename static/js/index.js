        /*  scroll 이벤트 관리 변수 */
        var flag1 = 0;
        var flag2 = 0;
        var flag3 = 0;

/*  scroll 이벤트  */
        $(window).scroll(function () {

                /*  scroll 값  */
                var height = $(document).scrollTop();

                /*  scroll 값 확인용 함수호출  */
                log(height);


                /*  상단 고정 메뉴바 이벤트  */
                if(height > 100){
                    if(flag1==0){
                        $('.top').css("background-color", "#EDA900");
                        $('.top_logo_txt').css("color", "#ffffff")
                        //$('.top_logo_txt').animate({fontSize: '1.3rem'}, "fast");
                        $('.menu').css("color", "#ffffff");
                        flag1=1;
                    }
                }

                if(height < 100){
                    if(flag1==1){
                        $('.top').css("background-color", "transparent");
                        $('.top_logo_txt').css("color", "#EDA900");
                        //$('.top_logo_txt').animate({fontSize: '1rem'}, "fast");
                        $('.menu').css("color", "#EDA900");
                        flag1=0;
                    }
                }
        });

        /*  scroll 값 확인용 함수  */
        function log(str){
            $('#w').text(str);
            //$('#w').text(str);
        }

        function set_mark(){
            $('#mark1').show();
            $('#mark2').hide();
            $('#mark3').hide();
            $('#mark4').hide();
        }

        set_mark();