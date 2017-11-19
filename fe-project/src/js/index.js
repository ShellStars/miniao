var canShowVideoDetail = false;

$(function () {

  showVideoAlert();

  $("#btn_login").click(function () {
    $('.modal-login').show(300);
  });
  $('.modal-login .login-close').click(function () {
    $('.modal-login').hide(150);
  });
  $('.modal-login button').click(function (e) {
    e.preventDefault();
    $('.modal-login .error').text('');
    var telnum = $('.modal-login .ipt-telnum');
    var password = $('.modal-login .ipt-password');
    if (!telnum) {
      $('.modal-login .error').text('请输入手机号');
      return false;
    }
    if (!password) {
      $('.modal-login .error').text('请输入密码');
      return false;
    }
    $.ajax({
      url: '/userdata/login/',
      type : "POST",
      data: $('.modal-login form').serialize(),
      success: function (res) {
        if (res.info == 'success') {
          window.location.href = '/userdata/show';
          return false;
        }
        $('.modal-login .error').text(res.info);
      },
      error: function () {
        $('.modal-login .error').text('系统错误');
      }
    });
  });



  // 判断登录态
  $.ajax({
    url: '/userdata/navigationinfo/',
    type: 'get',
    success: function (ret) {
      ret.username && $('.header-wrap .profile').html('\
        <a href="/userdata/show" class="profile-islogin">\
          <img src="' + ret.headimg + '" alt="AVATAR">\
          <h6>'+ ret.username +'</h6>\
        </a>\
        <a href="" class="btn-layout">退出</a>\
      ');

      ret.username && $('.my-score').show();
      // 评分
      var score = $('.score-box').attr('data-score');
      if ($('.score-box')[0]) {
        if (score === 'no') {
          var score = 5;
          $('.score-box i').click(function () {
            $('.score-box')[0].className = 'score-box';
            $('.score-box').addClass('score-' + ($(this).index() + 1));
            score = $(this).index() + 1;
          });

          $('.submit-score').click(function () {
            $.ajax({
              url: '/userdata/scoreclass/',
              method: 'get',
              data: {
                scorenum: score,
                url: window.location.href,
              },
              success: function (rrr) {
                if (rrr.info === 'success') {
                  window.location.reload();
                } else {
                  alert('评分失败');
                }
              },
              error: function () {
                alert('评分失败');
              }
            });
          });
        } else {
          score && (score = score.toString());
          if (score.length > 1) {
            $('.score-box').addClass('score-' + score[0]);
          } else {
            $('.score-box').addClass('score-' + score);
          }
          $('.submit-score').hide();
        }
      }

      // if (ret.identity === 0 || ret.identity === 2) {
      //   $('.video-hide').show();
      // }
      if (ret.state == 'fail' && window.isVideo) {
        // showVideoAlert();
      }
      ret.username && (canShowVideoDetail = true);

      $('.btn-layout').click(function (e) {
        e.preventDefault();
        var img = new Image();
        img.src = 'http://changyan.sohu.com/api/2/logout?client_id=cyti4u9K7';
        img.onload = function() {
          window.location.href = "/userdata/logout";
        }
        setTimeout(function () {
          window.location.href = "/userdata/logout";
        }, 2000);
      });
    },
    error: function() {
      // showVideoAlert();
    }
  })


  $('#btn-collect').click(function () {
    var t = this;
    if ($(this).attr('data-action') == 1) {
      $.ajax({
        url: '/userdata/collect/',
        method: 'get',
        data: {
          title: $(this).attr('data-title'),
          url: window.location.href,
        },
        success: function (data) {
          if (data.info === 'fail') {
            alert('请登录后收藏');
            return ;
          }
          $(t).text('取消收藏');
          $(t).attr('data-action', '0');
        }
      });
    } else {
      $.ajax({
        url: '/userdata/cancel/',
        method: 'get',
        data: {
          title: $(this).attr('data-title'),
          url: window.location.href,
        },
        success: function () {
          $(t).text('收藏');
          $(t).attr('data-action', '1');
        }
      });
    }
  });


  $('.header-wrap .select-box .select-value').click(function () {
    if (!$(this).hasClass('active')) {
      $('.header-wrap .select-box ul').show();
      $(this).addClass('active');
    } else {
      $('.header-wrap .select-box ul').hide();
      $(this).removeClass('active');
    }
  });
  $('.header-wrap .select-box ul li').click(function () {
    $('.header-wrap .select-box .select-value span').text($(this).text());
    $('.header-wrap .hidden-ipt').val($(this).attr('data-value'));
    $('.header-wrap .select-box ul').hide();
    $('.header-wrap .select-box .select-value').removeClass('active');
  });

  $('.video-container .video-list').length && $('.video-container .video-list').masonry({
    // options...
    itemSelector: 'li',
    columnWidth: $('.video-container .video-list li').width()
  });
  $('.article-container .article-list').length && $('.article-container .article-list').masonry({
    // options...
    itemSelector: 'li',
    columnWidth: $('.article-container .article-list li').width()
  });
  $('.album-list').length && $('.album-list').masonry({
    // options...
    itemSelector: 'li',
    columnWidth: $('.album-list li').width()
  });
  //
});
function getUrlParam(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if (r != null) return (r[2]); return '';
}

function param(obj) {
  var arr = [];
  for (var key in obj) {
    arr.push(key + '=' + obj[key]);
  }
  return arr.join('&');
}
function showVideoAlert() {
  $('.video-list li a, .section-mix .box-article ul li a').click(function (e) {
    if (!canShowVideoDetail) {
      e.preventDefault();
      $('.modal-vodeo').show();
    }
  });
}
