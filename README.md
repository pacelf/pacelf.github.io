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

To set up the project and install its dependencies, run the following commands:

```shell
git clone git@github.com:pacelf/pacelf.github.io.git
cd pacelf.github.io
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

The built application files are written to the `dist/pwa/` directory.

To view this build, run:

```shell
yarn start
```

Then, you can open <http://localhost:4000/> in your browser.


## Deployment

Once you are happy with local version:

1. Run `yarn build`.

2. Copy the contents `dist/pwa/` and replace the entire contents of the
`gh-pages` branch.

2. Commit and push to the GitHub repository https://github.com/pacelf/pacelf.github.io.

3. GitHub Pages are already configured to serve the content of `gh-pages` branch at `https://pacelf.github.io`. See the settings at https://github.com/pacelf/pacelf.github.io/settings/pages.


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
