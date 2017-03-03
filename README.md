# Frictionless Data Stack
General documentation container and issue tracker for the Frictionless Data stack.

# Stack Reference [draft]
## Architecture

![frictonless data 1](https://cloud.githubusercontent.com/assets/557395/17673886/d368f642-632b-11e6-9b59-3021952f09ca.png)
## Language
- row number - row number starting from 1
- col number - column number starting from 1
- headers - array of column names
- row - array of column values
- keyed row - dictionary of column values
- extended row - array containing row number, headers and row
- descriptor - dictionary describing something

## Interface

### goodtables

```
Inspector(checks='all', 
          table_limit=10,
          row_limit=1000, 
          error_limit=1000,
          order_fields=False,
          infer_fields=False)
    inspect(source, preset='table', **options)
~@check(code, type, context, before/after)
~@preset(name)
exceptions
spec
~cli
```
### datapackage

```
Datapackage(descriptor, profile='base', base_path=None, remote_profiles=False, raise_invalid=True)
    valid -> dict
    errors -> list
    profile -> str
    descriptor -> dict
    resources -> Resource[]
    update(descriptor)
    addResource(descriptor)
    removeResource(index)
    save(target)
Resource(descriptor, profile='base', base_path=None)
    type -> local/remote/inline
    source -> path/data
    profile -> str
    descriptor -> dict
    table -> jsontableschema.Table/None
validate(descriptor, profile='base', remote_profiles=False) -> raise/True
exceptions
~cli
```
### jsontableschema

```
Table(source, schema=None, post_cast=None, backend=None, **options)
    stream -> tabulator.Stream
    schema -> Schema
    iter(keyed/extended=False) -> (generator) (keyed/extended)row[]
    read(keyed/extended=False, limit=None) -> (keyed/extended)row[]
    save(target, backend=None, **options)
Schema(descriptor)
    descriptor -> dict
    fields -> Field[]
    headers -> str[]
    primary_key -> str[]
    foreign_keys -> str[]
    get_field(name) -> Field
    has_field(name) -> bool
    cast_row(row) -> row
    save(target)
Field(descriptor)
    descriptor -> dict
    name -> str
    type -> str
    format -> str
    required -> bool
    constraints -> dict
    cast_value(value, skip_constraints=False) -> value
    test_value(value, skip_constraints=False, constraint=None) -> bool
infer(headers, values) -> descriptor
validate(descriptor) -> raise/True
exceptions
~cli
---
Storage(**options)
    buckets -> str[]
    create(bucket, descriptor, force=False)
    delete(bucket=None, ignore=False)
    describe(bucket, descriptor=None) -> descriptor
    iter(bucket) -> (generator) row[]
    read(bucket) -> row[]
    write(bucket, rows)
plugins
```
### tabulator

```
Stream(source, 
       headers=None,
       scheme=None, 
       format=None,  
       encoding=None, 
       sample_size=None,
       post_parse=None,
       **options)
    closed/open/close/reset
    headers -> list
    sample -> rows
    iter(keyed/extended=False) -> (generator) (keyed/extended)row[]
    read(keyed/extended=False, limit=None) -> (keyed/extended)row[]
    save(target, format=None, encoding=None, **options)
    ::test(source, scheme=None, format=None)
exceptions
~cli
```
## References
- [RFC: Rows naming in tabular data representation](https://github.com/frictionlessdata/project/issues/284)

# Development Process [draft]

This document proposes a process to work on the technical side of the Frictionless Data project. The goal - have things manageable for a minimal price.

## Project

The specific of the project is a huge amount of components and actors (repositories, issues, contributors etc). The process should be effective in handling this specific. 

## Process

The main idea to focus on getting things done and reduce the price of maintaining the process instead of trying to fully mimic some popular methodologies. We use different ideas from different methodologies.

## Roles
- Product Owner (PO)
- Product Manager (PM)
- Developer Advocate (DA)
- Technical Lead (TL)
- Senior Developer (SD)
- Junior Developer (JD)

## Board

We use a kanban board located at https://waffle.io/frictionlessdata/project to work on the project. The board has following columns (ordered by issue stage):
- Backlog - unprocessed issues without labels and processed issues with labels
- Priority - prioritized issues planned for the next iterations (estimated and assigned)  
- Current - current iteration issues promoted on iteration planning (estimated and assigned)
- Review - issues under review process
- Done - completed issues

## Workflow

The work on the project is a live process splitted into 2 weeks iterations between iteration plannings (including retrospection):
- Inside an iteration assigned persons work on their current issues and subset of roles do issues processing and prioritizing
- During the iteration planning the team moves issues from the Priority column to the Current column and assign persons. Instead of issue estimations assigned person approves amount of work for the current iteration as a high-level estimation.

## Milestones

As milestones we use concrete achievements e.g. from our roadmap. It could be tools or spec versions like “spec-v1”. We don’t use the workflow related milestones like “current” of “backlog” managing it via the board labeling system.   

## Labels

Aside internal waffle labels and helpers labels like “question” etc we use core color-coded labels based on SemVer. The main point of processing issues from Inbox to Backlog is to add one of this labels because we need to plan releases, breaking announces etc:

![labels](https://cloud.githubusercontent.com/assets/557395/17673693/f6391676-632a-11e6-9971-945623b68e16.png)

## Assignments

Every issue in the Current column should be assigned to some person with meaning “this person should do some work on this issue to unblock it”. Assigned person should re-assign an issue for a current blocker. It provides a good real-time overview of the project. 

## Analysis

After planning it’s highly recommended for an assigned person to write a short plan of how to solve the issue (could be a list of steps) and ask someone to check. This work could be done on some previous stages by subset of roles.

## Branching

We use Git Flow with some simplifications (see OKI coding standards). Master branch should always be “green” on tests and new features/fixes should go from pull requests. Direct committing to master could be allowed by subset of roles in some cases.

## Pull Requests

A pull request should be visually merged on the board to the corresponding issue using “It fixes #issue-number” sentence in the pull request description (initial comment). If there is no corresponding issue for the pull request it should be handled as an issue with labeling etc.

## Reviews

After sending a pull request the author should assign the pull request to another person “asking” for a code review. After the review code should be merged to the codebase by the pull request author (or person having enough rights). 

## Documentation

By default documentation for a tool should be written in README.md not using additional files and folders. It should be clean and well-structured. API should be documented in the code as docstrings. We compile project level docs automatically.

## Testings

Tests should be written using OKI coding standards. Start write tests from top (match high-level requirements) to bottom (if needed). The most high-level tests are implemented as testsuites on project level (integration tests between different tools).

## Releasing

We use SemVer for versioning and Travis for testing and releasing/deployments. We prefer short release cycle (features and fixes could be released immediately). Releases should be configured using tags based on package examples workflow provided by OKI.

## References
- [Open Knowledge International Coding Standards](https://github.com/okfn/coding-standards)
- [Python Package Example](https://github.com/okfn/oki-py)
- [JavaScript Package Example](https://github.com/okfn/oki-js)
