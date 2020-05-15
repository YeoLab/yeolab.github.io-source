yeolab.github.io-source
=======================

[![Build Status](https://travis-ci.org/YeoLab/yeolab.github.io-source.svg)](https://travis-ci.org/YeoLab/yeolab.github.io-source)

Markdown and HTML source code for the static website http://yeolab.github.io/ built via Pelican and Fabric on Travis-CI.


To set up pushes from Travis-CI, I had to encrypt a Github token in my `.travis.yml` file. First, you will need a "personal access token", which you can generate from
github by going to the settings of your account (where you would change your password),
and creating a new token with the name "Yeolab Website" (or whatever you want to call it). It will look like `1234567890qwertyuiopasdfghjklzxcvbnm`. Make sure to copy this to your clipboard because for security reasons, you'll only see it once. Note that you do not want to save this to a public place because anyone with this key can make changes to your repositories, including malicious ones.

Then, run this command, but replace the "Olga Botvinnik" and olga.botvinnik@gmail.com with your own name and email.

```
travis encrypt --add -r gbic-ucsd/gbic-ucsd.github.io-source GIT_NAME="Olga Botvinnik" GIT_EMAIL=olga.botvinnik@gmail.com GH_TOKEN=<secret personal access token from github.com>
```

## How to install, build, and view the website

### Important notes

This website relies on **both**

* The [`people`](https://github.com/olgabot/people) extension, which populates a dictionary of "persons" (i.e. individual people), their position in lab, and their status, and assigns it to the "people"
* The [`twenty-pelican-html5up`](https://github.com/YeoLab/twenty-pelican-html5up/) theme, which specifies how to make both a "person" and "people" page.

Both of these extensions are required for the website to build.

### Install requirements

Install the required python packages on the command line with,

```
pip install -r requirements.txt
```

### Build the website
Now that you have everything installed, build the website with

```
fab build
```

`fab` stands for `fabric` which is the system we use to "weave" together all of the components of the website.

To remove the built folder (say you want to start fresh), do

```
fab build
```

### Viewing the built website

To see what the website would look like online, do

```
fab serve &
```

Which should result in the output,

```
[localhost] local: cd output && python -m SimpleHTTPServer
Serving HTTP on 0.0.0.0 port 8000 ...
```

Now, open your web browser and go to this magic website: http://localhost:8000 This is a local server on your computer only (not a public website) which allows the HTML pages to talk to each other and load data. Every time you make a change and want to see it on the built website, refresh the page.

The "`&`" (ampersand) is the symbol for "do this operation in the background," which is helpful for when you edit the website and re-build it multiple times. *You only need to serve once* - you don't need to re-serve after you build. Just refresh the page.

## Viewing the website online

To see if the online version successfully built, go to [Travis-CI](https://travis-ci.org/YeoLab/yeolab.github.io-source) and see if there's an error (there's also a badge in this readme). If it was successful, then check out the [live site](http://yeolab.github.io/people/)!

## Editing the website

### Adding people

To add a new person to the people page, copy an existing person's markdown file (in `content/pages/people/*.md`) (it's easiest if you pick someone from the same position, e.g. an existing grad student for a new grad student), and copy their information in.

The top of the `.md` (markdown) file is a bunch of metadata. The critical stuff that is required is (HTML comments on what the thing is are inline) below. Note that capitalization matters differently whether something is before or after the colon: `before_colon: after_colon`:

* `before_colon`: Capitalization doesn't matter. Could be `title` or `Title`
* `after_colon`: Capitalization ***does*** matter. Must be `Graduate Student`.

```markdown
<!-- Name of the person -->
Title: Olga Botvinnik  

<!-- A date is required to build - use approximate date started in the lab.
Only the year is used for the alumni page -->
Date: 2013-06-01

<!-- Position of the person, one of "Principal Investigator", "Post-Doctoral Fellow",
"Graduate Student" (represents phD student group), "Visiting Scientists,"Visiting Graduate Student","Masters Student","Visiting Graduate Students","Staff", "Undergraduate Student", "High School Student"-->
Position: Graduate Student

<!-- A suffix to add after the position. Mostly relevant for Staff Research
 Associates, so here for them you would put "Research Associate II" or
  "Bioinformatics Analyst I", whichever position they are-->
Position_suffix:

<!-- Department the person is tied to. If unknown, leave blank -->
Affiliation: Bioinformatics and Systems Biology

<!-- UCSD-related email to contact the person. gmail and hotmail not
okay here -->
Email: obotvinn@ucsd.edu

<!-- Name of the fellowship, if applicable. If none, leave blank.
Leave out the word "Fellowship" -->
Fellowship: NDSEG

<!-- Location of the person's square headshot, relative to the folder "content/" If someone doesn't have a photo, put "/yeolab_favicon.svg"-->
Headshot: /images/people/botvinnik_olga_headshot.jpeg

<!-- Whether they are currently in the lab or have moved on -->
Alumni_or_current: Current

<!-- don't touch this! if it doesn't say "person" here then
they don't get a page :( -->
Template: person
```

#### Notes about photos

The headshot provided must be:

* `.jpeg` or `.jpg` format, because `png`s get corrupted for some reason in building the website
* **exactly square**, because if not square, your circle for your photo will be an oval
* exactly 500x500 pixels, which will ensure maximum legibility on both high and low resolution screens.


### Moving somebody to the Alumni page

When moving somebody to the alumni page, you will need to change and add the following:

* Change `Alumni_or_current: Current` to `Alumni_or_current: Alumni`
* Add `Current_position`, where they are working now to put in their profile
* Add `End_date` (approximate, only year is used), to show their total years in lab

For example, here is the metadata for Melissa Wilbert:

```
Title: Melissa Wilbert
Date: 2008-06-01
Position: Graduate Student
Position_suffix: (Ph.D.)
Affiliation: Biomedical Sciences Program
Email: shsathe@ucsd.edu
Fellowship:
Headshot: /images/people/botvinnik_olga_headshot.jpeg
Template: person
Alumni_or_current: Alumni
Current_position: Novartis, Boston, MA
End_date: 2014-11-01
```

## Building and viewing the website

To test the built website on your computer, go to the `yeolab.github.io-source` directory and type:

```
fab build
fab serve &
```

Go to http://localhost:8000 to see the built website.

The `&` is to run the task in the background so you can edit the page and
hit "refresh" when you rebuild, without having to re-serve.

### Debugging

If you get the error, `CRITICAL: UndefinedError: 'page' is undefined`, double check that you have put individual "person" pages **only** in `content/pages/people`. If it's in `content/`  but not the subdirectory `people`, then Pelican will try to use the Article template (Article = blog post) instead of the Page template (from which the "Person" template is derived), leading to `page` being undefined.

### Organization

#### `content` folder

This folder contains most of the things that will be edited.

##### `pages` folder

This contains pages that you can put content in to. They are required to have a header like this:

```
Title: Funding
Date: 2015-09-21
icon: mdi mdi-currency-usd
```

* `Title`: This is the name of the folder that will be created for this content. In this example, this page is located at `yeolab.github.io/funding/`, **not** the name of the file (e.g. `funding.md`). You would link to it from another page with `[here's where you can find out more about funding](/funding/)`. So if in the file `funding.md`, your title was "Moolah" then the website builder would create `yeolab.github.io/moohah/` Moral of the story is, if your link isn't working, check the title!
* `Date`: This is required for legacy reasons because the system we're using is actually a blogging system. I use the date the file was created
* `icon`: This puts an icon at the top of the page. You can choose from any [Material Design](https://materialdesignicons.com/) icon. Notice that you have to say `mdi mdi-iconname` to specify the icon. This is because CSS is stupid. Say you wanted to use the `paperclip` icon, then you would put `mdi mdi-paperclip`.

#### `people` folder

This contains individual pages for each person. This is explained in depth in the [Adding People](#adding-people) section.

#### `extras` folder

This folder contains icons

#### `people` folder

This is a plugin written to auto-generate a people/team page based on the files in `content/pages/people`.


#### `twenty-pelican-html5up` folder

The folder `twenty-pelican-html5up` contains the templates for all pages. In the `twenty-pelican-html5up/templates` folder, these are the key files:

* `index.html`: Raw content for the landing page. All HTML, no markdown
* `person.html`: Template for an individual person's page (e.g. what Gene's page will link to)
* `people.html`: Template for the people/team page
* `page.html`: Template for all non-people pages, e.g. for funding, research, software
