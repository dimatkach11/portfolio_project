console.log('Its working');

let theme = localStorage.getItem('theme')

if(theme == null){
    setTheme('ligth')
}else{
    setTheme(theme)
}

let themeDots = document.getElementsByClassName('theme-dot')

for (var i=0; themeDots.length > i; i++){
    themeDots[i].addEventListener('click', function(){
        let mode = this.dataset.mode
        console.log('Option clicked:', mode)
        setTheme(mode)
    })
}

function setTheme(mode){
    if(mode == 'light'){
        document.body.style.setProperty('--mainColor', '#eaeaea')
        document.body.style.setProperty('--secondaryColor', '#fff')
        document.body.style.setProperty('--borderColor', '#c1c1c1')
        document.body.style.setProperty('--mainText', 'black')
        document.body.style.setProperty('--secondaryText', '#4b5156')
        document.body.style.setProperty('--themeDotBorder', '#24292e')
        document.body.style.setProperty('--previewBg','rgb(251, 249, 243, 0.8)')
        document.body.style.setProperty('--previewShadow','#f0ead6')
        document.body.style.setProperty('--buttonColor','black')
    }
    if(mode == 'blue'){
        document.body.style.setProperty('--mainColor', '#15202B')
        document.body.style.setProperty('--secondaryColor', '#192734')
        document.body.style.setProperty('--borderColor', '#164d56')
        document.body.style.setProperty('--mainText', '#fff')
        document.body.style.setProperty('--secondaryText', '#eeeeee')
        document.body.style.setProperty('--themeDotBorder', '#fff')
        document.body.style.setProperty('--previewBg','rgb(25, 39, 52, 0.8)')
        document.body.style.setProperty('--previewShadow','#111921')
        document.body.style.setProperty('--buttonColor','#17a2b8')
    }
    if(mode == 'green'){
        document.body.style.setProperty('--mainColor', '#606b56')
        document.body.style.setProperty('--secondaryColor', '#515a48')
        document.body.style.setProperty('--borderColor', '#161914')
        document.body.style.setProperty('--mainText', '#fff')
        document.body.style.setProperty('--secondaryText', '#eeeeee')
        document.body.style.setProperty('--themeDotBorder', '#fff')
        document.body.style.setProperty('--previewBg','rgb(81, 90, 72, 0.8)')
        document.body.style.setProperty('--previewShadow','#2a2f25')
        document.body.style.setProperty('--buttonColor','#669966')
    }
    if(mode == 'purple'){
        document.body.style.setProperty('--mainColor', '#46344e')
        document.body.style.setProperty('--secondaryColor', '#382a3f')
        document.body.style.setProperty('--borderColor', '#1d1520')
        document.body.style.setProperty('--mainText', '#fff')
        document.body.style.setProperty('--secondaryText', '#eeeeee')
        document.body.style.setProperty('--themeDotBorder', '#fff')
        document.body.style.setProperty('--previewBg','rgb(29, 21, 32, 0.8)')
        document.body.style.setProperty('--previewShadow','#2b202f')
        document.body.style.setProperty('--buttonColor','#8534a3')
    }

    localStorage.setItem('theme', mode)
}



var content = document.getElementById("content-about");
//var hidden = document.getElementsByClassName('hidden')
var button = document.getElementById("show-more");



button.onclick = function(){
    if(content.className == 'open'){
        //shrink the box
        content.className = '';
        button.innerHTML = 'Show more';
        //hidden.className = 'hidden';
        
    } else{
        //expand the box
        content.className = 'open';
        button.innerHTML = 'Show less';
        //hidden.className = '';
    }
};





//var achievements = document.getElementById("achievements");
//var moreAchievements = document.getElementById("more-achievements");


//moreAchievements.onclick = function(){
//    if(achievements.className == 'open'){
//        //shrink the box
//        achievements.className = '';
//        moreAchievements.innerHTML = '...';

//    } else{
//        //expand the box
//        achievements.className = 'open';
//        moreAchievements.innerHTML = 'Show less';
//    }
//};