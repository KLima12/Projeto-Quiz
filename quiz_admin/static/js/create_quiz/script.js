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

        ul.appendChild(li);
    });
}


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
    const form = document.getElementById('form-edit');
    if (form) { 
        form.addEventListener('submit', async (e)=> { 
            e.preventDefault();

            const token = localStorage.getItem('acessToken');
            console.log('token: ',token)
            if (!token) { 
                alert('Faça login primeiro!');
                return;
            }

            const formData = new FormData(form);
            const data = { 
                text: formData.get('text'),
                description: formData.get('description')
            };

            try { 
                const response = await fetch(`${baseUrl}`, { 
                    method: 'POST', 
                    headers: { 
                        'Authorization': `Bearer ${token}`,
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken
                    },
                    body: JSON.stringify(data)
                });

                if (response.ok) { 
                    alert('Quiz criado!');
                    form.reset(); // Limpando o Form.
                    getAllQuizzes(); // Aqui vou atualizar a lista na hora.
                
                } else { 
                    alert('Erro ao criar quiz!');
                } 
            } catch(error) { 
                console.error('Erro no submit: ', error);
            }
            
        })
    }

})