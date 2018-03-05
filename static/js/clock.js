var animate, day, month, year, hours, minutes, seconds, date;

function init(){
    clock();
};

function bind(id, value){
    if (value < 10){
        value = '0' + value;
    }
    document.getElementById(id).innerHTML = value;
};

function clock(){
    date = new Date();
    seconds = date.getSeconds();
    minutes = date.getMinutes();
    hours = date.getHours();
    day = date.getDate();
    month = date.getMonth()+1;
    year = date.getFullYear();
    bind('sec', seconds);
    bind('min', minutes);
    bind('hours', hours);
    bind('day', day);
    bind('month', month);
    bind('year', year);
    animate = setTimeout(clock, 1000);
}

window.onload = init;