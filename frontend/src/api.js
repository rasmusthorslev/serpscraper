import axios from 'axios';

const API_BASE = 'http://localhost:8000/api/';

export const getClients = () => axios.get(`${API_BASE}clients/`).then(res => res.data);
export const getKeywords = () => axios.get(`${API_BASE}keywords/`).then(res => res.data);
export const getRankResults = () => axios.get(`${API_BASE}rankresults/`).then(res => res.data);