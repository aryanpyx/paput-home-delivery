const scrape = require('website-scraper').default;

const options = {
  urls: ['https://www.paputmenorca.com/'],
  directory: './site',
  recursive: true,
  maxRecursiveDepth: 3,
  filenameGenerator: 'bySiteStructure',
  urlFilter: function(url) {
    return url.indexOf('https://www.paputmenorca.com') === 0;
  }
};

scrape(options).then((result) => {
  console.log('Site successfully downloaded!');
}).catch((err) => {
  console.error('An error occurred:', err);
});
