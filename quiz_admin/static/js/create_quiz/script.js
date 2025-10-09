function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }

const csrftoken = getCookie('csrftoken');
const baseUrl = 'http://127.0.0.1:8000/api/';
// let allQuiz = [];


function allQuizzes(quiz) {
    const ul = document.getElementById('lista');
    ul.innerHTML = ''; // Limpando a lista anterior;
    quiz.forEach(quizzes => {
        const li = document.createElement('li');
        li.innerHTML = `
                    <strong>${quizzes.text}</strong>
        `
        const btnDelete = document.createElement('button');
        const btnEdit = document.createElement('button');
        btnDelete.innerHTML = "Deletar";
        btnEdit.innerHTML = "Editar";
        li.appendChild(btnDelete);
        li.appendChild(btnEdit);
        ul.appendChild(li);
        
    });
}


async function createQuiz() {  
    const form = document.querySelector('.form-edit');
    form.addEventListener('submit', async function(e){ 
        e.preventDefault();
        const formData = new FormData(form);
        const data = Object.fromEntries(formData);
       
        try { 
            const response = await fetch(`${baseUrl}`, {
                method: "POST", 
                headers: { 
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken,
                },
                body: JSON.stringify(data),
                credentials: 'include', // Cookie da sessão vai junto
            });
            if (response.ok) { 
                alert('Quiz criado com suceo!');
                form.reset();
                getAllQuizzes();
            } else { 
                const errorData = await response.json();
                alert(`Erro ao criar quiz: ${response.status} - ${errorData.detail || 'Verifique se é admin'}`);
            }
        } catch(error) { 
            console.error('Erro no POST:', error);
            alert('Erro ao conectar com a API');
        }
    });
}

// async function deleteQuiz(id) {
//     try { 
//         const response = await fetch(`${baseUrl}`, { 
        
//     })
//     }
// }

async function getAllQuizzes() {
    try { 
        const response = await fetch(`${baseUrl}`);
        if (!response.ok) throw new Error(`Error: ${response.status}`);
        const dados = await response.json();
        allQuizzes(dados);
        // chame a função aqui
    } catch(error) { 
        console.error("Ocorreu um erro ao buscar os dados: ", error);
    }

}



document.addEventListener('DOMContentLoaded', () => { 
    getAllQuizzes(); // Carregando a lista inicial
    createQuiz();
});