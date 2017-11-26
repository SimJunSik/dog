		/*  scroll 이벤트 관리 변수 */
		var flag1 = 0;
		var flag2 = 0;
		var flag3 = 0;


		/*  scroll 이벤트  */
		$(window).scroll(function () {

				/*  scroll 값  */
				var height = $(document).scrollTop();

				/*  scroll 값 확인용 함수호출  */


				/*  상단 고정 메뉴바 이벤트  */
				if(height > 100){
					if(flag1==0){
						$('.top').css("background-color", "#EDA900");
						$('.top_logo_txt').css("color", "#ffffff")
						$('.top_logo_txt').animate({fontSize: '50px'}, "fast");
						$('.menu').css("color", "#ffffff");
						flag1=1;
					}
				}

				if(height < 100){
					if(flag1==1){
						$('.top').css("background-color", "transparent");
						$('.top_logo_txt').css("color", "#EDA900");
						$('.top_logo_txt').animate({fontSize: '40px'}, "fast");
						$('.menu').css("color", "#EDA900");
						flag1=0;
					}
				}





				/*  Who we are 텍스트 강조 이벤트 */
				var who_we_are_offset = $('.who_we_are').offset().top;

				if(height > who_we_are_offset-100){
					if(flag2==0){
						$('#number').animate({fontSize: '3em'}, "slow");
						$('#number').css("color", "#EDA900");		
						flag2=1;
					}
				}




				/*  Our Team fadeIn 이벤트 */
				var self_introduction_offset = $('.self_introduction').offset().top;


				if(height > self_introduction_offset-100){
					if(flag3==0){
						$('#team1').fadeIn(1000);
						$('#team2').delay(500).fadeIn(1000);
						$('#team3').delay(600).fadeIn(1000);
						$('#team4').delay(700).fadeIn(1000);
						$('#team5').delay(800).fadeIn(1000);
						flag3=1;
					}
				}




				/*  배경이미지 변경 이벤트  */

				if(height > who_we_are_offset+100){
					$('.mid_img_src').attr("src","../../static/img/bg7.jpg");
				}

				if(height > self_introduction_offset+500){
					$('.mid_img_src').attr("src","../../static/img/bg8.jpg");
				}

				if (height < who_we_are_offset+100){
					$('.mid_img_src').attr("src","../../static/img/bg1.jpg");
				}
		});


		/*  scroll 값 확인용 함수  */
		function log(str){
		    $('#tmp').text(str);
		}


		/*  Top으로 스크롤링 함수  */
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