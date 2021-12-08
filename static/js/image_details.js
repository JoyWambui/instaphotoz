var submitButton=document.getElementById('commentButton')
submitButton.onclick= function () {
    const formToHide = document.getElementById('commentForm')
    formToHide.style.display = 'none';
}
var commentLink=document.getElementById('comment')
commentLink.onclick= function () {
    const formToDisplay = document.getElementById('commentForm')
    formToDisplay.style.display = 'block';
}

console.log('yes')