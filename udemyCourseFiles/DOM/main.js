var restart = document.querySelector("#re")
var boxes = document.querySelectorAll('td')
console.log(restart);
console.log(boxes);
function restartGame(){
  for(var i=0;i<boxes.length;i++)
    boxes[i].textContent='';
}
function addInput(){
  if(this.textContent==='')
    this.textContent='X';
  else if(this.textContent==='X')
    this.textContent='O';
  else
    this.textContent='';
}
restart.addEventListener('click',restartGame);

for(var i=0;i<boxes.length;i++){
  boxes[i].addEventListener('click',addInput);
}
