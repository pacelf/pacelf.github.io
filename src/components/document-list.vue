<template>
  <div class="q-pa-md">
    <q-card flat>
      <p>
        {{ docs.length }} document{{ docs.length > 1 ? "s displayed" : " displayed" }}  (we don't display > 200)
      </p>
    </q-card>

    <q-list dense bordered separator>
      <DLDocumentCard v-for="doc in docs" :docdata="doc" :key="doc.id" />
    </q-list>
  </div>
</template>

<style></style>

<script setup>
import DLDocumentCard from "components/document-card.vue";

defineProps({
  docs: Array,
});
</script>
