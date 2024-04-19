const TOKEN_KEY = 'token'

export const getToken = () => sessionStorage.getItem(TOKEN_KEY)
export const saveToken = (token) => sessionStorage.setItem(TOKEN_KEY, token)
export const deleteToken = () => sessionStorage.removeItem(TOKEN_KEY)