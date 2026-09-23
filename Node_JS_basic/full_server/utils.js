import fs from 'fs';

const readDatabase = (path) => new Promise((resolve, reject) => {
  fs.readFile(path, 'utf-8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const fields = {};
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const [, ...rows] = lines; // skip the header row

    rows.forEach((row) => {
      const [firstname, , , field] = row.split(',');
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    });

    resolve(fields);
  });
});

export default readDatabase;
