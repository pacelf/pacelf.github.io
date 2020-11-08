<template>
  <q-layout
    view="lHh Lpr lFf"
    class="about"
  >
    <q-header elevated>
      <q-toolbar>
        <a href="/">
          <q-avatar to="/">
            <img src="~assets/pacelf_logo.png">
          </q-avatar>
        </a>

        <q-toolbar-title>
          PacELF Digital Library
        </q-toolbar-title>

        <!--
        notice shrink property since we are placing it
        as child of QToolbar
      -->
        <q-tabs
          shrink
          stretch
        >
          <q-route-tab to="/">About</q-route-tab>
          <q-route-tab to="/documents">Library</q-route-tab>
          <q-route-tab to="/contact">Contact</q-route-tab>

        </q-tabs>

      </q-toolbar>

    </q-header>
    <q-footer>
      <q-toolbar>
        <q-space />
        <q-tabs
          shrink
          stretch
        >
          <q-route-tab to="/eresearch">Made with &hearts; by JCU eResearch Centre</q-route-tab>

        </q-tabs>
      </q-toolbar>
    </q-footer>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { openURL } from 'quasar'

export default {
  name: 'MyLayout',
  data () {
    return {

    }
  },
  methods: {
    openURL
  }
}
</script>

<style>
</style>
