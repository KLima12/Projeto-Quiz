 function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }

const csrftoken = getCookie('csrftoken');

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    if (loginForm) { 
        loginForm.addEventListener('submit', async (event)=> { 
            event.preventDefault();

            const username = document.getElementById('id_username').value;
            const password = document.getElementById('id_password').value;

            try { 
                const response = await fetch('/api/token/', { 
                    method: "POST", 
                    headers: { 
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken 
                    },
                    // Passando o username e password
                    body: JSON.stringify({username, password}),
                });
                if (!response.ok) {
                    // Se a resposta não vier OK 
                    const errorData = await response.json();
                    alert(`Erro no login: ${errorData.detail || 'credenciais inválidas'}`);
                    throw new Error('Falha na autentificação');
                }

                const data = await response.json();


                localStorage.setItem('accessToken', data.access);
                localStorage.setItem('refreshToken', data.refresh);

                console.log('Login bem-sucedido! Tokens armazenados.');
                alert('Login realizado com sucesso!');
                
                window.location.href = '/api/create-quiz/';
            } catch (error){ 
                console.error('Ocorreu um erro durante o login: ', error)
            }
        })
    }
})