const BASE_URL = 'http://127.0.0.1:8000/api';
const URL_REFRESH = `${BASE_URL}/token/refresh`;

export function getAuthHeader() { 
    const accessToken = localStorage.getItem('access_token');
    if (!accessToken) { 
        throw new Error('Token de acesso não encontrado. Faça login novamente.');
    }

    return { 
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${accessToken}`,
    };
}

// Lógica de renovação do Token
export async function refreshAcessToken() { 
    // Pegando o refreshToken armazenado
    const refreshToken = localStorage.getItem('refresh_token');
    if (!refreshToken) { 
        // Forçando o logout e redirecionando se não tiver o token
        localStorage.clear();
        window.location.href = '/login.html';
        throw new Error("Sessão expirada. Faça login novamente.");
    }

    try { 
        // Requisição para pegar o refreshToken
        const response = await fetch(URL_REFRESH, { 
            method: 'POST', 
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({refresh: refreshToken})
        });

        if (!response.ok) { 
            logout();
            throw new Error('Refresh Token inválido ou espirado.');
            
        }

        // Recebendo o response e transformando em JSON
        const data = await response.json();
        // Pegando o novo accessToken
        const newAccessToken = data.access;

        localStorage.setItem('access_token', newAccessToken);
        console.log('Novo Access Token obtido com sucesso!');

        return newAccessToken; // Retorna o novo token
    } catch (error) { 
        // Limpar tudo e forçar o logout
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        logout();
        throw new Error(error.message);
        
    }
}

export function logout() { 
    localStorage.clear(); 
    window.location.href = '/login.html';
}
