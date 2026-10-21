const Database = require('better-sqlite3');

const db = new Database('/data/korest.db');

const username = process.argv[2];
const password = process.argv[3];

if (!username || !password) {
  console.error('Usage: node change-korest-password.js USERNAME PASSWORD');
  process.exit(1);
}

const result = db
  .prepare('UPDATE users SET password_key = ? WHERE username = ?')
  .run(password, username);

console.log(`Rows changed: ${result.changes}`);

db.close();
