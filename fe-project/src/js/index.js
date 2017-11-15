$(function () {
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
        <a href="/userdata/logout" class="btn-layout">退出</a>\
      ');

      if (ret.identity === 0 || ret.identity === 2) {
        $('.video-hide').show();
      }
    }
  })
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
