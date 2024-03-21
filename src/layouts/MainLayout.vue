<template>
  <q-layout view="lHr LpR lFr" class="textured-bg">
    <q-drawer show-if-above width="300" breakpoint="1440" class="bg-secondary text-white" />
    <q-drawer side="right" show-if-above breakpoint="1440" class="bg-secondary text-white" />
    <q-header>
      <div class="q-pa-md">
        <q-toolbar class="bg-primary text-white glossy">
          <q-avatar>
            <img src="~assets/app-logo-128x128.png">
          </q-avatar>
          <q-toolbar-title>
            PacELF Digital Library
          </q-toolbar-title>
          <q-tabs vertical shrink outside-arrows align="right">
            <q-route-tab to="/" label="About" />
            <q-route-tab to="/background" label="Background" />
            <q-route-tab to="/library" label="Library" />
            <q-route-tab to="/contact-us" label="Contact Us" />
          </q-tabs>
        </q-toolbar>
      </div>
    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer elevated>
      <q-toolbar>
        <q-toolbar-title>
          <div class="text-right text-subtitle1">
            Made with &hearts; by JCU eResearch
          </div>
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<style lang="scss"></style>
