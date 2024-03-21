<template>
  <q-list separator dark>
    <q-item>
      <q-input dark
        v-model="searchText"
        :value="searchText"
        filled
        type="search"
        hint="Search"
        autogrow
        counter
        maxlength="30"
        @keyup.enter="updatedSearch"
      >
        <template v-slot:append>
          <q-btn
            round
            dense
            flat
            color="accent"
            icon="search"
            type="submit"
            @click="updatedSearch"
          />
        </template>
      </q-input>
    </q-item>
    <q-separator dark />
    <q-chip dark
      v-for="item in props.selectedFilters"
      :key="item"
      color="primary"
    >
      {{ item }}
    </q-chip>
    <q-separator />

    <DLFilterCategory
      v-for="[key, value] in Object.entries(props.filterCategories)"
      :categoryDetails="value"
      :key="key"
      @updatedFilter="
        (value1, value2) => {
          updatedFilter(value1, value2);
        }
      "
    />
  </q-list>
</template>

<script setup>
import { ref } from "vue";
import DLFilterCategory from "components/filter-category.vue";

const props = defineProps({
  filterCategories: Object,
  selectedFilters: Array,
});
const emit = defineEmits(["updatedFilter", "updatedSearch"]);

const searchText = ref("");

//console.log("filter-menu: selectedFilters(", props.selectedFilters, ")");

function updatedFilter(cat, option) {
  // DEBUG
/*   console.log(
    "filter-menu: updatedFilter: category is (",
    cat,
    ") option selected is (",
    option,
    ")"
  ); */
  emit("updatedFilter", cat, option);
}

function updatedSearch() {
  searchText.value = searchText.value.trim();
  // console.log("filter-menu: searchText(", searchText.value, ")"); // DEBUG
  emit("updatedSearch", searchText.value);
}
</script>
