<template>
  <!-- <p>{{ categoryDetails }}</p> -->
  <q-expansion-item expand-separator :label="categoryDetails.title">
    <q-card-section>
      <!-- <p>{{ categoryDetails.buckets }}</p> -->
      <!-- DEBUG -->
      <q-option-group
        v-model="group"
        :name="categoryDetails.title"
        :options="getOptions(categoryDetails.buckets)"
        color="primary"
        type="toggle"
        @update:modelValue="
          (newValue) => {
            filterUpdated(categoryDetails.name, newValue);
          }
        "
      />
    </q-card-section>
  </q-expansion-item>
</template>
<script setup>
import { ref } from "vue";

defineProps({ categoryDetails: Object });
const emit = defineEmits(["updatedFilter"]);
const group = ref([]);

function getOptions(options) {
  let optionsList = [];
  for (let option of options) {
    optionsList.push({
      label: option.key + " (" + option.doc_count + ")",
      value: option.key,
    });
  }

  return optionsList;
}

function filterUpdated(filterCategory, selectedFilterOption) {
  // DEBUG
/*   console.log(
    "filter-category: Filter updated: filterCategory (",
    filterCategory,
    " newValue is(",
    selectedFilterOption,
    ")"
  );
 */
  emit("updatedFilter", filterCategory, selectedFilterOption);
}
</script>
