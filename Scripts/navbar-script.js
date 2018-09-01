console.log("Navbar Script Connected");

var wrapper = document.querySelector(".wrapper");
wrapper.onscroll = function()
{
  var navBar = document.getElementById("navbar");
  var Btn = navBar.querySelectorAll(".btn");
  console.log(wrapper.scrollTop);

  if (wrapper.scrollTop > 1500)
  {
    for (var i = 0; i < Btn.length; i++) {
        Btn[i].classList.add('changeStyle');
    }
  }
  else
  {
    for (var i = 0; i < Btn.length; i++) {
        Btn[i].classList.remove('changeStyle');
    }
  }
}
