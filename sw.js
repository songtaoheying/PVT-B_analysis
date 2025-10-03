// sw.js 内容
const CACHE_NAME = 'pvt-b-viewer-cache-v1'; 
// 需要缓存的文件列表。请确保 'chart.umd.js' 的路径与您本地存放的路径一致！
const urlsToCache = [
  'PVT-B-Show.html', // 您的 HTML 文件名
  './chart.umd.js',  // 本地化的 Chart.js 文件
  // 也可以添加其他未来可能有的 CSS 文件等
];

// 监听安装事件，将文件添加到缓存
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

// 监听获取（fetch）事件，拦截请求并返回缓存中的资源
self.addEventListener('fetch', event => {
  // 仅处理同源请求
  if (event.request.url.startsWith(self.location.origin)) {
    event.respondWith(
      // 尝试从缓存中匹配请求
      caches.match(event.request)
        .then(response => {
          // 如果缓存中有，则直接返回
          if (response) {
            return response;
          }
          // 如果缓存中没有，则进行网络请求
          return fetch(event.request);
        })
    );
  } else {
    // 对于跨域资源（例如 CDN，虽然我们已经本地化了），直接走网络
    event.respondWith(fetch(event.request));
  }
});

// 监听激活事件，清理旧的缓存
self.addEventListener('activate', event => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            return caches.delete(cacheName); // 删除旧版本缓存
          }
        })
      );
    })
  );
});