# Redox Parser Library Generator for Python
> [!NOTE]  
> This library is not accepting contributions and is in maintenance mode (only security updates). We recommend forking this code or using another library if you require more active development.

This utility *generates* a library for producing/ingesting JSON data that conforms
to the [Redox
data model specification](https://developer.redoxengine.com/data-models/).

_**NOTE:**_ If you're looking for a library for working with Redox data, you're in
the wrong place. Search for `redox-parser` instead.

## About

`redox_lib_gen` creates Pydantic models using the Redox data schema and a [Jinja2
template](https://jinja.palletsprojects.com/en/3.0.x/templates/). The approach was
inspired by the work of the
[`fhir.resources`](https://pypi.org/project/fhir.resources/) library and the
[`fhir-parser`](https://github.com/nazrulworld/fhir-parser) project that generates
the majority of the `fhir.resources` code.


## But... why?

This utility provides two main benefits:

1. It prevents the need to manually create (and then manually verify) models that
   accurately reflect the JSON schema of the Redox data models.
2. It assists with ensuring the `redox-parser` library is up-to-date and consistent with
   the Redox schema in the event that the schema either (1) has more detail added to
   it or (2) gets updated by Redox (Redox promises that if an update to the schema
   is ever necessary, "[they] would notify all customers far in advance of the update
   and that in appropriate cases [they] would provide a transition plan to affected
   customers.")


## Running the Utility

Make sure your working directory is `redox_lib_gen` and activate the virtual
environment:

```shell
poetry shell
```

Then run the `generate.py` script:

```shell
cd redox_lib_gen && python3 generate.py
```

### Run Options

```
Usage: generate.py [OPTIONS]

  Generate Pydantic models from the Redox JSON specs.

Options:
  -d, --dst DIRECTORY        The directory where the redox-parser library will be
                             generated. NOTE: If the provided path already
                             exists, it will be deleted (along with its
                             contents) before the library is generated or
                             saved there.
  -c, --cache-dir DIRECTORY  The directory where the Redox schema will
                             downloaded and extracted. Any files in the
                             directory will be overwritten.
  --spec_url TEXT            [default: https://developer.redoxengine.com/data-
                             models/schemas.zip]
  -f, --force-download       Force a fresh download of the Redox specification
                             zip file. If not specified and the zip file has
                             already been downloaded, the local copy will be
                             used instead of downloading a fresh version of
                             the spec.
  --help                     Show this message and exit.
```
