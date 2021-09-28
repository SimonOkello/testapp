const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn  = document.getElementById('start-button')
const url = window.location.href


modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
  const pk =modalBtn.getAttribute('data-pk')
  const name=modalBtn.getAttribute('data-quiz')
  const topic=modalBtn.getAttribute('data-topic')
  const numOfQuestions=modalBtn.getAttribute('data-questions')
  const timeToComplete=modalBtn.getAttribute('data-time')
  const passMark=modalBtn.getAttribute('data-pass')
  const difficulty=modalBtn.getAttribute('data-dificulty')
  modalBody.innerHTML = `
  <div class="h5 mb-3">Are you sure you want to start "<b> ${name}</b>"?</div>
  <div  class="text-muted">
     <ul>
     <li>Topic: <b>${topic}</b></li>
     <li>No of Questions: <b>${numOfQuestions}</b></li>
     <li>Time To Complete: <b>${timeToComplete} min</b></li>
     <li>Pass Mark: <b>${passMark}%</b></li>
     <li>Dificulty: <b>${difficulty}</b></li>
     </ul>
  </div>
  `

  startBtn.addEventListener('click', ()=>{
    window.location.href  = url + pk
  })
}))