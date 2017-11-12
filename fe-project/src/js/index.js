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
      ');
    }
  })
});
