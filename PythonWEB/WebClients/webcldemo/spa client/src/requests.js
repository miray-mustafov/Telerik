import { getToken } from "./token.js"

const BASE_URL = 'http://127.0.0.1:8000'

/**
 * 
 * @param {string} path 
 * @returns {Promise<any>}
 */
export const getJson = (path) => {
    const init = { headers: { 'x-token': getToken() || '' } }

    return fetch(`${BASE_URL}/${path}`, init).then(r => r.json())
}

export const updateRequest = (path, data) => {
    const init = {
        method: 'PUT',
        headers: {
            'x-token': getToken() || '',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }

    return fetch(`${BASE_URL}/${path}`, init)
}

export const createRequest = (path, data) => {
    const init = {
        method: 'POST',
        headers: {
            'x-token': getToken() || '',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }

    return fetch(`${BASE_URL}/${path}`, init)
}

export const deleteRequest = (path) => {
    const init = {
        method: 'DELETE',
        headers: { 'x-token': getToken() || '' }
    }

    return fetch(`${BASE_URL}/${path}`, init)
}