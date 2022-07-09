# PacELF Digital Library

A static web site built using [Quasar
JS](https://quasar.dev/quasar-cli/installation) framework and ItemsJS to
index, search and download documents.

A static site port of a MediaFlux portal built by the JCU eResearch
Centre.

## Software Requirements

- [NodeJS v14.18.0](https://nodejs.org/download/release/v14.18.0/)
- [Yarn version 1.22.19](https://classic.yarnpkg.com/en/docs/install#mac-stable)
- [Python 3.10.5](https://www.python.org/downloads/)
- This repository, pacelf/pacelf.github.io.git

Note: This website has only been built on a MacOS system.

![Diagram of the update process](PacELF-update-overview.png)

## Step 1
Get access to the documents that will be going into the library and the spreadsheet that indexes the documents and contains metadata about them.
For an example spreadsheet see the files in PacELF_Phase6/rawdata

## Step 2
Clone the main branch of this repository

## Step 3
Setup a Python virtual environment, this is needed for 3A and 3B.

```shell
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Step 3A - Create pacelf-index.csv file and download Open Access files

The PacELF team will send you a spreadsheet and share a folder with you.
The folder contains various folders and extraneous files. This is why we 
created the `get-pacelf-files.py` script.

The only files that we need to copy are the ones in the spreadsheet that have open access rights. So there will be less files copied than there are rows in the spreadsheet.

1. Save the spreadsheet as a UTF-8 CSV file, named pacelf-index.csv, at the top of the repository.
2. Delete the files in the `src/statics/data` folder.
3. Run the script, `get-pacelf-files.py`. It may take awhile the first time as you will be copying a lot of files. Redirect the output to a log file so that you can review it.
   ```shell
   python get-pacelf-files.py > get-files.log
   ```
4. Review the logfile, `get-files.log`
5. Work with the PacELF team to resolve any errors in the spreadsheet.
   - sometimes the filename has been entered incorrectly in the spreadsheet
   - it may be OK for a file with Open access rights to have no filename, see the behaviour of the next script.
6. Repeat until there are no more warnings that need to be dealt with.

## Step 3B - Generate the pacelf-index.json file

This script will run through the `pacelf-index.csv` file and if the 
access rights are:
- Contact PacELF at JCU
   - creates a file that contains instructions to contact PacELF to gain access to the document.
   - sets the download_url to the appropriate path
- Open
   - if the filename is empty is will create an access notification file (as per Contact PacELF at JCU)
   - if the file exists, it will set the download_url to the appropriate path.
- Open via Publisher
   - sets the download_url to the value in the publisher's url field.

Meanwhile it is building the `pacelf-index.json` file that the website needs to provide search functionality. This is saved into the correct place in the folder structure to work with the build.

### Creating the JSON file

1. Run the script `csv-to-json.py`. Redirect the output to a log file so that you can review the warnings.
   ```shell
   python csv-to-json.py > csv-to-json.log
   ```
2. Review the logfile, `csv-to-json.log`
3. Work with the PacELF team to resolve any errors in the spreadsheet.
4. Repeat until there are no more warnings that need to be dealt with.

Note: This script assumes that the open access files are already in the `src/statics/data` folder.

## Step 3C - Test the website in dev mode

### First time

The first time you want to build the website, run 
```shell
yarn install
```
Note: After the yarn install, you can run lint over the code with `yarn lint`

### Running the website in dev mode

To open up a browser window with the PacELF Digital Library website running in it:
```shell
yarn dev
```

## Step 3D - Build the website

To build the app for deployment, run the following:

```shell
yarn build
```

### To test the build

```shell
yarn start
```

Open <http://localhost:4000/> in your browser.


## Step 4 Publish/Deploy
Assumes that you have built the website in the main branch of the repository.

1. Clone the gh-pages branch of the repository
   ```shell
   git clone --branch gh-pages --single-branch git@github.com:pacelf/pacelf.github.io.git gh-pages
   ```
2. Delete the contents of the gh-pages repository (except the .git, .gitignore, etc)
2. Copy the contents from `dist/pwa/` in the **main repository** thus replacing the entire contents of the `gh-pages` branch.
3. Stage the changes, the -A option says to include adds, modifications and deletes
   ```shell
   git add -A
   ```
   Commit and push the staged changes to GitHub
   ```shell
   git commit -m "<commit message text>"
   git push
   ```
3. GitHub Pages are already configured to serve the content of `gh-pages` branch at `https://pacelf.github.io`. See the settings at https://github.com/pacelf/pacelf.github.io/settings/pages.
4. Look at https://github.com/pacelf/pacelf.github.io/actions to see how the deployment is progressing.
5. Test the website
6. If all is well, tag the changes:
   ```shell
   git tag -a phase<X>-gh-pages -m "website for phase <X>"
   git push origin phase<X>-gh-pages
   ```
7. Add, commit and push the changes to the main branch.














## Customise the configuration

See [Configuring quasar.conf.js](https://quasar.dev/quasar-cli/quasar-conf-js).
