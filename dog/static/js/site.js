var flag3 = 0;
    $(window).scroll(function () {
    alert("!!!!!");
      var height = $(document).scrollTop();
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

                              flag3=0;
                          }
                      }

                  }

