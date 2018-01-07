		/*  scroll 이벤트 관리 변수 */
		var flag1 = 0;
		var flag2 = 0;
		var flag3 = 0;


		/*  scroll 이벤트  */
		$(window).scroll(function () {

				/*  scroll 값  */
				var height = $(document).scrollTop();

				/*  scroll 값 확인용 함수호출  */




				/*  Who we are 텍스트 강조 이벤트 */
				/*
				var who_we_are_offset = $('.who_we_are').offset().top;

				if(height > who_we_are_offset-100){
					if(flag2==0){
						$('#number').animate({fontSize: '3em'}, "slow");
						$('#number').css("color", "#EDA900");		
						flag2=1;
					}
				}
				*/



				/*  Our Team fadeIn 이벤트 */
				var self_introduction_offset = $('.self_introduction').offset().top;


				if(height > self_introduction_offset-100){
					//var container_obj = document.getElementsByClassName('container');
					if(flag2==0){
						$('.team1').fadeIn(1000);
						$('.team2').delay(500).fadeIn(1000);
						$('.team3').delay(600).fadeIn(1000);
						$('.team4').delay(700).fadeIn(1000);
						$('.team5').delay(800).fadeIn(1000);
						flag2=1;
					}
				}




				/*  배경이미지 변경 이벤트  */
				/*
				if(height > who_we_are_offset+100){
					$('.mid_img_src').attr("src","../../static/img/bg7.jpg");
				}

				if(height > self_introduction_offset+500){
					$('.mid_img_src').attr("src","../../static/img/bg8.jpg");
				}

				if (height < who_we_are_offset+100){
					$('.mid_img_src').attr("src","../../static/img/bg1.jpg");
				}
				*/

                var w = $(window).width();



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

                            $('.menu').css("color", "black");
                            

                            $('.top_logo').animate({
                                marginLeft : '50%',
                            });

                            $('.top_nav').animate({
                                marginLeft: '50%',
                                marginTop : '1%'
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


		/*  scroll 값 확인용 함수  */
		/*
		function log(str){
		    $('#tmp').text(str);
		}
		*/

		/*  Top으로 스크롤링 함수  */
		/*
		$(document).ready(function(){
			$(".top_scroll").click(function(){
				return $("html, body").animate({scrollTop:0},900),!1})

			$(".top, .top_scroll").hide();

			$(function () {
				$(window).scroll(function () {
					if ($(this).scrollTop() > 100) {
						$('.top, .top_scroll').fadeIn();
					} else {
						$('.top, .top_scroll').fadeOut();
					}
				});
			});
		});
		*/