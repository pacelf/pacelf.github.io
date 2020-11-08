const routes = [{
  path: '/',
  component: () =>
            import('layouts/MyLayout.vue'),
  children: [{ path: '',
    component: () =>
                import('pages/Index.vue') }]
},
{
  path: '/documents',
  component: () =>
            import('layouts/MyLayout.vue'),
  children: [
    { path: '/documents',
      component: () =>
                    import('pages/Documents.vue') }
  ]
},
{
  path: '/contact',
  component: () =>
            import('layouts/MyLayout.vue'),
  children: [
    { path: '/contact',
      component: () =>
                    import('pages/contact.vue') }
  ]
},
{
  path: '/eresearch',
  beforeEnter (to, from, next) {
    // Put the full page url including the protocol http(s) below
    window.location = 'https://www.jcu.edu.au/eresearch'
  }
}
]

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: () =>
            import('pages/Error404.vue')
  })
}

export default routes
