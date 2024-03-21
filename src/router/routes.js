const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      { path: "", component: () => import("pages/IndexPage.vue") },
      { path: "/library", component: () => import("pages/LibraryPage.vue") },
      { path: "/background", component: () => import("pages/BackgroundPage.vue") },
      { path: "/contact-us", component: () => import("src/pages/Contact-us.vue") },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
