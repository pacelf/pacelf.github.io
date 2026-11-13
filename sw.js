// Retire the previous Quasar offline app. Keep this at its original URL.
// No fetch handler: requests use the network instead of the old app cache.
self.addEventListener('install', event => {
  event.waitUntil(self.skipWaiting());
});
self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    await self.clients.claim();
    const names = await caches.keys();
    await Promise.all(names.filter(name => name.startsWith('pacelf-dl-'))
      .map(name => caches.delete(name)));
    await self.registration.unregister();
    const windows = await self.clients.matchAll({type: 'window'});
    await Promise.all(windows.map(client => {
      const url = new URL(client.url);
      if (['/', '/index.html', '/library', '/library/', '/background',
           '/contact-us'].includes(url.pathname)) {
        return client.navigate(client.url);
      }
    }));
  })());
});
