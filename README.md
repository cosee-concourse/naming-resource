# Naming Resource

[![Build Status](https://travis-ci.org/cosee-concourse/naming-resource.svg?branch=master)](https://travis-ci.org/cosee-concourse/naming-resource) 
[![Docker Repository on Quay](https://quay.io/repository/cosee-concourse/naming-resource/status "Docker Repository on Quay")](https://quay.io/repository/cosee-concourse/naming-resource)

Generates names for various services using a prefix and the current version.

## Source Configuration

* `prefix`: *Required.* The prefix to be used in service names. Must only contain alphabetic characters and has to be 
   unique in order to not cause name conflicts in services.

## Behavior

### `check`: Extract versions of the archives from the bucket.

* Since this resource does not have a version itself `check` returns an empty JSON.

### `in`: Fetches artifacts from the bucket.

* Generates names for services and places them in files with the same name as the corresponding service. The default 
  output looks like this: *prefix_1_0_0_rc__10*

#### Parameters

* *None.*

### `out`: Upload artifacts as archive to the bucket.

* Retrieves a version generated by [semver](http://semver.org/) and makes it available to `in`.

#### Parameters
 
* `version`: *Required* Filepath to `semver` version file

## Example Configuration

### Resource Type
``` yaml
- name: service-naming
  type: docker-image
  source:
    repository: quay.io/cosee-concourse/naming-resource
```
### Resource

``` yaml
- name: naming
  type: service-naming
  source:
    prefix: uniqueprefix
```

### Plan

``` yaml
- get: naming
```

``` yaml
- put: naming
  params:
    version: version/number
```