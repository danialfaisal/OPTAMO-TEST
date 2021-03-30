/* eslint-disable */
import axios from 'axios';

// Production environment URL
/* https://optamo-backend.herokuapp.com */

// Development environment URL
// http://localhost:8000

const API_URL = 'http://localhost:8000';

export class APIService {
  constructor() {

  }

   getWeatherList() {
    const url = `${API_URL}/api/weather/`;
    let jwtToken = localStorage.getItem('token');
    console.log(":::jwtToken:::::"+jwtToken);
    const headers = {Authorization: `jwt ${jwtToken}`};
    return axios.get(url, {headers: headers});

  }

  authenticateLogin(credentials) {
    const url = `${API_URL}/auth/`;
    return axios.post(url, credentials);
  }
}
