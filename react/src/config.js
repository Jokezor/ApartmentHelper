let apiUrl, appUrl;

if (process.env.REACT_APP_STAGE == 'dev') {
    apiUrl='http://localhost:8000';
    appUrl='http://localhost:3000';
}

if (process.env.REACT_APP_STAGE == 'prod') {
    apiUrl = 'https://api.apartmenthelper.com';
    appUrl = 'https://app.apartmenthelper.com';
}

export {
    apiUrl,
    appUrl
}