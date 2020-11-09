# PacELF Digital Library

A static web site built using [Quasar
JS](https://quasar.dev/quasar-cli/installation) framework and ItemsJS to
index, search and download documents.

A static site port of a MediaFlux portal built by the JCU eResearch
Centre.

## Setup

### Requirements

- [NodeJS LTS](https://nodejs.org/en/)
- [Yarn](https://classic.yarnpkg.com/en/docs/install#mac-stable)
- [Python 3.7](https://www.python.org/downloads/)

### Installation

To install each of the system-level requirements on a macOS platform, you
require the [Homebrew](https://brew.sh/) package manager. Once you have `brew`
installed, run the following command:

```shell
brew install node yarn python3
```

To set up the project and its dependencies, run the following commands:

```shell
git clone git@github.com:jcu-eresearch/marine-conservation-planning-database.git
cd marine-conservation-planning-database
yarn
```

### Development mode

To start the app in development mode (hot-code reloading, error reporting,
etc), run the following:

```shell
yarn dev
```

### Lint the JavaScript source

```shell
yarn lint
```

### Production

To build the app for production, run the following:

```shell
yarn build
```

Check the resulting `dist/pwa` directory for the built application. To test
serving the build as if from a webserver, run the following:

```shell
yarn start
```

Then, you can open <http://localhost:4000/> in your browser and view and test
the built site.

### Netlify

Currently nothing is setup automatically.

Deploys are done using `netlify-cli` and `netlify deploy --dir=dist/pwa/ --prod`.

TODO: Setup GitHub and Netlify
Once you are happy with the results, you can then commit your changes to the
`master` branch and push to GitHub. Netlify will then build and deploy the
site at its end automatically.

## Deployment

The project is currently hooked up to eResearch's Netlify account from the
GitHub repository.

Netlify is configured to build and deploy commits automatically pushed to the
`master` branch.

Any other static site hosting (such as GitHub Pages) can also be used
to host the output folder from the build step (`dist/pwa`).


### Existing data

`PacELF_Phase4/Phase4.xlsx` contains the catalogue data and `src/statics/data/` contains the PDFs, supplied by the PacELF project maintainers.

## Adding new data

TODO: Ask how many more phases and decide who to document this for.

Basically the PacELF Excel file is converted to CSV and then parsed by `csv-to-json.py` to generate `/src/pages/pacelfv4.json`

### Producing JSON data file in detail

Once the raw data is correctly located as above, install the Python dependencies to convert from CSV to JSON:

```shell
pip3 install -r requirements.txt
```

and run the script:

```shell
python ./csv-to-json.py
```

This will write `pacelfv4.json` to `src/pages/`.

The website uses the `src/pages/pacelfv4.json` file as a search index of the documents.

Now start the Quasar app in development mode (`yarn dev`, as
mentioned above) and test if the new data is searchable.

### Customise the configuration

See [Configuring quasar.conf.js](https://quasar.dev/quasar-cli/quasar-conf-js).
