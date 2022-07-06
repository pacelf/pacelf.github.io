<template>
  <q-page padding>
    <q-card class="my-card">
      <div class="row">
        <div class="col-3">
          <items-js-facets
            :rows="jsonData"
            :configuration="configuration"
            @searchResultUpdated="searchResultUpdated"
          >
          </items-js-facets>

        </div>

        <!-- <div class="col-1"></div> -->
        <div class="col-9">
          <q-list
            highlight
            bordered
            separator
          >
            <q-item
              v-for="item of items"
              :key="item.ID"
            >

              <q-item-section avatar>
                <a
                  :href="item.download_url"
                  target="_blank"
                  rel="nofollow"
                  aria-label="Link to selected document"
                ><img
                    alt="HTML Placeholder Image"
                    style="width: 100px;"
                    src="~assets/document_placeholder.png"
                  /></a>
                <p class="caption"></p>
                <a
                  :href="item.download_url"
                  target="_blank"
                  rel="nofollow"
                  aria-label="Link to get selected document"
                  download
                >
                  <q-btn
                    split
                    color="black"
                    outline
                    label=" ⬇ Get Link"
                    type="a"
                  >
                  </q-btn>
                </a>

              </q-item-section>
              <q-item-section>
                <a
                  :href="item.download_url"
                  target="_blank"
                  aria-label="Link to download selected document"
                >
                  <h6>{{item.Title}}</h6>

                </a>
                <q-item-section>
                  <p>
                    {{item.Description}}
                  </p>
                </q-item-section>

                <q-item-section>
                  <br />
                  <dl class="horizontal">
                    <dt>PacELF ID</dt>
                    <dd>
                      {{item.ID}}
                    </dd>
                    <dt>Access Rights</dt>
                    <dd>
                      {{item.Access_Rights}}
                    </dd>
                    <dt>Category</dt>
                    <dd>
                      {{item.Category}}
                    </dd>
                    <dt>Journal</dt>
                    <dd>
                      <em>{{item.Journal}}</em>
                    </dd>
                    <dt>Authors</dt>
                    <dd>
                      {{item.Authors}}
                    </dd>

                    <dt>Year of Publication</dt>
                    <dd>
                      {{item.Year}}
                    </dd>
                    <dt>Work Location</dt>
                    <dd>
                      {{item.Work_Location}}
                    </dd>

                    <dt>Copy Location</dt>
                    <dd>
                      {{item.HardcopyLocation2020}}
                    </dd>

                    <dt>Volume/Issue</dt>
                    <dd>
                      {{item.Volume_Issue}}
                    </dd>

                    <dt>Pages</dt>
                    <dd>
                      {{item.Pages}}
                    </dd>
                    <dt>Language</dt>
                    <dd>
                      {{item.Language}}
                    </dd>
                    <dt>Publisher</dt>
                    <dd>
                      {{item.Publisher}}
                    </dd>
                    <dt>Type</dt>
                    <dd>
                      {{item.Type}}
                    </dd>

                    <!-- Other terms and descriptions -->
                  </dl>

                  <!--                <q-chip small tag v-for="tag in item.goals_types" :key="tag.key">{{ tag }}</q-chip>-->

                </q-item-section>

                <!--                <q-item-label><a :href="item.download_url" target="_blank"><q-btn type="a" icon="remove_red_eye" class="primary" label="View"></q-btn></a>-->
                <!--                <a :href="item.download_url" download><q-btn type="a" icon="get_app" class="primary" label="Download"></q-btn></a></q-item-label>-->

              </q-item-section>

            </q-item>
          </q-list>
        </div>
      </div>
    </q-card>
  </q-page>
</template>
<style>
</style>
<script>
import rawJson from './pacelf-index.json'
import ItemsJsFacets from './ItemsJsFacets.vue'

export default {
  components: { ItemsJsFacets },
  created () {
    this.jsonData = rawJson
    // this.jsonData.forEach(e => {
    //   e.year = [e.year.toString()]
    // })
  },
  data () {
    var configuration = {
      sortings: {
        name_asc: {
          field: ['Title'],
          order: ['asc']
        }
      },
      // what fields the search indexes
      searchableFields: [
        'Title',
        'ID',
        'Type',
        'Authors',
        'Year',
        'Journal',
        'Work_Location',
        'HardcopyLocation2020',
        'Category'

      ],
      // what facets are used on the side
      aggregations: {
        Access_Rights: { title: 'Access Rights', size: 10 },
        Category: { title: 'Category', size: 30 },
        Journal: { title: 'Journal', size: 30 },
        Year: { title: 'Year of Publication', size: 30 },
        Work_Location: { title: 'Work Location', size: 50 },
        HardcopyLocation2020: { title: 'Copy Location', size: 10 },
        Language: { title: 'Language', size: 10 },
        Publisher: { title: 'Publisher', size: 50 },
        Type: { title: 'Type', size: 10 }

      }
    }
    return {
      jsonData: [],
      configuration,
      items: []
    }
  },
  methods: {
    searchResultUpdated (d) {
      this.items = d
    }
  }
}
</script>
