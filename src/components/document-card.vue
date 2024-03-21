<template>
  <!-- DEBUG-->
  <!-- <p>{{ docdata }}</p> -->
  <q-expansion-item expand-separator :label="docdata.Title" :icon="docdata.Icon" header-class="bg-accent">
    <q-card>
      <q-card-section class="q-py-sm">
        <div v-if="docdata.URL === ''" class="row justify-start">
          <div class="col-1">
            <q-btn round color="primary" :icon="docdata.Icon" :href="generateEmailHRef(docdata.ID)" />
          </div>
          <div class="col q-pl-md">
              Please email pacelf@jcu.edu.au to request this item. Quote ID number {{ docdata.ID }}.
              We will do our best to make it available.
          </div>
        </div>
        <div v-else class="row">
          <div class="col-1">
            <q-btn round color="primary" :icon="docdata.Icon" :href="docdata.URL" target="_blank" />
          </div>
          <div class="col q-pl-md">
              <em>Click the button to access the document.</em>
          </div>
        </div>
      </q-card-section>

      <q-card-section>
        <q-item-label v-for="[key, value] in getDocDetails(docdata)" :label="key" :value="value" :key="key">
          <b>{{ key }}:</b> {{ value }}
        </q-item-label>
      </q-card-section>
    </q-card>
  </q-expansion-item>
</template>

<script setup>
defineProps({ docdata: Object });

function getDocDetails(obj) {
  let details = Object.entries(obj);
  return details;
}

function generateEmailHRef(docid) {
  let emailHRef = "mailto:pacelf@jcu.edu.au?subject=PacELF website request for document#" +
    docid + "&body=I would like to access a copy of document " + docid;

  return emailHRef;
}
</script>
