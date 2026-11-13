// Old Quasar bookmarks used hash routes and /documents/ PDF URLs.
(() => {
  const url = new URL(window.location.href);
  const routes = {
    '/': '/',
    '/library': '/library/',
    '/background': '/',
    '/contact-us': '/contact/'
  };
  const hashRoute = url.hash.startsWith('#/') ? url.hash.slice(1).split('?')[0].replace(/\/$/, '') || '/' : '';
  let destination;
  if (['/', '/index.html'].includes(url.pathname) && Object.hasOwn(routes, hashRoute)) {
    destination = routes[hashRoute];
  } else if (url.pathname === '/contact-us' || url.pathname === '/contact-us/') {
    destination = '/contact/';
  } else if (url.pathname === '/background' || url.pathname === '/background/') {
    destination = '/';
  } else if (url.pathname.startsWith('/documents/')) {
    destination = '/library' + url.pathname;
  }
  if (destination) window.location.replace(destination + url.search);
})();
