$(document).ready(function(){
    var headingScroll = document.getElementById('block-heading-scroll');
    var appsScroll = document.getElementById('block-apps-scroll');

    headingScroll.onclick = function(e){
        appsScroll.scrollIntoView({
            block: "start",
            behavior: "smooth"
        });
    };
});

