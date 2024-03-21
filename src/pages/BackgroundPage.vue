<template>
  <q-page>
    <div class="q-pa-md q-gutter-md rows">
      <q-card>
        <q-carousel animated v-model="slide" arrows infinite padding height="300px" object-fit="contain">
          <q-carousel-slide :name="1" img-src="~assets/1996-conference-bali_processed.jpg"
            class="column no-wrap flex-centre">
            <div class="q-mt-md text-center absolute-top slide-text">
              <div class="text-h5">International Conference on the Control of Lymphatic Filariasis - Bali 1996</div>
            </div>
          </q-carousel-slide>
          <q-carousel-slide :name="2" img-src="~assets/1996-conference-participants_scaled.jpg">
            <div class="q-mt-md text-center absolute-bottom slide-text">
              <div class="text-h5">International Conference Participants - Bali 1996</div>
            </div>
          </q-carousel-slide>
          <q-carousel-slide :name="3" img-src="~assets/Dr-Ichimori-receiving-prize_2000x900.jpg">
            <div class="q-mt-md text-center absolute-bottom slide-text">
              <div class="text-h5">Dr Ichimori receiving Yomiuri Intl Cooperation Prize</div>
            </div>
          </q-carousel-slide>
        </q-carousel>
      </q-card>
      <q-card>
        <q-card-section>
          <h5>Pacific Programme for the Elimination of Lymphatic Filariasis</h5>
          <p>PacELF worked within the framework of the
            <a href="https://www.who.int/health-topics/lymphatic-filariasis#tab=tab_1" target="_blank">
            Global Programme to Eliminate Filariasis</a>,
            the <a href="https://www.who.int/westernpacific" target="_blank">
              WHO Regional Office for the Western Pacific</a>
              and the <a href="https://www.who.int/westernpacific/about/how-we-work/pacific-support" target="_blank">
                Division of Pacific Technical Support</a>.
          </p>
          <p>
            PacELF, the first regional filariasis elimination programme,
            formed in 1999 as a network to coordinate the efforts in the twenty-two island countries
            and territories that are working to eliminate filariasis in the Pacific.
            The elimination strategy has two pillars:
          <ol>
            <li>
              Annual mass drug administration (MDA) using diethylcarbamazine citrate (DEC),
              albendazole and/or ivermectin to stop transmission, and
            </li>
            <li>
              Clinical management of infections and support to minimize progression of
              morbidity and disability in those individuals that are already infected.

            </li>
          </ol>
          </p>
          <p>
            PacELF countries classified as non endemic in 2000 were Guam, Nauru, Northern Mariana Islands,
            Pitcairn Island, Solomon Islands, and Tokelau.
            Of the remaining PacELF 16 endemic countries and territories, some have since achieved
            filariasis elimination, and others are moving closer to that goal.

          </p>
          As of 2024, eight PacELF countries have achieved validation of elimination since the start of the programme:
          <ul>
            <li>Vanuatu,</li>
            <li>Republic of the Marshall Islands,</li>
            <li>Niue,</li>
            <li>Cook Islands,</li>
            <li>Tonga,</li>
            <li>Palau,</li>
            <li>Wallis & Futuna</li>
            <li>Kiribati.</li>
          </ul>

          The remaining countries are still conducting surveillance or mass drug
          administration:
          <ul>
            <li>American Samoa,</li>
            <li>Federated States of Micronesia,</li>
            <li>Fiji,</li>
            <li>French Polynesia,</li>
            <li>Papua New Guinea,</li>
            <li>Samoa,</li>
            <li>Tuvalu,</li>
            <li>New Caledonia.</li>
          </ul>

          <p>Some Pacific countries recently introduced triple drug therapy by adding ivermectin
            to mass drug administration to accelerate their progress towards elimination.
          </p>
        </q-card-section>
      </q-card>
      <q-card>
        <q-card-section>
          <h6>PacELF Publications</h6>
          Progress by country with links to a bibliography of published literature from 1970 to mid 2017
            is summarized in the following articles:
          <ul>
            <li><a href="https://www.biomedcentral.com/collections/Filariasis" target="_blank">
                https://www.biomedcentral.com/collections/Filariasis</a>
            </li>
            <li><a href="https://tropmedhealth.biomedcentral.com/articles/10.1186/s41182-017-0075-4" target="_blank">
                https://tropmedhealth.biomedcentral.com/articles/10.1186/s41182-017-0075-4</a>
            </li>

          </ul>

        </q-card-section>
      </q-card>
      <q-card>
        <q-card-section class="q-mx-md row">
          <q-img src="~assets/PacELF-books_white-bkgnd.jpg" alt="PacELF book covers" fit="contain"
            max-width="500px" class="col-12 col-sm-4" />
          <div class="q-ma-md col-12 col-sm">
            <h6>PacELF books</h6>
            <p>
              We published a book in 2023: <em>“The PacELF collection: PacELF scientific papers and Dr Kazuyo
                Ichimori’s contribution in commemoration of the Yomiuri International Cooperation Prize 2022”</em>
              which contains an updated bibliography of lymphatic filariasis in the Pacific, 1999-2020.
              It is available as hardcopy on request.
            </p>
          </div>
        </q-card-section>
      </q-card>
    </div>
  </q-page>
</template>
<style lang="scss">
.slide-text {
  color: #273256;
  font-weight: 900;
  background-color: #ffffffbb;
}
</style>
<script setup>
import { ref } from 'vue'

let slide = ref(1)

</script>
