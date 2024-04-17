import axios from 'axios';
const API_URL ='http://127.0.0.1:8000';

export class APIService {
    constructor() {

    }
    //posts user credentials to db, hashes pw on frontend
    registerUser(credentials) {
        const url = `${API_URL}/user/register/customer`;
        return axios.post(url, credentials);
    }
    //user login, this sends user credentials to backend to get auth token and isAuthenticated flag
    //this is called after user signs in
    authenticateLogin(credentials) {
        const username = credentials.username
        console.log(credentials);
        const url = `${API_URL}/user/auth/${username}`;
        return axios.post(url);
    }
    //same as registering user but for employees, once employee admin status and permissions work this will allow
    //employees who are admins to make new employees
    //sends employee creds to backend db
    registerEmployee(credentials) {
        const url = `${API_URL}/user/register/employee`;
        return axios.post(url, credentials);
    }
    authenticateEmpLogin(credentials) {
        const username = credentials.username
        //make sure to take this out at some point....
        console.log(credentials);
        const url = `${API_URL}/user/auth/employee/${username}`;
        return axios.post(url);
    }
    //this gets customer account from db when given username, used for password verification
    findCustomerAccount(email) {
        const url = `${API_URL}/user/find-account/customer/${email}`;
        return axios.get(url);
    }
    //this gets employee account from db to authenticate employee acct on sign in, right now it doesn't work!
    findEmployeeAccount(email) {
        const url = `${API_URL}/user/find-account/employee/${email}`;
        return axios.get(url);
    }

    getDepartments() {
        const url = `${API_URL}/user/departments`;
        return axios.get(url)
    }
}

export class APIGetPlants {
    constructor() {

    }
    //returns list of plants to display in main menu
    getPlantList() {
        const url = `${API_URL}/product/home/`;
        return axios.get(url);
    }
    //returns list of plants depending on the category
    getPlantsByCategory(category_type) {
        const url = `${API_URL}/product`;
        return axios.get(url);
    }
    //returns plants by department
    getPlantByDepartment(department_id) {
        const url = `${API_URL}/product`;
        return axios.get(url);
    }
    //returns plants by color
    getPlantByColor(plant_color) {
        const url = `${API_URL}/product`;
        return axios.get(url);
    }
    //returns plant by specific category
    getPlantBySpecialCategory(plant_type, category) {
        const url = `${API_URL}/product`;
        return axios.get(url);
    }
    //returns specific plants
    getPlantByID(plant_id) {
        const url = `${API_URL}/product`;
        return axios.get(url);
    }
    //returns most popular searches
    getMostPopularSearches() {
        const url = `${API_URL}/product`;
        return axios.get(url);
    }
    //returns list of plants recently searched by specific user
    getRecentSearchesByUser(user_id) {
        const url = `${API_URL}/product`;
        return axios.get(url);
    }
}

export class APIQuestions {
    constructor() {
    }
    //posts question to db
    askQuestion(question) {
        const url = `${API_URL}/user`;
        return axios.get(url);
    }
    //returns all questions
    listQuestions() {
        const url = `${API_URL}/user`;
        return axios.get(url);
    }
    //returns questions asked by specific user
    findQuestionByUser(username) {
        const url = `${API_URL}/user`;
        return axios.get(url);
    }
    //returns questions asked about a specific plant
    findQuestionByPlant(plant_id) {
        const url = `${API_URL}/user`;
        return axios.get(url);
    }
    //returns questions asked on a specific date
    findQuestionByDate(date) {
        const url = `${API_URL}/user`;
        return axios.get(url);
    }
    //posts answer to question in db, arr is either going to be array of question id, emp number, answer, and date, or
    //seperate variables
    answerQuestion(arr) {
        const url = `${API_URL}/user`;
        return axios.get(url);
    }

}