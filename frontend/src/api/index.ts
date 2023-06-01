import axios from 'axios';

const loginConfig = {
  baseURL: import.meta.env.VITE_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
}

export const LoginAPIInstance = axios.create(loginConfig);

const defaultConfig = {
  baseURL: import.meta.env.VITE_BASE_URL,
  headers: {
      'Content-Type': 'application/json',
  },
}

const token = localStorage.getItem('token');
if (token) defaultConfig.headers['Authorization'] = `Token ${token}`;

export const DefaultAPIInstance = axios.create(defaultConfig);