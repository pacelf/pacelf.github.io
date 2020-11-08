# TODO

- [x] fix up the duplicates in the side menus by crappy spelling somewhere?
  - [ ] extra spaces in the data entry
- [ ] figure out if the phase4 data doesn't include any phase3 and have to support both
- [x] extract DOI from original data to include
- [x] change .txt text
- [ ] refactor everything into functions for readability - its a mess
- [ ] add conditional rendering or something
  - [ ] https://vuejs.org/v2/guide/conditional.html
- [x] ask for text copy of the content on the About page

## Done

- [x] remove empty fields from pacelf.json somehow to prevent search breaks
  - [ ] turns out this was due to how the items were being indexed by VueJS
    - [ ] https://medium.com/@chiatsai/vue-js-common-issue-duplicate-keys-stops-components-rendering-df415f31838e
    - [ ] so instead we index by the PacELF ID - which SHOULD BE unique!
    - [ ] see `Documents.vue` L 20
      - [ ]     ````<q-item
              v-for="item of items"
              :key="item.PacELF_ID"
              >

````
