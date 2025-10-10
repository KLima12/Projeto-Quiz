import { refreshAcessToken } from "../auth/authApi.js";

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }

const csrftoken = getCookie('csrftoken');
const baseUrl = 'http://127.0.0.1:8000/api';
// let allQuiz = [];



function allQuizzes(quiz) {
    console.log(quiz);
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
    const form = document.querySelector('#form-edit');
    form.addEventListener('submit', async function(e){ 
        e.preventDefault();
        const formData = new FormData(form);
        const data = Object.fromEntries(formData);
        
        // Função auxiliar que faz a requisição e lida com o token
        const makeRequest = async (token) => { 
            // Criando o objeto Headers
            const requestHeaders = { 
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`, // Token renovado/atual
                "X-CSRFToken": csrftoken,
            };
            
            // Fazendo requisição
            return fetch(`${baseUrl}/create-quiz/`, { 
                method: "POST", 
                headers: requestHeaders, 
                body: JSON.stringify(data),
            });
        };

        try { 

            // 1. Primeira tentativa
            let accessToken = localStorage.getItem('access_token');
            let response = await makeRequest(accessToken);
            
            // 2. Se a primeira tentativa falhar por 401
            if (response.status === 401) { 
                console.log("Token expirado. Tentando renovar...");
                // Renovando o token e pegando o novo
                const newAccessToken = await refreshAcessToken();
                
                // Tentando requisição mais uma vez
                response = await makeRequest(newAccessToken);
            }

            // Processando o resultado final
            if (response.ok) { 
                alert('Quiz criado com sucesso!');
                form.reset();
                getAllQuizzes();
            } else if (response.status === 401) { 
                // Se persistir o 401, significa que o refresh_token falhou!
                alert("Sessão totalmente expirada ou problema de permissão. Faça login.");
            } else { 
                const errorData = await response.json();
                alert(`Erro ao criar quiz: ${response.status} - ${errorData.detail || JSON.stringify(errorData)}`);
            }

        } catch(error) { 
            console.error('Erro no POST ou no Refresh: ', error);
            alert(`Erro: ${error.message}`);
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
        console.log(dados)
        // chame a função aqui
    } catch(error) { 
        console.error("Ocorreu um erro ao buscar os dados: ", error);
    }

}



document.addEventListener('DOMContentLoaded', () => { 
    getAllQuizzes(); // Carregando a lista inicial
    createQuiz();
});