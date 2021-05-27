<template>
  <q-page
    padding
    class="flex flex-center justify-center"
  >
    <div class="q-pa-md row items-start q-gutter-md">
      <q-card class="my-card">
        <q-card-section>
          <!-- <div class="text-h1 text-center">
            <p>
              PacELF
            </p>
          </div> -->
          <div class="text-h3 text-center">
            <p>
              The PacELF Endgame Project and Digital Library
            </p>
          </div>
          <br>
          <div>

            <p>Our goal is to assist in achieving and documenting the elimination of lymphatic filariasis in the Pacific Region. We contribute to this by collating and synthesizing information in publications, and by making PacELF and other documents available. Much of our archive is not digitized but we will scan documents on request. Our address is pacelf@jcu.edu.au
            </p>
          </div>
        </q-card-section>

        <q-separator inset />

        <q-card-section>

          <h6 class="text-center"> Pacific Programme for the Elimination of Lymphatic Filariasis </h6>

          <p>
            PacELF worked within the framework of the <a href="https://www.who.int/lymphatic_filariasis/elimination-programme/en/"> WHO Global Programme to Eliminate Filariasis</a>, the <a href="https://www.who.int/about/regions/wpro/en/"> WHO Regional Office for the Western Pacific </a> and the <a href="https://www.who.int/westernpacific/about/how-we-work/pacific-support"> WHO Division of Pacific Technical Support</a>.
          </p>

          <p>
            PacELF, the first regional filariasis elimination programme, formed in 1999 as a network to coordinate the efforts in the twenty-two island countries and territories that are working to eliminate filariasis in the Pacific. The elimination strategy has
            two pillars: 1) annual mass drug administration (MDA) using diethylcarbamazine citrate (DEC), albendazole and/or ivermectin to stop transmission, and 2) clinical management of infections and support to minimize progression of morbidity and disability in
            those individuals that are already infected. PacELF countries classified as non endemic in 2000 were Guam, Nauru, Northern Mariana Islands, Pitcairn Island, Solomon Islands, and Tokelau. Of the remaining PacELF 16 endemic countries and territories, some
            have since achieved filariasis elimination, and others are moving closer to that goal. Progress by country with links to a bibliography of published literature from 1970 to mid 2017 is summarized in the following articles:
          </p>

          <ul>
            <li><a href="https://www.biomedcentral.com/collections/Filariasis">
                https://www.biomedcentral.com/collections/Filariasis</a>
            </li>
            <li>
              <a href="https://tropmedhealth.biomedcentral.com/articles/10.1186/s41182-017-0075-4"> https://tropmedhealth.biomedcentral.com/articles/10.1186/s41182-017-0075-4</a>
            </li>
          </ul>

          <p>
            Eight PacELF countries have achieved validation of elimination since the start of the programme: Vanuatu, Republic of the Marshall Islands, Niue, Cook Islands, Tonga, Palau, Wallis & Futuna and Kiribati. The remaining countries (American Samoa, Federated States
            of Micronesia, Fiji, French Polynesia, Papua New Guinea, Samoa, Tuvalu and New Caledonia) are still conducting surveillance or mass drug administration. Some Pacific countries recently introduced triple drug therapy by adding ivermectin
            to mass drug administration to accelerate their progress towards elimination.
          </p>

          <h6 class="text-center"> PacELF Digital Library </h6>

          <p>
            To assist with documentation and validation of elimination, and to provide a historical record, this project has collected all available published and unpublished documents about filariasis in the Pacific, with a focus on the PacELF period 1999 to present. This searchable archive consists of electronic and hard copy peer-reviewed papers, WHO documents, and programme reports, including the personal collection of Dr Kazuyo Ichimori. Some are freely available, while for some access must be requested. A collection of hard copy documents is housed at James Cook University's Townsville Campus in the <a href="https://research.jcu.edu.au/who-collaborating-centres/tropicalmedicine">JCU WHO Collaborating Centre for Vector-Borne and Neglected Tropical Diseases (WHO-181)</a> and may be accessed by request to pacelf@jcu.edu.au
          </p>

          <p>The development of this digital library is ongoing. We are very grateful to Dr Ichimori and James Cook University's WHOCC, eResearch Centre, and library for support, especially Kent Adams, Clair Meade, Alvaro Berg Soto, Peter Wood, Steve Vandervalk and many others. Thanks to our two interns, Sinead Rush and Jessica Scott and other volunteers for hours spent cataloguing.
          </p>

          <p>This work was supported by a grant from the United States Agency for International Development (USAID) through NTD SC, a program of the Task Force for Global Health, Inc. Its contents are solely the responsibility of the authors and do not necessarily represent the views of the supporting institutions.
          </p>

        </q-card-section>

        <q-separator inset />

        <q-card-section>
          <div class="text-h3 text-center">
            <p>Partners</p>
          </div>
        </q-card-section>
        <q-separator inset />

        <q-card-section class="logos">

          <q-img
            src="statics/icons/jcu_nag_who_logo.png"
            class="responsive"
            spinner-color="white"
            style="max-width: 1024px"
          />
          <q-separator inset />

          <q-img
            padding
            src="
            statics/icons/usaid_neg_logo.png"
            spinner-color="white"
            style="max-width: 1024px"
          />
          <q-separator inset />

        </q-card-section>

      </q-card>
    </div>
  </q-page>
</template>

<style>
</style>

<script>

export default {

  name: 'Index'
}
</script>
