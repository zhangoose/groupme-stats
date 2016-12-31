Groupme Stats
====

![travis](https://travis-ci.org/zhangoose/groupme-stats.svg?branch=master)

[See this live here!](https://gm-stats.us)

See your GroupMe groups' posting stats through specific dates.

![demo](https://d17oy1vhnax1f7.cloudfront.net/items/0h212X3u20100I0r0H2S/Screen%20Recording%202016-12-30%20at%2007.07%20PM.gif?v=04ed8e1a)

**Still a WIP**

### Local Setup

This repo is divided into two parts: `frontend` and `backend`.

Begin by setting up the backend:

```
cd backend
pip install -r requirements.txt
```

Then the frontend:

```
cd frontend
bower install
```

You must also have a `config.json` file somewhere in `frontend/`.

```
{
    "API_URL": "http://localhost:5000", // the URL for the backend API
    "CLIENT_ID": ..... //groupme app client ID
}
```

(Note that after updating your config.json, you may need to do a `gulp config` to update the config/config.js)

### Running Locally

Backend:

```
cd backend
python app.py
```

Frontend:

```
cd frontend
node index.js
```

Go to `localhost:3000`! 

### Tests

API tests are powered by py.test.

```
cd backend
pytest tests
```
