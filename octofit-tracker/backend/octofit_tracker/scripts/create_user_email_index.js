// Run in mongosh: use octofit_db; db.users.createIndex({ "email": 1 }, { unique: true })
db = db.getSiblingDB('octofit_db');
db.users.createIndex({ "email": 1 }, { unique: true });