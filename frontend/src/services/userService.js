import { authHeader } from '../store/auth-header';
import { handleResponse } from '../store/handler';

export const userService = {
    login,
    logout,
    register,
    getAll,
    getById,
    update,
    delete:_delete
}

function login(username,password){
    const requestOptions = {
        method = 'POST',
        headers:{'Content-Type':'application/json'},
        body : JSON.stringify({username,password})
    };

    return fetch('/login/',requestOptions).then(handleResonse)
        .then(user => {
            if( user.token){
                localStorage.setItem('user',JSON.stringify(user));
            }

            return user;
        })
}

function logout() {
    localStorage.removeItem('user');
}

function register(user) {
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(user)
    };

    return fetch('/register/', requestOptions).then(handleResponse);
}

function getAll() {
    const requestOptions = {
        method: 'GET',
        headers: authHeader()
    };

    return fetch('/users/', requestOptions).then(handleResponse);
}

function getById(id) {
    const requestOptions = {
        method: 'GET',
        headers: authHeader()
    };

    return fetch('/users/${id}/', requestOptions).then(handleResponse);
}

function update(user) {
    const requestOptions = {
        method: 'PUT',
        headers: { ...authHeader(), 'Content-Type': 'application/json' },
        body: JSON.stringify(user)
    };

    return fetch('/users/${user.id}/', requestOptions).then(handleResponse);
}

function _delete(id) {
    const requestOptions = {
        method: 'DELETE',
        headers: authHeader()
    };

    return fetch('/users/${id}', requestOptions).then(handleResponse);
}

