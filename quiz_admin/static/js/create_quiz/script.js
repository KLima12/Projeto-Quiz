 function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }

const csrftoken = getCookie('csrftoken');
const baseUrl = "http://127.0.0.1:8000/api/"
// let allQuiz = [];



function renderAllQuizes(allQuizzes) {
    const existingEditForm = document.querySelector('.form-edit');
    if (existingEditForm) {
        existingEditForm.remove()
    }

    const ulPeding = document.getElementById('lista');
    ulPeding.innerHTML = '';
    
    allQuizzes.forEach(quizzes => { 
        const li = document.createElement('li')
    li.dataset.quizId = allQuiz.id;
    li.innerHTML = `
        <strong>${quizzes.text}</strong><br>
        ${quizzes.desciption}
    `;
    ulPeding.appendChild(li)
    });
    
}



async function fetchAllQuizzes() {
    try { 
        const response = await fetch(`${baseUrl}`);
        if (!response.ok) throw new Error(`Erro: ${response.status}`);
        const allQuizzes = await response.json()
        renderAllQuizes(allQuizzes);
    } catch(error){ 
        console.error("Erro ao buscar todos os quizes!", error.message);
    }
}


document.addEventListener('DOMContentLoaded', fetchAllQuizzes);