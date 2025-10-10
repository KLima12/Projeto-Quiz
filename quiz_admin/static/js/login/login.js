const form = document.getElementById('loginForm')

const baseUrl = 'http://127.0.0.1:8000';


async function handleLogin(user, password){ 
    try { 
        const response = await fetch(`${baseUrl}/token/`, { 
            method: 'POST', 
            headers: { 
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ 
                username: user, 
                password:password
            })
        });

        if (!response.ok) { 
            throw new Error('Falha no login. Verifique as credenciais.');
        }
        
        const data = await response.json();
        const accessToken = data.access;
        const refreshToken = data.refresh

        // Armazenando os tokens
        localStorage.setItem('access_token', accessToken);
        localStorage.setItem('refresh_token', refreshToken);

    } catch (error) { 
        console.error('Erro de login:', error);
        alert(error.message);
    }
}

form.addEventListener('submit', async function(e) { 
    const user = document.getElementById('username').value
    const password = document.getElementById('password').value

    handleLogin(user, password)
})
